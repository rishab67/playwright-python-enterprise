pipeline {
    agent any

    environment {
        API_BASE_URL = 'https://dummy-api.com'
        UI_BASE_URL = 'https://dummy-ui.com'
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
                    "C:\\Users\\india\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv
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
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}