pipeline {
    agent any
    
    stages {
        stage("Checkout Terraform Code"){
            steps {
                git branch: 'main', changelog: false, credentialsId: 'Github-SSH-Private', poll: false, url: 'git@github.com:Maazii/FlaskAppOnAWS-EC2.git'
            }
        }
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