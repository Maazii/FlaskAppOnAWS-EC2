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

## Choosing An Image In AWS

Login to AWS. Goto EC2 by searching for EC2 in the search bar. In the navigation menu on the left look for the Images heading and
then under it AMIs, and go to that. Once inside AMIs look at the left for the dropdown. If it is set to Owned by me then switch to Public Images.
Here you may choose the image or more simply the platform for your server (EC2) machine. In this project I chose ubuntu.

Once you find the desired image click on the left tickbox and you will see detailed information pop up below including that image's AMI-ID.
Keep this AMI-ID stored somewhere for quick access when needed.

## Placing Your Network Keypair In Your Directory

Make sure that the key pair file (the one with its as extension as .pem) is also present in the same directory as the terraform files and the app.py

## Launching AWS Resources Using Terraform

This is where all the files in this repository will come into play. Download them or simply use a `git pull` or whatever you wish into your
working directory.

Once done open a shell terminal and guide it to the directory where you have the terraform files and the python file and execute `terraform init`

Once initialized successfully execute `terraform validate`. This verifies if there are any bugs in all the **.tf** files you have. And I know your mind right now might be a bit overwhelmed with all the files and thinking wait a minute, do I need to execute them individually or not, or which one I shall execute first.

Let me reassure you you do not need to worry. Terraform will organize all of them for you when it starts working with them.

So now, if `terraform validate` was successful execute `terraform plan`. This command will provide all the actions Terraform is going to be taking, such as modifications of any resources or creating resources.

Upon execution of `terraform plan` you will be asked for three things:

- AMI-ID
- Keypair Name | **This is NOT the Access Key Pair name. This is what you create in EC2 -> Network and Security -> Key Pairs. When entering the name, make sure to need include any extensions such as .pem or .ppk, just the name of Key Pair as it is in your AWS.
- InstanceName | This is more of a tag and can be of your choice.

Finally, if there have been no hiccups, execute `terraform apply`. This is the command after which Terraform will start pulling AWS Resources and this is where you can potentially incur costs in some scenarios but obviously due to the setup in this repository it is not the case as of writing this.

*However, please note that despite the Free-Tier setup in this repository there are limitations to Free-Tier. You would be wise to look them up yourselves but generally what I am aware of they are that after one year of Free-Tier you will incur costs no matter what, and there are also limitations while using Free-Tier for example the EC2 instance provides 750 hours of free usage each month. After which you will have to pay for your usage. Rely on the Cost Explorer in Billing and Cost Management after logging into AWS to keep track of your usage.*

Once you run `terraform apply` you will be asked a final confirmation here once you will be asked for the three pieces of  information you were asked after running `terraform plan`, type `yes` and enter after which you will your resources being created by Terraform. Terraform will report if there were any errors or if the creation of resources was successful.

If successful go to your AWS, then EC2 -> Instances, and check for running instances. You should see the InstanceName you entered after running `terraform plan` and `terraform apply`. To the left of it there will be a tickbox. Tick it and you will see detailed information for your instance pop up below.

Congratulations! You have now successfully pulled and ran an AWS-EC2 using Terraform.

## SSH Into Your EC2 Instance

Now this is the crucial step of the project. Despite this, there is not a lot you will have to do in this given the terraform files in the repository take care of everything.

Once again open command prompt and navigate to the directory that has your terraform files. At the same time go to your running instance on AWS, tick the tickbox left on the left
and you will see that the connect button on the top right is now available. Click on it and you will be taken to a screen wher you will see tabs one which says **SSH**.
Click on SSH, scroll down to see a command that looks like the following structure:

`ssh -i "path\to\your\network\key" ubuntu@your-machine's-dns`

Copy it, paste it into your command prompt. You might be asked to add your key pair to your list, so allow it, and if everything has been correct upto this point you will have
logged into your EC2 instance!

## Adding and Executing the Python File to Your Instance

Before you do this, you should update and upgrade packages on your ubuntu machine.

Run:

`sudo apt update && sudo apt upgrade`

Install Python and Pip:

`sudo apt install python3 python3-pip`

You can verify the installation as follows:

`python3 --version`
`pip3 --version`

After which install Flask and Flask Async as they are the dependencies for the Flask app.

`pip3 install Flask`
`pip3 install Flask[async]`

Once done, now we shall move onto bringing the app to your instance.

You can rely on `scp`, that is secure copy, which comes with built-in OpenSSH in Windows 10 and 11, to achieve this as follows:

`scp -i /path/to/your-key.pem /path/to/your/flask-app/ ubuntu@<your-ec2-dns>:/home/ubuntu/`

Once added, execute the python file, and goto

`http://<your-ec2-dns>:5000`

and you should see a small **Hello!** on the top left of the page.

And Voila! You are running the Flask application in your instance.

Curiously enough, the Flask app is not simply a home page saying Hello! as text. It is somewhat more. I will leave that upon your curiousity to discover.