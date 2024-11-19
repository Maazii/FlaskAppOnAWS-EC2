pipeline {
    agent any
    
    stages {
        stage("Initialize Terraform"){
            steps {
                sh "terraform init"
            }
        }
        stage("Validate Configuration"){
            steps {
                sh "terraform validate"
            }
        }
    }
}