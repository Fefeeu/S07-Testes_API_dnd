pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Postman Tests') {
            steps {
                sh 'newman run Collections_Postman/collection_guico.json'
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
