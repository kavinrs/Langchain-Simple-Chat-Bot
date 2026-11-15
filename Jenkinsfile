pipeline{
  agent any
  triggers{
    pollSCM('* * * * *')
  }
  stages{
    stage("dev"){
      steps{
      echo "This is a dev environment"
      }
    }
    stage("stage"){
      steps{
        echo "This is a stage environment"
      }
    }
  }
    
}
