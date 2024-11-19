pipeline {
    agent any

    environment {
        TF_VAR_REGION = "us-east-1"
        PATH = "C:\\terraform\\terraform.exe"
    }
    
    stages {
        stage("Checkout Terraform Code"){
            steps {
                git branch: 'main', changelog: false, credentialsId: 'Github-SSH-Private', poll: false, url: 'git@github.com:Maazii/FlaskAppOnAWS-EC2.git'
            }
        }
        stage("Initialize Terraform"){
            steps {
                bat "terraform init"
            }
        }
        stage("Validate Configuration"){
            steps {
                bat "terraform validate"
            }
        }
    }
}