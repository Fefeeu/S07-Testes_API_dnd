pipeline {
    agent any

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
                    for collection in $(find Collections_Postman -name "*.json"); do
                        echo "Rodando: $collection"
                        newman run "$collection"
                    done
                '''
            }
        }
    }

    post {
        success {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                sh "/usr/local/bin/email.sh sucesso ${BUILD_URL} ${DESTINATARIO}"
            }
        }
        failure {
            withCredentials([string(credentialsId: 'email-destinatario', variable: 'DESTINATARIO')]) {
                sh "/usr/local/bin/email.sh falha ${BUILD_URL} ${DESTINATARIO}"
            }
        }
    }
}
