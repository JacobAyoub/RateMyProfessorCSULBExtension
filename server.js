const express = require('express');
const cors = require('cors'); // Import CORS
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(cors()); // Enable CORS for all routes
app.use(express.json());

app.post('/run-python', (req, res) => {
  const { professorName } = req.body;

  const pyProg = spawn('python', ['TeacherInfo.py', professorName]);

  let data = '';
  pyProg.stdout.on('data', (stdout) => {
    data += stdout.toString();
  });

  pyProg.stderr.on('data', (stderr) => {
    console.error(`stderr: ${stderr}`);
    res.status(500).send(`Error: ${stderr}`);
  });

  pyProg.on('close', (code) => {
    if (code === 0) {
      res.send(data);
    } else {
      res.status(500).send('Python script execution failed');
    }
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});