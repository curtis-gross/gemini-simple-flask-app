//Copyright 2024 Google LLC
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//    https://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.


const uploadButton = document.querySelector('.custom-file-upload');
const fileInput = document.getElementById('image-upload');
const message = document.getElementById('upload-message'); // Select the existing <p> element
const form = document.querySelector('form');

uploadButton.addEventListener('click', () => {
        fileInput.click(); // Trigger the file input when the button is clicked
    });

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        message.textContent = 'Image ready for analysis.';
    } else {
        message.textContent = ''; // Clear the message if no file is selected
    }
    });

form.addEventListener('submit', (event) => {
    if (fileInput.files.length === 0) {
        event.preventDefault(); // Prevent form submission
        alert('Please upload an image first.');
    } else {
        message.textContent = 'Image uploaded. Analyzing...';
    }
    });
