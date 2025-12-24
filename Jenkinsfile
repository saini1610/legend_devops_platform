pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
                sh 'docker build -t legend-flask-app:ci .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic test'
                sh 'docker run --rm legend-flask-app:ci python -c "print(\'App test passed\')"'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging Docker image'
                sh 'docker tag legend-flask-app:ci legend-flask-app:latest'
            }
        }

        stage('Validate Artifact') {
            steps {
                echo 'Validating built artifact'
                sh 'docker images | grep legend-flask-app'
            }
        }
    }
}

