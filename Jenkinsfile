pipeline {
  agent none
  tools {
    maven 'Maven'
  }
  stages {
    stage('SCM') {
      checkout scm
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
          steps {
              script {
                  // Run SonarQube analysis
                  sh """
                      mvn sonar:sonar \
                      -Dsonar.projectKey=your-project-key \
                      -Dsonar.host.url=http://localhost:9000/ \
                      -Dsonar.login=sqp_3654775126359d1e01912c54d56279e2da33111c
                  """
              }
          }
      }
  }
}
