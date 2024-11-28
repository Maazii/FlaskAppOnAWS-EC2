pipeline {
    agent any
    
    stages {
        stage("Check Terraform Version"){
            steps{
                bat "terraform version"
            }
        }
        stage("Terraform Validate"){
            steps{
                bat "terraform validate"
            }
        }
        stage("Terraform Plan"){
            steps{
                bat "terraform plan"
            }
        }
    }
}
