pipeline {
    agent any
    stages {
        stage('Run Postman Tests') {
            steps {
                sh '''
                    newman run Collections_Postman/collection_guico.json \
                        --reporters cli,htmlextra \
                        --reporter-htmlextra-export report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
        success {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                sh '/usr/local/bin/email.sh sucesso "$BUILD_URL" "$DESTINATARIO"'
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                sh '/usr/local/bin/email.sh falha "$BUILD_URL" "$DESTINATARIO"'
            }
        }
    }
}
