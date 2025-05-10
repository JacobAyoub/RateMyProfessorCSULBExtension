  button = document.getElementById("reviewButton");
  button2 = document.getElementById("commentButton");
async function runPythonScript() {
    const professorName = document.getElementById('professorName').value;
    const outputElement = document.getElementById('output');

    // Clear previous output
    outputElement.textContent = 'Loading...';

    try {
      // Send a POST request to the backend
      const response = await fetch('http://localhost:3000/run-python', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ professorName }),
      });

      if (!response.ok) {
        throw new Error('Professor not found. Please check your spelling.');
      }

      // Display the scraped data
      const data = await response.text();
      outputElement.textContent = data;
    } catch (error) {
      outputElement.textContent = "Error: Database/Backend is currently not enabled";
    }
    document.getElementById("iframe").src = "ratings.html";
    button.style.backgroundColor = "White";
    button2.style.backgroundColor = "skyblue";
  }
  function changeToReview()
  {
    document.getElementById("iframe").src = "ratings.html";
    button.style.backgroundColor = "White";
    button2.style.backgroundColor = "skyblue";
  }
  function changeToComment()
  {
    document.getElementById("iframe").src = "comments.html";
    button2.style.backgroundColor = "White";
    button.style.backgroundColor = "skyblue";
  }
  document.getElementById("button").addEventListener("click", runPythonScript);
  button.addEventListener("click", changeToReview);
  button2.addEventListener("click", changeToComment);