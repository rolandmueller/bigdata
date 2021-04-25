# Deployment with CapRover

## Apply for GitHub Student Developer Pack

Apply for the free GitHub Student Developer Pack at: https://education.github.com/pack

## Register a Domain Name

Use either https://www.name.com/ or https://www.namecheap.com/ for registering a domain name (you might want to use the GitHub Student Developer Pack discount)

## Register at a Cloud Provider for a Virtual Private Server (VPS)

Register at https://www.digitalocean.com/ via your GitHub Student Developer Pack to get $100 in platform credit for new users.

## Install CapRover on your VPS

Instructions:
- https://www.youtube.com/watch?v=VPHEXPfsvyQ 
- https://caprover.com/docs/get-started.html 

On DigitalOcean you can select a Droplet with CapRover preinstalled. 
Alternativly you have to install on the server a) Docker (also available as a Droplet or manual installation) and b) CapRover.

## Install CapRover CLI (Command Line Interface) on your laptop

- https://caprover.com/docs/get-started.html#step-3-install-caprover-cli 


## Create a CapRover captain-definition file

CapRover has different ways to define how to deploy an application through a Captain Definition File `captain-definition`, see https://caprover.com/docs/captain-definition-file.html for more details.

We will use a Dockerfile for the deployment: https://caprover.com/docs/captain-definition-file.html#use-dockerfile-in-captain-definition 

- Go into your Streamlit application folder from the last exercise
- Create a new file with the name `captain-definition`

put in the `captain-definition` the following content:
```json
 {
  "schemaVersion": 2,
  "dockerfilePath": "./Dockerfile"
 }
```

## On the Server, create an App

Go to your the CapRover server web dashboard and create your app

## On the Laptop, your App

In the folder of your Streamlit app, execute in the Terminal:

```bash
caprover deploy
```

## Enable HTTPS

On the server, enable HTTPS for your main CapRover Dashboard and your Streamlit app

Deliverable: Copy the URL of your deployed Streamlit App to Moodle

