pipeline {
    agent any

    environment {
        GMAIL_USER = credentials('gmail-user')
    }


    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Postman Tests')
        {
            steps {
                sh '''
                    newman run Collections_Postman/collection_guico.json
                '''
            }
        }
    }

    post {
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
