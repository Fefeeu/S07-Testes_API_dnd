pipeline {
    agent any
    stages {
        stage('Run Postman Tests') {
            steps {
                // Gera o relatório HTML em vez de só rodar os testes
                sh '''
                    newman run Collections_Postman/collection_guico.json \
                        --reporters cli,htmlextra \
                        --reporter-htmlextra-export /relatorios/report.html
                '''
            }
        }
    }
    post {
        always {
            // Arquiva o relatório como artefato do build no Jenkins
            archiveArtifacts artifacts: '/relatorios/report.html', allowEmptyArchive: true
        }
        success {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                script {
                    def buildUrl = env.BUILD_URL ?: 'N/A'
                    sh "/usr/local/bin/email.sh sucesso '${buildUrl}' '${DESTINATARIO}'"
                }
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                script {
                    def buildUrl = env.BUILD_URL ?: 'N/A'
                    sh "/usr/local/bin/email.sh falha '${buildUrl}' '${DESTINATARIO}'"
                }
            }
        }
    }
}
