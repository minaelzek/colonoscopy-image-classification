# Colonoscopy Image Classification

This repository contains a web application for classifying colonoscopy images as 'Normal' or 'Abnormal' using a pre-trained deep learning model.

## Purpose

The purpose of this repository is to provide a tool for medical professionals to quickly and accurately classify colonoscopy images. This can help in early detection and diagnosis of abnormalities in the colon.

## Environment Setup

To set up the environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, follow these steps:

1. Ensure that the virtual environment is activated:
   ```bash
   source venv/bin/activate
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Using the Application

To use the application, follow these steps:

1. Open the web application in your browser.
2. Upload a colonoscopy image using the provided form.
3. The application will process the image and display the classification result along with the confidence percentage.

## Training the Model

To train the model, follow these steps:

1. Prepare your dataset of colonoscopy images, ensuring that they are labeled as 'Normal' or 'Abnormal'.
2. Use a deep learning framework such as TensorFlow or Keras to define and train your model.
3. Save the trained model to a file (e.g., `model.h5`).

The pre-trained model file should be placed in the root directory of the repository and named `model.h5`.

