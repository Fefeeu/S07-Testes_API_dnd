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
                sh '''
                    newman run Collections_Postman/collection_guico.json
                '''
            }
        }
    }
}
