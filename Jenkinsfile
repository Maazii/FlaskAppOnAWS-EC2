pipeline {
    agent any
    
    stages {
        stage("Initialize Terraform"){
            steps{
                terraform init
            }
        }
        stage("Validate Configuration"){
            steps{
                terraform validate
            }
        }
    }
}