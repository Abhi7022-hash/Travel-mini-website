pipeline {
    agent any
 
    environment {
        DOCKER_USER  = "abhishek661"
        DOCKER_CREDS = "dockerhub-cred"
    }

    stages {

        stage("Checkout Code") {
            steps {
                git branch: "main",
                    url: "https://github.com/Abhi7022-hash/Travel-mini-website.git"
            }
        }

        stage("Build Docker Images") {
            steps {
                sh """
                docker build -t $DOCKER_USER/frontend-service:latest frontend-service
                docker build -t $DOCKER_USER/user-service:latest user-service
                docker build -t $DOCKER_USER/booking-service:latest booking-service
                """
            }
        }

        stage("Docker Login") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKER_CREDS,
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh """
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    """
                }
            }
        }

        stage("Push Images to DockerHub") {
            steps {
                sh """
                docker push $DOCKER_USER/frontend-service:latest
                docker push $DOCKER_USER/user-service:latest
                docker push $DOCKER_USER/booking-service:latest
                """
            }
        }

        stage("Check Kubernetes Access") {
            steps {
                sh """
                kubectl get nodes
                """
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                sh """
                kubectl apply -f frontend-service/k8s/
                kubectl apply -f user-service/k8s/
                kubectl apply -f booking-service/k8s/
                """
            }
        }

        stage("Restart Deployments") {
            steps {
                sh """
                kubectl rollout restart deployment f-deploy
                kubectl rollout restart deployment user-deployment
                kubectl rollout restart deployment booking-deployment
                """
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline executed successfully."
        }
        failure {
            echo "Pipeline failed. Check Jenkins logs."
        }
    }
}
















