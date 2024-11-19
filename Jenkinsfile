pipeline {
    agent any

    // environment {
    //     TF_VAR_REGION = "us-east-1"
    //     PATH = "C:\\Users\\hp\\AppData\\Local\\Temp\\jenkins12441364719468129590.bat"
    // }
    
    stages {
        stage("Check Terraform Version"){
            steps{
                bat "terraform version"
            }
        }
    }
}