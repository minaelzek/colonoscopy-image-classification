from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
try:
    model = tf.keras.models.load_model('path_to_your_model.h5')
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

def preprocess_image(image):
    image = image.resize((224, 224))  # Resize the image to match the model's input size
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                image = Image.open(file.stream)
                processed_image = preprocess_image(image)
                if model:
                    predictions = model.predict(processed_image)
                    confidence = predictions[0][0]
                    classification = 'Abnormal' if confidence > 0.5 else 'Normal'
                    confidence_percentage = confidence * 100 if classification == 'Abnormal' else (1 - confidence) * 100
                    return render_template('index.html', classification=classification, confidence=confidence_percentage)
                else:
                    return render_template('index.html', classification="Error", confidence="Model not loaded")
            except Exception as e:
                return render_template('index.html', classification="Error", confidence=f"File upload error: {e}")
    return render_template('index.html', classification=None, confidence=None)

if __name__ == '__main__':
    app.run(debug=True)
