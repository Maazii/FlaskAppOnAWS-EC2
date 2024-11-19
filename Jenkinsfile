pipeline {
    agent any

    // environment {
    //     TF_VAR_REGION = "us-east-1"
    //     PATH = "C:\\terraform\\terraform.exe"
    // }
    
    stages {
        stage("Call Batch Shell"){
            steps{
                cmd /c call C:\Users\hp\AppData\Local\Temp\jenkins12441364719468129590.bat
            }
        }
        stage("Check Terraform Version"){
            steps{
                bat "terraform version"
            }
        }
    }
}