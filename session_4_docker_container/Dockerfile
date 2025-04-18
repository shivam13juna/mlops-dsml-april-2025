#FROM python:3.10-alpine⁠
FROM python:3.8-slim-buster
# Here I'm using the python:3.10-alpine image as the base image
# This is a lightweight version of the Python image based on Alpine Linux

WORKDIR /flask-loan-app
# This will create a directory called flask-loan-app in the container

COPY artefacts/requirements.txt .
# This copies the requirements.txt file from the artefacts directory on your host machine to the current working directory in the container

RUN pip install -r requirements.txt
# This command installs the Python packages listed in requirements.txt

COPY . /flask-loan-app/
# This copies the entire contents of the current directory on your host machine to the /flask-loan-app directory in the container

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]

# RUn command only runs while creating the image, CMD command runs when the container is started. 

# Install Docker Desktop from https://docs.docker.com/desktop/setup/install/




#docker build -t mark1 .
#docker image ls
#docker run -p 8000:8000 mark1
#docker run -p 8000:8000 --name flask-loan-app-container mark1


#docker run -d -p 8000:8000 mark1
# -d flag is for detached mode, which runs the container in the background

#docker container run -it -p 8000:8000 mark2 bash
# -it flag is for interactive mode, which allows you to interact with the container's shell

# first 8000 is the port on the host machine (my local) and the second 8000 is the port on the container

#docker container ls --all

# this will tell us the container id, which we can use to stop the container

#swarms

#docker image tag mark2:latest shivam13juna/example2-docker:latest