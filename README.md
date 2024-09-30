# Image to Pencil Sketch Converter

This project is a simple web application that allows users to upload an image and convert it to a pencil sketch. The frontend is built using HTML, CSS, and JavaScript, and the backend uses Python with OpenCV for image processing.

## Features

- Upload any image (JPEG/PNG) and convert it to a pencil sketch.
- Real-time image preview before conversion.
- Simple, user-friendly interface.
- Download the converted sketch image.

## Technologies Used

### Frontend:
- **HTML**: For structuring the webpage.
- **CSS**: For styling the application.
- **JavaScript**: For handling user interactions and sending the image to the backend.

### Backend:
- **Python**: The logic to convert images to pencil sketches.
- **Flask**: Lightweight framework for handling API requests.
- **OpenCV**: Used for image processing to create the pencil sketch effect.

## How It Works

1. **Upload an Image**: Users can upload an image from their local system.
2. **Image Processing**: The image is sent to the backend where OpenCV processes it to generate a pencil sketch.
3. **Download**: The converted pencil sketch is returned to the user, and they can download it.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/image-to-pencil-sketch.git
cd image-to-pencil-sketch
