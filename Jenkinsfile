pipeline {
    agent any

    environment {
        API_BASE_URL = 'https://restful-booker.herokuapp.com'
        UI_BASE_URL = 'https://www.amazon.in'
        ADMIN_USERNAME = 'admin'
        ADMIN_PASSWORD = 'password123'
    }

    stages {
        stage('Download Codebase') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python and Dependencies') {
            steps {
                bat '''
                    "C:\\Users\\india\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install chromium
                '''
            }
        }

        stage('Execute Parallel Test Engine') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest tests/ -n auto --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}