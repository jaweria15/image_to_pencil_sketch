# Importing necessary Libraries 
from flask import Flask, request, send_file, render_template
import cv2
import numpy as np
# Initializing Flask app

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image file from the user input
        image_file = request.files['image']
        # Read the image file and convert it to an OpenCV format

        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        # Convert the image to grayscale

        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Invert the grayscale image

        invert = 255 - grey_image

        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        # Invert the blurred image

        inverted_blur = 255 - blur
        # Create a sketch effect 
        
        sketch_filter = cv2.divide(grey_image, inverted_blur, scale=256.0)
        # save the picture into a static folder 

        cv2.imwrite('static/sketch.png', sketch_filter)
        
        return send_file('static/sketch.png', as_attachment=True)
        # If the request is GET, render the HTML page (index.html)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
