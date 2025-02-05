pipeline {
    agent none
    tools {
        maven 'Maven'
    }
    stages {
	   stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/nekarir/Jeu.git' 
            }

        stage('Test SonarQube Connection') {
            steps {
                script {
                    sh 'ping -c 4 sonarqube'  
                    sh 'curl -v http://AdressIP:Port'
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
	   stage('SonarQube Analysis') {
            environment {
                SONAR_HOST_URL = 'http://AdressIP:Port/' 
                SONAR_AUTH_TOKEN = credentials('sonarqube') 
            }
            steps {
                sh 'mvn sonar:sonar -Dsonar.projectKey=sample_project -Dsonar.host.url=$SONAR_HOST_URL -Dsonar.token=$SONAR_AUTH_TOKEN'
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
