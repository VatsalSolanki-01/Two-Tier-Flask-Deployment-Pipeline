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
        stage('deploy'){
            steps{
                sh'''
                    docker run -p 5000:5000 flask-app 
                '''
            }
        }
    }
    
}