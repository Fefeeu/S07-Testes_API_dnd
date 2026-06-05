pipeline {
    agent any
    stages {
        stage('Run Postman Tests') {
            steps {
                sh '''
                    newman run /newman/collection_tests.json \
                        --reporters cli,html \
                        --reporter-html-export /relatorios/report_$(date +%Y-%m-%d_%H-%M-%S).html
                '''
            }
        }
        stage('Salvar Log no Banco') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh '''
                    cd /data
                    pip install -r requirements.txt --break-system-packages -q
                    python3 db_manager.py
                '''
            }
        }
    }
    post {
        success {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                script {
                    def buildUrl = env.BUILD_URL ?: 'N/A'
                    def dest = DESTINATARIO
                    sh "/usr/local/bin/email.sh sucesso '${buildUrl}' '${dest}'"
                }
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                script {
                    def buildUrl = env.BUILD_URL ?: 'N/A'
                    def dest = DESTINATARIO
                    sh "/usr/local/bin/email.sh falha '${buildUrl}' '${dest}'"
                }
            }
        }
    }
}
