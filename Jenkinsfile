pipeline {
    agent any

    environment {
        TF_VAR_REGION = "us-east-1"
        PATH = "C:\\terraform\\terraform.exe"
    }
    
    stages {
        stage("Check CMD"){
            steps{
                bat "C:\\Windows\\System32\\cmd.exe /c Hello World!"
            }
        }
    }
}