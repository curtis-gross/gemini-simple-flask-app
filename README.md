# Starter App
This application is meant to be as simple as possible to get a cloud run + gemini application runing.

- You will need to get your local development environment configured to work with gcloud
- https://cloud.google.com/sdk/docs/install-sdk
- Install Python
- Create a Python virtual environment
- Install requirements (in requirements.txt)

# Run / Dev
- gunicorn main:app

# Deploy
- change the cloudrun.sh file to be runnable. chmod 755

# The app:
- There is a default prompt, output prompt and default image. 
- You can press 'go' to see the results or upload your own image.