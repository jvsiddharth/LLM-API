const { spawn } = require('child_process');

function generateReply(message) {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python', ['A:/projects/NodeJS/chatbot-server/script.py']);

    pythonProcess.stdin.write(message + '\n');
    pythonProcess.stdin.end();

    let output = '';

    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      reject(data.toString());
    });

    pythonProcess.on('close', (code) => {
      if (code === 0) {
        resolve(output.trim());
      } else {
        reject(`Python script exited with code ${code}`);
      }
    });
  });
}

// Usage example
generateReply("Hello, how are you?")
  .then(reply => console.log("Bot:", reply))
  .catch(error => console.error(error));
