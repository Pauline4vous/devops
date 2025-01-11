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
                bat '''
                C:/Users/Envy/AppData/Local/Programs/Python/Python313/python.exe -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test Docker Access') {
            steps {
                bat 'docker version'
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest tests/
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t give-take:latest .'
            }
        }
        stage('Deploy to Heroku') {
            steps {
                withCredentials([string(credentialsId: 'HEROKU_API_KEY', variable: 'HEROKU_API_KEY')]) {
                    bat '''
                    heroku container:login
                    heroku container:push web --app %HEROKU_APP_NAME%
                    heroku container:release web --app %HEROKU_APP_NAME%
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
    
