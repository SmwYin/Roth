// Run in functions.exec, with store('root_native_request_path', ABS_REQUEST_JSON).
const requestPath=load('root_native_request_path');
if(typeof requestPath!=='string')throw Error('Missing explicit root request path');
const sq=s=>"'"+s.replace(/'/g,"'\\''")+"'";
const prep=await tools.exec_command({cmd:'python3 /private/tmp/roth-overview/prepare_root_native_request.py '+sq(requestPath),workdir:'/Users/ramin/LEAN/Roth',max_output_tokens:50000});
if(prep.exit_code!==0)throw Error('Native preparation failed: '+prep.output);
const p=JSON.parse(prep.output);
const tool={diagnostics:'mcp__lean_lsp__lean_diagnostic_messages',run_code:'mcp__lean_lsp__lean_run_code',local_search:'mcp__lean_lsp__lean_local_search'}[p.operation];
if(typeof tools[tool]!=='function')throw Error('Required tool unavailable: '+tool);
const t=Date.now();let result,transportFailure;
try{result=await tools[tool](p.arguments);}catch(e){transportFailure=String(e);}
const elapsed_ms=Date.now()-t;
const record={request:p.arguments,elapsed_ms,executor:{owner:'root',worker_request:p.worker_request,request_file:requestPath,source_archive:p.source,preexecution_audit:p.preexecution_audit}};
if(transportFailure)record.transport_failure=transportFailure;else record.result=result;
const ascii=JSON.stringify(record,null,2).replace(/[\u007f-\uffff]/g,c=>'\\u'+c.charCodeAt(0).toString(16).padStart(4,'0'));
await tools.apply_patch('*** Begin Patch\n*** Add File: '+p.receipt+'\n'+ascii.split('\n').map(x=>'+'+x).join('\n')+'\n*** End Patch');
const z=result?.structuredContent?.result??result?.structuredContent??{};
const ds=z.items??z.diagnostics??[];
text({id:p.id,operation:p.operation,receipt:p.receipt,elapsed_ms,transport_failure:transportFailure??null,isError:result?.isError??false,success:z.success??null,partial:z.partial??null,timed_out:z.timed_out??null,errors:ds.filter(x=>x.severity==='error').length,warnings:ds.filter(x=>x.severity==='warning').length,items:ds.length,index:z.index??null});
