ObjC.import('Foundation');
function fail(s) { throw new Error(s); }
function textFile(path) { return ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError(path, $.NSUTF8StringEncoding, null)); }
function policy() { return JSON.parse(textFile(ObjC.unwrap($.NSHomeDirectory()) + '/Library/Application Support/Steward/apple-policy.json')); }
function guardWrite(app, id) {
    var entry = (policy()[app] || {})[id];
    if (!entry || entry.write !== true) fail('Write blocked: shared or unknown container');
    var age = Date.now() - Date.parse(entry.privateVerifiedAt);
    if (app !== 'notes' && (!Number.isFinite(age) || age < -60000 || age > 900000)) fail('Private status needs a fresh app UI check');
}
function exactly(items, id, getID) {
    var found = items.filter(function(x) { return getID(x) === id; });
    if (found.length !== 1) fail('ID missing or ambiguous'); return found[0];
}
function escapeHTML(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function body(title, text) { return '<h1>' + escapeHTML(title) + '</h1><div>' + escapeHTML(text).replace(/\n/g,'<br>') + '</div>'; }
function noteJSON(n, full) {
    var result = {id:n.id(),title:n.name(),shared:n.shared(),locked:n.passwordProtected(),modified:n.modificationDate().toISOString()};
    if(full && !result.locked) { result.text=n.plaintext(); result.html=n.body(); result.attachments=n.attachments().length; }
    return result;
}
function run(argv) {
    try {
        var r = JSON.parse(textFile(argv[0])), app;
        var allowed=['connect','containers','list','get','create','update','delete','create-container','rename-container','delete-container'];
        if(allowed.indexOf(r.op)<0) fail('Unsupported operation');
        if(['create','update','delete','create-container','rename-container','delete-container'].indexOf(r.op)>=0 && r.apply!==true) return JSON.stringify({state:'preview',request:r});
        if(r.app !== 'notes') fail('This script handles Notes only');
        app=Application('Notes');
        if(['connect','containers'].indexOf(r.op)>=0) {
            return JSON.stringify({containers:app.folders().map(function(f){return {id:f.id(),name:f.name(),shared:f.shared(),container:f.container().id()};}),sources:app.accounts().map(function(a){return {id:a.id(),name:a.name()};})});
        }
        if(r.op==='create-container') {
            if(policy().allowContainerCreation!==true) fail('Container creation disabled');
            var a=exactly(app.accounts(),r.source,function(x){return x.id();});
            if(a.folders().some(function(f){return f.name()===r.name;})) fail('Folder already exists; inspect instead of duplicating');
            var newFolder=app.Folder({name:r.name}); a.folders.push(newFolder);
            return JSON.stringify({state:'created',container:{id:newFolder.id(),name:newFolder.name(),shared:newFolder.shared()}});
        }
        var folder=exactly(app.folders(),r.calendar,function(x){return x.id();});
        if(r.op==='list') return JSON.stringify({items:folder.notes().map(function(n){return noteJSON(n,false);})});
        if(r.op==='get') return JSON.stringify({item:noteJSON(exactly(folder.notes(),r.id,function(x){return x.id();}),true)});
        guardWrite('notes',r.calendar);
        if(folder.name()==='Recently Deleted') fail('Recently Deleted is read-only; permanent removal requires a separate explicit workflow');
        if(folder.shared()) fail('Shared folder writes are blocked');
        if(r.op==='rename-container') { folder.name=r.name; return JSON.stringify({state:'renamed',container:{id:folder.id(),name:folder.name()}}); }
        if(r.op==='delete-container') {
            if(folder.notes().length || folder.folders().length) fail('Folder is not empty; bulk deletion requires a separate reviewed workflow');
            app.delete(folder);
            if(app.folders().some(function(f){return f.id()===r.calendar;})) fail('Folder deletion unverified');
            return JSON.stringify({state:'deleted',id:r.calendar});
        }
        var f=r.fields||{}, marker='[steward:'+r.token+']', n;
        if(r.op==='create') {
            if(f.appendText!==undefined) fail('Use text for new note content');
            var found=folder.notes().filter(function(x){return !x.passwordProtected() && x.plaintext().indexOf(marker)>=0;});
            if(found.length) return JSON.stringify({state:'existing',item:noteJSON(found[0],true)});
            n=app.Note({body:body(f.title,(f.text||'')+'\n\n'+marker)});folder.notes.push(n);
        } else {
            n=exactly(folder.notes(),r.id,function(x){return x.id();});
            if(n.shared() || n.passwordProtected()) fail('Shared or locked note writes are blocked');
            if(r.op==='delete') {
                app.delete(n);
                if(folder.notes().some(function(x){return x.id()===r.id;})) fail('Note deletion unverified');
                return JSON.stringify({state:'deleted',id:r.id});
            }
            if(r.op!=='update') fail('Unsupported operation');
            if(r.expectedModified!==n.modificationDate().toISOString()) fail('Read note first; expectedModified must match before update');
            var html=n.body();
            if(n.attachments().length || /<(table|object|img)|Apple-dash-list|data-checked|Apple-checkbox/i.test(html)) fail('Rich note requires Notes UI to preserve attachments, tables and checklists');
            if(r.expectedModified!==n.modificationDate().toISOString()) fail('Note changed during inspection; reread before updating');
            if(f.appendText!==undefined) n.body=html+'<div>'+escapeHTML(f.appendText).replace(/\n/g,'<br>')+'</div>';
            if(f.text!==undefined) {
                if(r.expectedModified!==n.modificationDate().toISOString()) fail('Read note first; expectedModified must match before replacing text');
                var oldMarker=n.plaintext().match(/\[steward:[0-9a-f-]+\]/i);
                n.body=body(f.title||n.name(),f.text+(oldMarker?'\n\n'+oldMarker[0]:''));
            } else if(f.title!==undefined) n.name=f.title;
        }
        return JSON.stringify({state:'saved',item:noteJSON(n,true)});
    } catch(e) { return JSON.stringify({state:'failed-or-uncertain',error:String(e)}); }
}
