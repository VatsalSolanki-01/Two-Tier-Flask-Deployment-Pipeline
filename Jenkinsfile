pipeline{
    agent any
    
    stages{
        stage('Clone repo'){
            steps{
                git branch: 'main', url: 'https://github.com/VatsalSolanki-01/Two-Tier-Flask-Deployment-Pipeline.git'
            }
        }
        stage('Image build'){
            steps{
                sh '''
                    docker build -t flask-app .
                '''
            }
        }
    }
    
}