stage("deploy & OWASP Dependency-Check") {
    agent any
    steps {
        dependencyCheck additionalArguments: '''
        -o './'
        -s './'
        -f 'ALL'
        --prettyPrint''', odcInstallation: 'owasp-dependency'
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    }
}

pipeline {
    agent none
    tools {
        maven 'Maven'
    }
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
                        -Dsonar.host.url=http://192.168.175.125:9000 \
                        -Dsonar.login=sqp_3654775126359d1e01912c54d56279e2da33111c
                    """
                }
            }
        }
    }
}
