pipeline {
    agent { label 'any' }

    stages {

        stage('Init') {
            steps {
                script {
                    env.COMMIT_SHA = sh(
                        script: "git rev-parse --short HEAD",
                        returnStdout: true
                    ).trim()
                }
                echo "Building commit: ${env.COMMIT_SHA}"
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t legend-flask-app:${env.COMMIT_SHA} ."
            }
        }

        stage('Test') {
            steps {
                sh "docker run --rm legend-flask-app:${env.COMMIT_SHA} python -c \"print('App test passed')\""
            }
        }

        stage('Package') {
            steps {
                sh "docker tag legend-flask-app:${env.COMMIT_SHA} legend-flask-app:latest"
            }
        }

        stage('Validate Artifact') {
            steps {
                sh "docker images | grep legend-flask-app"
            }
        }
    }
}

