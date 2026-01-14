pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t <tu-dockerhub-usuario>/flask-app:latest .'
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push <tu-dockerhub-usuario>/flask-app:latest'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
}