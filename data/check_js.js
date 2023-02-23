const fs = require('fs');
const readline = require('readline');
const fs1 = require('fs').promises;
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });


// var folderPath = ""
// rl.question('', (name) => {
//   console.log(`Hello, ${name}`);
//   folderPath = name
//   rl.close();
// });

const folderPath = process.argv[2];
// const folderPath = '/home/rivka/Desktop/chr/chromes/good/30'; // Replace with your folder path
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
  // console.log('The file contains obfuscated code');
  count++
}
if (isMalicious) {
  // console.log('The file contains potentially malicious code');
  count++
}
if (!isObfuscated && !isMalicious) {
  // console.log('The file seems to be clean');
  count--
}
if (isScript) {
  // console.log('isScript');
  count++
}
}});
});

return new Promise(resolve => {
  setTimeout(() => {
    resolve(count);
  }, 2000);
});
// console.log(count);
}
// Read the file contents
// const fileContent = fs.readFileSync('/home/rivka/Desktop/chr/chromes/good/0/background.js', 'utf8');




function checkForMaliciousCode(jsCode) {
    // Check for use of eval
    if (jsCode.includes('eval(')) {
      return true;
    }
  
    // Check for use of Function
    if (jsCode.includes('Function(')) {
      return true;
    }
  
    // Check for use of setTimeout with a string parameter that can be modified by user input
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
  
    // If none of the checks above returned true, the code is probably not malicious
    return false;
  }

  async function asyncCall() {
    const result = await file();
    console.log(result);
    // Expected output: "resolved"
  }
  
  asyncCall();
  
  