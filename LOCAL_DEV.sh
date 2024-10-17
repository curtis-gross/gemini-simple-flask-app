#!/bin/bash
echo "First, get your python virtual env created"
echo "go into gcp and create a service account, create keys, download them, add them into a folder called 'keys'"
echo "then run source LOCAL_DEV.sh"
export GOOGLE_APPLICATION_CREDENTIALS="../keys/key.json"
source ../../pipenv/bin/activate
export FLASK_APP=main.py
echo "run:  export FLASK_APP=main.py"
echo "Now run : flask run --debug"
echo "to deploy make your cloud_run.sh file runnable with chmod 755 or "
echo "just copy / paste the code in there into your command line."