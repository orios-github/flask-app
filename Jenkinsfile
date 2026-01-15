pipeline {
    agent any

    environment {
        VERSION = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']], // or main
                          userRemoteConfigs: [[url: 'https://github.com/orios-github/flask-app.git',
                                               credentialsId: 'github-credential']]])
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t oscar8899/flask-app:${VERSION} ."
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'oscar8899-dockerHub',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) {
                    sh """
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push oscar8899/flask-app:${VERSION}
                      docker tag oscar8899/flask-app:${VERSION} oscar8899/flask-app:latest
                      docker push oscar8899/flask-app:latest
                    """
                }
            }
        }   
        stage('Update Manifest') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkins-push-token',
                                          usernameVariable: 'GIT_USER',
                                          passwordVariable: 'GIT_PASS')]) {
                    sh """
                      sed -i "s|image: oscar8899/flask-app:.*|image: oscar8899/flask-app:v${BUILD_NUMBER}|g" k8s/deployment.yaml
                      git config --global user.email "jenkins@ci.local"
                      git config --global user.name "Jenkins CI"
                      git checkout master
                      git add k8s/deployment.yaml
                      git commit -m "Update image tag to v${BUILD_NUMBER}" || echo "No changes"
                      git push https://${GIT_USER}:${GIT_PASS}@github.com/orios-github/flask-app.git master
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                sh """
                  export KUBECONFIG=/var/lib/jenkins/.kube/config
                  kubectl apply -f k8s/deployment.yaml
                """
            }
        }
    }
}




















