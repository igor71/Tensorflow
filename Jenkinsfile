pipeline {
  agent {label 'yi-tensorflow'}
    stages {
        stage('Build Basic DEVEL-CPU-MKL Image') {
            steps {
              sh 'docker build --no-cache -f Dockerfile.devel-cpu-mkl -t yi/tflow:0.0 .'
            }
        }
		stage('Test $image_id Docker Image') { 
            steps {
                sh '''#!/bin/bash -xe
				    echo 'Hello, YI-TFLOW!!'
                    image_id="$(docker images -q yi/tflow:0.0)"
                    if [[ "$(docker images -q yi/tflow:0.0 2> /dev/null)" == "$image_id" ]]; then
                       docker inspect --format='{{range $p, $conf := .Config.ExposedPorts}} {{$p}} {{end}}' $image_id
                    else
                       echo "SSH port not listenning inside docker container, check the Dockerfile.SSH file!!!"
                       exit 0
                    fi 
                   ''' 
            }
        }
        stage('Build The Image & Install TENSORFLOW-CPU-MKL Package ') {
            steps {
                sh 'docker build --no-cache -f Dockerfile.cpu-mkl -t yi/tflow:0.1 .'
            }
        }
		stage('Test $image_id Docker Image') { 
            steps {
                sh '''#!/bin/bash -xe
				    echo 'Hello, Jenkins_Docker'
                    image_id="$(docker images -q yi/tflow:0.0:0.1)"
                    if [[ "$(docker images -q yi/tflow:0.0:0.1 2> /dev/null)" == "$image_id" ]]; then
                       docker inspect --format='{{range $p, $conf := .Config.ExposedPorts}} {{$p}} {{end}}' $image_id
                    else
                       echo "TomCat port not listenning inside docker container, check the Dockerfile file!!!"
                       exit 0
                    fi 
                   ''' 
		    }
		}
    }
	post {
            always {
               script {
                  if (currentBuild.result == null) {
                     currentBuild.result = 'SUCCESS' 
                  }
               }
               step([$class: 'Mailer',
                     notifyEveryUnstableBuild: true,
                     recipients: "igor.rabkin@xiaoyi.com",
                     sendToIndividuals: true])
            }
         } 
}
