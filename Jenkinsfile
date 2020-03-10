    pipeline {	
    agent { label 'master' }	
    options {	
        buildDiscarder(logRotator(numToKeepStr: '5'))	
    }		
    stages {
        stage('sonarqube') {
            environment {
                scannerHome = tool 'SonarQube'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }
        stage('Build Flaskapps') {	
        steps {	
            script {
                if (env.BRANCH_NAME == 'master'){
                    sh 'docker build -t gcr.io/wlb-dev/flaskapp:0.2.$BUILD_NUMBER-dev .'
                }
                else if (env.BRANCH_NAME == 'development'){
                    sh 'docker build -t gcr.io/wlb-dev/flaskapp:0.2.$BUILD_NUMBER-dev .'
                }
                else {
                    sh 'docker build -t gcr.io/wlb-dev/flaskapp:0.1.$BUILD_NUMBER-PR .'
                }
            }		        	
        }	
        }	
        stage('Publish Flaskapps') {	
            steps {
            script {
                if (env.BRANCH_NAME == 'master'){
                    sh 'docker push gcr.io/wlb-dev/flaskapp:0.2.$BUILD_NUMBER-dev'
                }
                else if (env.BRANCH_NAME == 'development'){
                    sh 'docker push gcr.io/wlb-dev/flaskapp:0.2.$BUILD_NUMBER-dev'
                }
            }		
        }	      
        }
    }
        
        post {
            success {
                mattermostSend channel: '#testing-integration',
                color: 'good',
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
            }
            failure {
                mattermostSend channel: '#testing-integration',
                color: 'bad',
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
            }
        }	
        post {
            success {
                slackSend channel: '#taufik-devops',
                color: 'good',
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
        }
            failure {
                slackSend channel: '#taufik-devops',
                color: 'bad',
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
        }
    }	
    }
