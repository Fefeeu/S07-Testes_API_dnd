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
                sh '''
                    URL="${BUILD_URL:-http://localhost:8080}"
                    export WORKSPACE="$WORKSPACE"
                    /usr/local/bin/email.sh sucesso "$URL" "$DESTINATARIO"
                '''
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                sh '''
                    URL="${BUILD_URL:-http://localhost:8080}"
                    /usr/local/bin/email.sh falha "$URL" "$DESTINATARIO"
                '''
            }
        }
    }
}
