pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t oscar8899/flask-app:latest .'
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'oscar8899-dockerHub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push oscar8899/flask-app:latest'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh '''
        	export KUBECONFIG=/var/lib/jenkins/.kube/config
        	kubectl apply -f k8s-deployment.yaml
        	'''

            }
        }
    }

}
