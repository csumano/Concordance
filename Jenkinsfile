
pipeline {
    agent any

    triggers {
        
        pollSCM 'H/2 * * * *'
    }
    
    stages {
        // stage('SonarQube'){
        //     environment{
        //         SCANNER_HOME = tool 'sonar_scanner'
                
        //     }
        //     steps{
        //         withSonarQubeEnv('SonarQube'){
                    
        //             sh '$SCANNER_HOME/bin/sonar-scanner -X'
        //         }
        //     }
        // }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3.7 -m pytest --junitxml=test_reports.xml'
            }
        }
 
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            junit '*.xml'
        }
    }
}
