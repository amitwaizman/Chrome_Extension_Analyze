const fs = require('fs');
const fs1 = require('fs').promises;

//check if Obfuscated code or Malicious word


const folderPath = process.argv[2];
function file() {
var count = 0
fs.readdir(folderPath, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  files.forEach(async (file) => {
  var filePath = folderPath + "/" +  file
  const stat = await fs1.lstat(filePath);
  if (file.includes(".js") && stat.isFile()){
    
    const fileContent = fs.readFileSync(filePath , 'utf8');
    // Check for common patterns of obfuscation or malicious code
const isObfuscated = /eval\(|escape\(|unescape\(|\[\s?["'a-zA-Z]/.test(fileContent);
const isMalicious = /(?:\b|)(eval|setTimeout|setInterval|XMLHttpRequest)(?:\b|)/.test(fileContent);
const isScript = checkForMaliciousCode(fileContent)

// Output the results
if (isObfuscated) {
  count++
}
if (isMalicious) {
  count++
}
if (!isObfuscated && !isMalicious) {
  count--
}
if (isScript) {
  count++
}
}});
});

return new Promise(resolve => {
  setTimeout(() => {
    resolve(count);
  }, 2000);
});
}




function checkForMaliciousCode(jsCode) {
    if (jsCode.includes('eval(')) {
      return true;
    }
  
    if (jsCode.includes('Function(')) {
      return true;
    }
  
    if (jsCode.includes('setTimeout(')) {
      const setTimeoutCalls = jsCode.match(/setTimeout\((.*)\)/g);
      try {
      for (const setTimeoutCall of setTimeoutCalls) {
        const setTimeoutParams = setTimeoutCall.match(/setTimeout\((.*)\)/)[1];
        if (setTimeoutParams.startsWith('"') && setTimeoutParams.endsWith('"')) {
          return true;
        }
      }
    }
    catch(err){
      return true;
    }
    }
  
    return false;
  }

  async function asyncCall() {
    const result = await file();
    console.log(result);
  }
  
  asyncCall();
  
  