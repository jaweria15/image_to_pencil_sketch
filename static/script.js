document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent the default form submission

    const form = event.target;
    const formData = new FormData(form);  // Create a FormData object to handle the file

    fetch("/", {
        method: "POST",
        body: formData  // Send the form data to the backend
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error processing the image!");
        }
        return response.blob();  // Convert the response to a Blob (binary data)
    })
    .then(blob => {
        // Create an object URL from the Blob and display the image
        const imageUrl = URL.createObjectURL(blob);
        document.getElementById("sketchImage").src = imageUrl;
        document.getElementById("output").style.display = "block";  // Make sure the container is visible
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error processing your image. Please try again.');
    });
});
