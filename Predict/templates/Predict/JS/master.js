// Function to show the popup
function showPopup(result) {
    const popup = document.getElementById('resultPopup');
    const resultText = document.getElementById('resultText');
    resultText.textContent = result;
    popup.style.display = 'block';
  }
  
  // Function to close the popup
  function closePopup() {
    const popup = document.getElementById('resultPopup');
    popup.style.display = 'none';
  }
  
  // Function to handle image upload
  function uploadImage(event) {
    event.preventDefault(); // Prevent form submission
  
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];
  
    // Perform your image classification here using AI
  
    // Assume the result is stored in a variable called 'classificationResult'
    const classificationResult = 'Cat';
  
    showPopup(classificationResult);
  }
  