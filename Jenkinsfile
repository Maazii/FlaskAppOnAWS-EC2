pipeline {
    agent any

    environment {
        TF_VAR_REGION = "us-east-1"
        PATH = "C:\\terraform\\terraform.exe"
    }
    
    stages {
        stage("Check bat"){
            steps{
                bat "echo Hello World!"
            }
        }
    }
}