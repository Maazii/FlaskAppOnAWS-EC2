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

## Launching AWS Resources using Terraform

This is where all the files in this repository will come into play. Download them or simply use a `git pull` whatever you wish into your
working directory.

Once done open a shell terminal and guide it to the directory where you have the terraform files and the python file and execute `terraform init`

Once initialized successfully execute `terraform validate`. This verifies if there are any bugs in all the **.tf** files you have. And I know your mind right now might be a bit overwhelmed with all the files and thinking wait a minute, do I need to execute them individually or not, or which one I shall execute first.

Let me reassure you you do not need to worry. Terraform will organize all of them for you when it starts working with them.

So now, if `terraform validate` was successful execute `terraform plan`. This command will provide all the actions Terraform is going to be taking, such as modifications of any resources or creating resources.

Finally, if there have been no hiccups, execute `terraform apply`. This is the command after which Terraform will start pulling AWS Resources and this is where you can potentially incur costs in some scenarios but obviously due to the setup in this repository it will not be the case.

*However, please note that despite the Free-Tier setup in this repository there are limitations to Free-Tier. You would be wise to look them up yourselves but generally what I am aware of they are that after one year of Free-Tier you will incur costs no matter what, and there are also limitations while using Free-Tier for example the EC2 instance provides 750 hours of free usage each month. After which you will have to pay for your usage. Rely on the Cost Explorer in Billing and Cost Management to keep track of your usage.*