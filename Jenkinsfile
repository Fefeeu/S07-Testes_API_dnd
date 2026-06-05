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
                script {
                    def url = env.BUILD_URL ?: 'N/A'
                    sh "/usr/local/bin/email.sh sucesso '${url}' '${DESTINATARIO}'"
                }
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                script {
                    def url = env.BUILD_URL ?: 'N/A'
                    sh "/usr/local/bin/email.sh falha '${url}' '${DESTINATARIO}'"
                }
            }
        }
    }
}
