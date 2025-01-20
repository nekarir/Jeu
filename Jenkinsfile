pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                echo 'Building the application'
                // Ajouter des commandes de build ici, par exemple:
                // sh 'mvn clean install'
            }
        }
        stage("test") {
            steps {
                echo 'Testing the application'
                // Ajouter des commandes de test ici, par exemple:
                // sh 'mvn test'
            }
        }
        stage("deploy") {
            steps {
                echo 'Deploying the application'
                // Ajouter des commandes de déploiement ici, par exemple:
                // sh 'scp target/app.war user@server:/path/to/deploy'
            }
        }
    }
}
