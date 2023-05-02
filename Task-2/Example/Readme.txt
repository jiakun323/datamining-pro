1. Develop the data mining pipeline for sentiment analysis and dump/save the pipeline to be delivered as in "\docker_demo\app\model\sentiment_model_dev.py"
	Note: Record and submit your 10-fold CV performance (F1 score) on the training data 【Required deliverables】, and you may test the saved pipeline as in "\docker_demo\app\model\sentiment_model_test.py"
	
2. Load the pipeline and deploy it as an API service 
	Note: You may test it in your local environment as below
	Step-0: make sure current directory is under the folder "docker_demo" on your laptop
	Step-1: install python (3.9 or higher) and required packages as specified in "docker_demo/requirements.txt" 
	Step-3: enter the path of "\docker_demo\app"
	Step-4: run "python main.py"

3. Build the docker image of your pipeline and the environment
	Step-0: make sure the current path is located in the folder of "docker_demo"
	Step-1： Build the docker via "docker build -t mds5724python -f Dockerfile_python ." [Note that the command ends with the dot "."]
	Step-2(for test only, please refer to the lecture notes of week11): run and test the docker with command "$ docker run -d -p 9000:5724 --memory=512m [IMAGE ID]"

4. Publish/push the docker image to a PUBLIC repository of your own account in Alibaba Cloud Container Registry
	Note: Record and submit the URL of your docker image 【Required deliverables】, and you may also run the code  Please refer to the lecture notes of week11 




