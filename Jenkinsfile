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
                    docker build -t vatsalsolanki19/flask-app:latest .
                '''
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push vatsalsolanki19/flask-app:latest'
            }
        }
        stage('deploy'){
            steps{
                sh'''
                    docker run -d --name flask-app --network two-tier-network -p 5000:5000 vatsalsolanki19/flask-app:latest
                '''
            }
        }
    }
    
}