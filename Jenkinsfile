pipeline {
  agent none
  tools {
    maven 'Maven'
  }
  stages {
    stage("Build & Analyse avec SonarQube") {
      agent any
      steps {
        script {
          sh 'mvn clean package sonar:sonar'
        }
      }
    }
  }
}
node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def mvn = tool 'Default Maven';
    withSonarQubeEnv() {
      sh "${mvn}/bin/mvn clean verify sonar:sonar -Dsonar.projectKey=Ta-m-re-la-reine-des-putes -Dsonar.projectName='Ta mère la reine des putes'"
    }
  }
