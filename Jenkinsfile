pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // This ensures Jenkins is on a branch, not detached HEAD
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],   // or your branch name
                          userRemoteConfigs: [[url: 'git@github.com:orios-github/flask-app.git']]
                         ])
            }
        }       
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
                    sed -i 's|image: oscar8899/flask-app:.*|image: oscar8899/flask-app:${IMAGE_TAG}|g' k8s/deployment.yaml
                    git config --global user.email "jenkins@ci.local"
                    git config --global user.name "Jenkins CI"
                    git add k8s/deployment.yaml
                    git commit -m "Update image tag to ${IMAGE_TAG}"
                    git push origin main
                    """
                }
            }
            steps {
                sh '''
                  sed -i "s|image: oscar8899/flask-app:.*|image: oscar8899/flask-app:${VERSION}|g" k8s/deployment.yaml
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








