pipeline {
    agent any

    environment {
        TF_VAR_REGION = "us-east-1"
        PATH = "C:\\terraform\\terraform.exe"
    }
    
    stages {
        stage("Check CMD"){
            steps{
                bat "Hello World!"
            }
        }
    }
}