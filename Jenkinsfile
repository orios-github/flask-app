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
                sh '''
                  sed -i "s|image: oscar8899/flask-app:.*|image: oscar8899/flask-app:${VERSION}|g" /var/lib/jenkins/workspace/fask-app-pipeline/k8s/deployment.yaml
                  git config --global user.email "jenkins@ci.local"
                  git config --global user.name "Jenkins CI"
                  git add k8s/deployment.yaml || true
                  git commit -m "Update image tag to ${VERSION}" || echo "No changes to commit"
                  git push origin HEAD:master || echo "Skipping push (detached HEAD)"
                '''
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

















