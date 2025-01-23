pipeline {
    agent none
    tools {
        maven 'Maven'
    }
    stages {
        stage('Test SonarQube Connection') {
            steps {
                script {
                    // Test de la connectivité
                    sh 'ping -c 4 sonarqube'  // Essayez de pinger sonarqube si c'est un nom de service
                    // ou
                    sh 'curl -v http://sonarqube:9000'  // Essayez de vous connecter à SonarQube
                }
            }
        }
        stage('SCM') {
            steps {
                checkout scm
            }
        }
        stage("Build & Analyse avec SonarQube") {
            agent any
            steps {
                script {
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }
        stage("deploy & OWASP Dependency-Check") {
            agent any
            steps {
                dependencyCheck additionalArguments: '''
                -o './'
                -s './'
                -f 'ALL'
                --prettyPrint
                --purge''', odcInstallation: 'owasp-dependency'
                dependencyCheckPublisher pattern: 'dependency-check-report.xml'
            }
        }
    }
}
