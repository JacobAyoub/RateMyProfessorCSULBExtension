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
      outputElement.textContent = `Error: ${error.message}`;
    }
    document.getElementById("iframe").src = "ratings.html";
  }
  function changeToReview()
  {
    document.getElementById("iframe").src = "ratings.html";

  }
  function changeToComment()
  {
    document.getElementById("iframe").src = "comments.html";
  }
  document.getElementById("button").addEventListener("click", runPythonScript);
  document.getElementById("reviewButton").addEventListener("click", changeToReview);
  document.getElementById("commentButton").addEventListener("click", changeToComment);