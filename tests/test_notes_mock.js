// Exercise native gates without opening any Apple app.
const vm = require('node:vm');
const fs = require('node:fs');
const assert = require('node:assert/strict');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../skills/steward-apple/scripts/notes.js'), 'utf8');
for (const op of ['create','update','delete','create-container','rename-container','delete-container']) {
  const request = {app:'notes',op,apply:false};
  const context = {ObjC:{import(){},unwrap(x){return x;}}, $:{NSString:{stringWithContentsOfFileEncodingError(){return JSON.stringify(request);}}}, Application(){throw new Error('Must not access app during preview');}};
  vm.createContext(context);vm.runInContext(source,context);
  const result=JSON.parse(context.run(['fixture.json']));
  assert.equal(result.state,'preview');
  assert.equal(result.error,undefined);
}
for (const app of ['notes','calendar']) {
  const request={app,op:'unknown',apply:true};
  const context={ObjC:{import(){},unwrap(x){return x;}},$:{NSString:{stringWithContentsOfFileEncodingError(){return JSON.stringify(request);}}},Application(){throw new Error('Unexpected app access');}};
  vm.createContext(context);vm.runInContext(source,context);
  assert.match(JSON.parse(context.run(['fixture.json'])).error,/Unsupported operation/);
}
console.log('PASS: native preview and unknown-operation gates; no Apple apps accessed');
