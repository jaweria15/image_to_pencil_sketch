from flask import Flask, request, send_file, render_template
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        invert = 255 - grey_image
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        inverted_blur = 255 - blur
        sketch_filter = cv2.divide(grey_image, inverted_blur, scale=256.0)
        cv2.imwrite('static/sketch.png', sketch_filter)  # Save sketch in static folder to be accessible
        return send_file('static/sketch.png', as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
