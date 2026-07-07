pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop python-demo || true
                docker rm python-demo || true
                docker run -d --name python-demo -p 5000:5000 python-demo
                '''
            }
        }

    }
}
