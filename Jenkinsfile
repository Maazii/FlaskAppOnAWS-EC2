pipeline {
    agent any

    // environment {
    //     TF_VAR_REGION = "us-east-1"
    //     PATH = "C:\\Users\\hp\\AppData\\Local\\Temp\\jenkins12441364719468129590.bat"
    // }
    
    stages {
        stage("Check Terraform Code"){
            steps{
                git branch: "main", changelog: false, credentialsId: "Github-SSH-Private", poll: false, url: "git@github.com:Maazii/FlaskAppOnAWS-EC2.git"
            }
        }
        stage("Check Terraform Version"){
            steps{
                bat "terraform version"
            }
        }
        stage("Terraform Initialize"){
            steps{
                bat "terraform init"
            }
        }
        stage("Terraform Validate"){
            steps{
                bat "terraform validate"
            }
        }
        // stage("Terraform Plan"){
        //     steps{
        //         bat "terraform plan"
        //     }
        // }
    }
}