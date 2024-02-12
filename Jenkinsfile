// pipeline {
//     agent any

//     environment {
//         CONTAINER_NAME = 'cwpp_container'
//         IMAGE_NAME = 'cwpp'
//         PORT_MAPPING = '8000:8000'
//         GITHUB_REPO_URL = 'https://github.com/shreyasdeodhare/byteBardBazaar.git'
//     }

//     stages {
//         stage('Checkout Source Code') {
//             steps {
//                 script {
//                     try {
//                         // Clone or pull the repository to get the latest changes
//                         git branch: 'master', url: "${GITHUB_REPO_URL}"
//                     } catch (Exception checkoutError) {
//                         error("Failed to checkout source code: ${checkoutError.message}")
//                     }
//                 }
//             }
//         }

//         stage('Build or Pull Docker Image') {
//             steps {
//                 script {
//                     try {
//                         def imageExists = bat(script: "docker images ${IMAGE_NAME} | findstr ${IMAGE_NAME}", returnStatus: true) == 0

//                         if (imageExists) {
//                             echo "Using existing Docker image."
//                         } else {
//                             // Build the Docker image if it doesn't exist
//                             bat "docker build -t ${IMAGE_NAME} ."
//                         }
//                     } catch (Exception buildError) {
//                         error("Failed to build or pull Docker image: ${buildError.message}")
//                     }
//                 }
//             }
//         }

//         stage('Run Docker Container') {
//             steps {
//                 script {
//                     try {
//                         // Run the Docker container or start it if it already exists
//                         bat "docker run -p ${PORT_MAPPING} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
//                     } catch (Exception runError) {
//                         error("Failed to run Docker container: ${runError.message}")
//                     }
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             script {
//                 try {
//                     // Stop and remove the Docker container
//                     bat "docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}"
//                 } catch (Exception cleanupError) {
//                     echo "Failed to stop and remove the Docker container: ${cleanupError.message}"
//                 }
//             }
//         }
//     }
// }


// pipeline {
//     agent any

//     environment {
//         // Your existing environment variables
//         CONTAINER_NAME = 'cwpp_container'
//         IMAGE_NAME = 'cwpp'
//         PORT_MAPPING = '8000:8000'
//         GITHUB_REPO_URL = 'https://github.com/shreyasdeodhare/byteBardBazaar.git'
//     }

//     stages {
//         stage('Checkout Source Code') {
//             steps {
//                 script {
//                     try {
//                         // Clone or pull the repository to get the latest changes
//                         git branch: 'master', url: "${GITHUB_REPO_URL}"
//                     } catch (Exception checkoutError) {
//                         error("Failed to checkout source code: ${checkoutError.message}")
//                     }
//                 }
//             }
//         }

//         stage('Build or Pull Docker Image') {
//             steps {
//                 script {
//                     try {
//                         def imageExists = bat(script: "docker images ${IMAGE_NAME} | findstr ${IMAGE_NAME}", returnStatus: true) == 0

//                         if (imageExists) {
//                             echo "Using existing Docker image."
//                         } else {
//                             // Build the Docker image if it doesn't exist
//                             bat "docker build -t ${IMAGE_NAME} ."
//                         }
//                     } catch (Exception buildError) {
//                         error("Failed to build or pull Docker image: ${buildError.message}")
//                     }
//                 }
//             }
//         }

//         stage('Run Docker Container') {
//             steps {
//                 script {
//                     try {
//                         // Run the Docker container or start it if it already exists
//                         bat "docker run -p ${PORT_MAPPING} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
//                     } catch (Exception runError) {
//                         error("Failed to run Docker container: ${runError.message}")
//                     }
//                 }
//             }
//         }

//         stage('SonarQube Analysis') {
//     steps {
//         script {
           
               
//             //   bat "sonar-scanner -Dsonar.projectKey=squ_db3d351da06648c35a9829eb0fa125405a73531c -Dsonar.sources=. -Dsonar.login=admin -Dsonar.password=shreyas"
//                           bat "sonar-scanner -Dsonar.projectKey=squ_f42dcb9d6c7a053903d0d65abaf756fec86546d1 -Dsonar.sources=. -Dsonar.login=admin -Dsonar.password=shreyas"

//         }
//     }
// }
//     }

//     post {
//         always {
//             script {
//                 try {
//                     // Stop and remove the Docker container
//                     bat "docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}"
//                 } catch (Exception cleanupError) {
//                     echo "Failed to stop and remove the Docker container: ${cleanupError.message}"
//                 }
//             }
//         }
//     }
// }


pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'cwpp_container'
        IMAGE_NAME = 'cwpp'
        PORT_MAPPING = '8000:8000'
        GITHUB_REPO_URL = 'https://github.com/shreyasdeodhare/byteBardBazaar.git'
        DOCKERHUB_REPO = 'ssddev007/bytebardbazar'
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                script {
                    try {
                        git branch: 'master', url: "${GITHUB_REPO_URL}"
                    } catch (Exception checkoutError) {
                        error("Failed to checkout source code: ${checkoutError.message}")
                    }
                }
            }
        }

        stage('Build or Pull Docker Image') {
            steps {
                script {
                    try {
                        def imageExists = bat(script: "docker images ${IMAGE_NAME} | findstr ${IMAGE_NAME}", returnStatus: true) == 0

                        if (imageExists) {
                            echo "Using existing Docker image."
                        } else {
                            bat "docker build -t ${IMAGE_NAME} ."
                        }
                    } catch (Exception buildError) {
                        error("Failed to build or pull Docker image: ${buildError.message}")
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    try {
                        bat "docker run -p ${PORT_MAPPING} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                    } catch (Exception runError) {
                        error("Failed to run Docker container: ${runError.message}")
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    try {
                        // Login to Docker Hub
                        bat "docker login -u shreyasdeodhare18@gmail.com -p Shreyas189"

                        // Tag the Docker image for Docker Hub repository
                        bat "docker tag ${IMAGE_NAME} ${DOCKERHUB_REPO}:${BUILD_NUMBER}"

                        // Push the Docker image to Docker Hub
                        bat "docker push ${DOCKERHUB_REPO}:${BUILD_NUMBER}"
                    } catch (Exception pushError) {
                        error("Failed to push Docker image to Docker Hub: ${pushError.message}")
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    bat "sonar-scanner -Dsonar.projectKey=squ_614561c007f3f673857dc1d145caea64c5c5384c -Dsonar.sources=. -Dsonar.login=admin -Dsonar.password=shreyas"
                }
            }
        }
    }

    post {
        always {
            script {
                try {
                    bat "docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}"
                } catch (Exception cleanupError) {
                    echo "Failed to stop and remove the Docker container: ${cleanupError.message}"
                }
            }
        }
    }
}
