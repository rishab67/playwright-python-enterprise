pipeline {
    // 1. THE ENVIRONMENT: Tell Jenkins to run this on any available node
    agent any

    // 2. THE VAULT: Pulling credentials securely from Jenkins Credentials Manager
    environment {
        API_BASE_URL = credentials('API_BASE_URL')
        UI_BASE_URL = credentials('UI_BASE_URL')
        ADMIN_USERNAME = credentials('ADMIN_USERNAME')
        ADMIN_PASSWORD = credentials('ADMIN_PASSWORD')
    }

    stages {
        stage('📥 Download Codebase') {
            steps {
                checkout scm
            }
        }

        stage('🐍 Setup Python & Dependencies') {
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

        stage('🚀 Execute Parallel Test Engine') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest tests/ -n auto --html=report.html --self-contained-html
                '''
            }
        }
    }

    // 3. ARTIFACTS: Generate the Dashboard even if tests fail
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}