# steelconnect-dialogflow
[![Build Status](https://travis-ci.com/finnhartshorn/apiai_webhook.svg?token=n8h3qqFcVcWaMV7ck3Aq&branch=master)](https://travis-ci.com/finnhartshorn/apiai_webhook)

A webhook for handling calls from the SteelConnect DialogFlow Agent

Hosted on Google Cloud Platform App Engine at https://steelconnect-dialogflow.appspot.com/

## How to install on Google App Engine

### Creating an App Engine Project
Go to https://console.developers.google.com/apis/dashboard
Select 'Select a project' in the top left
Create a new project using the '+' button
The projects id will be used as its address (app-id.appsport.com). Note your project's id down as you will need it later.

Install and configure the Google Cloud SDK by following the instructions here - https://cloud.google.com/sdk/docs/
On Windows this will install the Google Cloud SDK Shell which can be used to deploy the app, on OSX and Linux simply use the terminal.
Install the app engine python extension by entering 'gcloud components install app-engine-python' into the Google Cloud SDK Shell if on Windows or the terminal for OSX and Linux

You can either clone the repository using git or download a zip
### Cloning using Git
If git is not already installed get it here https://git-scm.com/
Clone this project using 'git clone https://github.com/finnhartshorn/apiai_webhook.git'
### Downloading the Zip
Use this link https://github.com/finnhartshorn/apiai_webhook/archive/master.zip

### Deploying
Fill out 'default-auth.json' with the details of your SCM account and organisation.
To deploy the app open Google Cloud SDK Shell/terminal switch to the apps directory via 'cd /path/to/steelconnect-dialogflow/' and run 'gcloud app deploy'

### Using Dialogflow
Click the settings icon next to your agent's name.
Click 'Export and Import' and then select 'Restore from Zip'
Upload the 'SteelConnect-Dialogflow.zip' file from the repository.
Last step is to enable the webhook under Fullfillment and use 'https://your-project-id.appspot.com/webhook/' as the url.

You can now use Dialogflow to the test out the intents on your realm and organisation.
