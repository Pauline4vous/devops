pipeline {
    agent any
    environment {
        HEROKU_APP_NAME = 'give-take'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pauline4vous/devops.git',
                    credentialsId: 'github-credentials'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t give-take:latest .'
            }
        }
        stage('Deploy to Heroku') {
            steps {
                withCredentials([string(credentialsId: 'HEROKU_API_KEY', variable: 'HEROKU_API_KEY')]) {
                    sh '''
                    heroku container:login
                    heroku container:push web --app ${HEROKU_APP_NAME}
                    heroku container:release web --app ${HEROKU_APP_NAME}
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment to Heroku successful!'
        }
        failure {
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}
