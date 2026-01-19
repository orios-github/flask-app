pipeline {
    agent any               // Run the pipeline on any available Jenkins agent

    environment {
        VERSION = "v${BUILD_NUMBER}"             // Define an environment variable VERSION using Jenkins build number
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],         // Checkout the master branch (or main if renamed)
                          userRemoteConfigs: [[url: 'https://github.com/orios-github/flask-app.git',
                                               credentialsId: 'jenkins-push-token']]])     // Use stored GitHub credentials
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t oscar8899/flask-app:${VERSION} ."         // Build Docker image tagged with the current VERSION (e.g., v12)
            }
        }

        stage('Push') {
            withCredentials([usernamePassword(credentialsId: 'oscar8899-dockerHub',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) 
                {
                    sh """
                      echo $PASS | docker login -u $USER --password-stdin          
                      docker push oscar8899/flask-app:${VERSION}                   
                      docker tag oscar8899/flask-app:${VERSION} oscar8899/flask-app:latest   
                      docker push oscar8899/flask-app:latest                       
                    """
                    // Authenticate to DockerHub securely
                    // Push versioned image to DockerHub
                    // Tag image as 'latest'
                    // Push 'latest' tag to DockerHub
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
                      git checkout -B master origin/master                   
                      git add k8s/deployment.yaml                            
                      git commit -m "Update image tag to v${BUILD_NUMBER}" || echo "No changes"  
                      git pull --rebase https://${GIT_USER}:${GIT_PASS}@github.com/orios-github/flask-app.git master     
                      git push https://${GIT_USER}:${GIT_PASS}@github.com/orios-github/flask-app.git master     
                    """
                    // Update Kubernetes deployment.yaml with the new image version
                    // Configure Git user email
                    // Configure Git username
                    // Ensure working on master branch
                    // Stage updated manifest file
                    // Commit changes (skip if no diff)
                    // Rebase with remote master to avoid conflicts
                    // Push updated manifest back to GitHub
                }
            }
        }

        stage('Deploy') {
            steps {
                sh """
                  export KUBECONFIG=/var/lib/jenkins/.kube/config         
                  kubectl apply -f k8s/deployment.yaml                    
                """
                // Point kubectl to Jenkins' kubeconfig
                // Apply updated manifest to Kubernetes cluster
            }
        }
    }
}
