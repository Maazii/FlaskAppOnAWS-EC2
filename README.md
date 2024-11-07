# FlaskAppOnAWS-EC2 for Windows

#### This is a starter project with the goal of running a flask application on an AWS EC2 instance, that was not created on the said EC2 instance.

## Prerequisites

- Installed Terraform
- Installed AWS CLI
- AWS Account with User Access Keys for AWS Resources and Network Access Keys (.pem file) for EC2 Instance. 

## AWS Configurations

Once you have all the above three it is time to configure AWS so that terraform is allowed to use AWS Resources through AWS CLI.

Open command prompt and type:

`aws --version`

to validate your installation.

Then type:

`aws configure`

You will be asked for four things:

- Public Access Key
- Private Access Key
- Region (for example ap-southeast-2)
- Output (choose this to be json)

Once done your AWS is configured.

## Choosing an Image in AWS

Login to AWS. Goto EC2 by searching for EC2 in the search bar. In the navigation menu on the left look for the Images heading and
then under it AMIs, and go to that. Once inside AMIs look at the left for the dropdown. If it is set to Owned by me then switch to Public Images.
Here you may choose the image or more simply the platform for your server (EC2) machine. In this project I chose ubuntu.

Once you find the desired image click on the left tickbox and you will see detailed information pop up below including that image's AMI-ID.
Keep this AMI-ID stored somewhere for quick access when needed.

## Launching Terraform

