pipeline {
    agent any

    environment {
        API_BASE_URL = credentials('API_BASE_URL')
        UI_BASE_URL = credentials('UI_BASE_URL')
        ADMIN_USERNAME = credentials('ADMIN_USERNAME')
        ADMIN_PASSWORD = credentials('ADMIN_PASSWORD')
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
                    python -m venv venv
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