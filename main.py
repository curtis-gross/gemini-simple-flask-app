#Copyright 2024 Google LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#    https://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from flask import Flask, render_template, request
import base64
import io
from vertexai.preview.generative_models import GenerativeModel, Part, GenerationConfig
import tempfile
import os
from utils.prompts import imageprompt,image_analysis_output, markdown_testing #put the prompts in a seprate file.
import markdown

app = Flask(__name__, template_folder='templates', static_folder='static')  # Initialize Flask app

# Define the model that will be used to process your text
model = GenerativeModel("gemini-1.5-pro")

def vertex_upload_and_analyze_image(uploaded_file, image_prompt, image_analysis_output): # This function sends an image, a prompt of what to do, and a secondary prompt that tells Gemini how to respond.
    try:
        # You can also tweak the generation config (look it up!) to send a schema and have Gemini send back JSON instead of text.
        # Combine the prompts to instruct Gemini on the task and desired output format
        #this prompt combines itself with the image prompt and output prompt that are both in prompts.py.
        #you can simplify this of course or you can give the user the ability to modify portions.
        image_prompt = f"""
            Task: Analyze this image and follow these instructions {image_prompt}. 
            Task: Your output should be {image_analysis_output}. 
            If you are not confident in an answer, return Unknown
            return HTML, return tables.
        """
        # Get the image content (directly from the in-memory file object)
        image_content = uploaded_file.getvalue()
        # Convert to Vertex required base64
        image1 = base64.b64encode(image_content).decode('utf-8')  
        # Use 'Part' function from Vertex AI to prepare the image
        image_ready = Part.from_data(image1, mime_type="image/jpeg")  
        # Send prompt and image to the model
        response = model.generate_content([image_prompt, image_ready])  
        print(response.text)
    except Exception as e:
        print(f"Vertex AI Service Unavailable: {e}")
        return "Error: Image analysis service is temporarily unavailable. Please try again later."  # Return error message and 503 status code
    return response.text


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded file
        uploaded_file = request.files["image"]

        if uploaded_file:
            try:
            # Save the uploaded image to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    uploaded_file.save(temp_file.name)
                    image_path = temp_file.name

                # Read the image data
                with open(image_path, "rb") as image_file:
                    image_data = image_file.read()
                    image_bytes = io.BytesIO(image_data)

                # Encode image to base64
                image_b64 = base64.b64encode(image_bytes.getvalue()).decode()

                # Analyze the image : Comment this out and and you can test without live data by replacing the output with 
                # a sample output.
                markdown_response = vertex_upload_and_analyze_image(image_bytes, imageprompt, image_analysis_output)
                output = markdown.markdown(markdown_response,
                                           extensions=[
                                            'markdown.extensions.tables',  # Enable the tables extension
                                            'markdown.extensions.fenced_code'  # Enable the fenced code blocks extension (if needed)
                                           ])
                # Remove the temporary image file
                os.remove(image_path)

                # Render the template with the image and analysis results
                return render_template("index.html", image_b64=image_b64, output=output)
            except Exception as e:
                # Handle other exceptions
                print(f"An error occurred: {e}")
                return "An unexpected error occurred. Please try again later.", 500

    # If it's a GET request, just render the template
    return render_template("index.html")

if __name__ == "__main__":
    # Set environment variables for Flask
    os.environ["FLASK_ENV"] = "development"  # Enable development mode

    # Start the Flask app
    app.run(
        host="0.0.0.0",  # Listen on all available network interfaces
        port=int(os.environ.get("PORT", 8080)),  # Use the PORT environment variable if available
        debug=True  # Enable debug mode
    )