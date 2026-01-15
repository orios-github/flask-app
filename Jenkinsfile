pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def IMAGE_TAG = "v${env.BUILD_NUMBER}"
                    sh "docker build -t oscar8899/flask-app:${IMAGE_TAG} ."
                    sh "docker push oscar8899/flask-app:${IMAGE_TAG}"
                }
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
        stage('Update Manifest') {
            steps {
                script {
                    def IMAGE_TAG = "v${env.BUILD_NUMBER}"
                    sh """
                    sed -i 's|image: oscar8899/flask-app:.*|image: oscar8899/flask-app:${IMAGE_TAG}|g' k8s/k8s-deployment.yaml
                    git config --global user.email "jenkins@ci.local"
                    git config --global user.name "Jenkins CI"
                    git add k8s/k8s-deployment.yaml
                    git commit -m "Update image tag to ${IMAGE_TAG}"
                    git push origin main
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                sh '''
        	export KUBECONFIG=/var/lib/jenkins/.kube/config
        	kubectl apply -f k8s/deployment.yaml
        	'''

            }
        }
    }

}




