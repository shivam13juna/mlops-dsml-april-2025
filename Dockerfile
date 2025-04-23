FROM python:3.10-slim


#FROM python:3.10-alpine
# this didn't work, I got errors like 
#10.90       The following exception(s) were encountered:
#10.90       Running `cc --version` gave "[Errno 2] No such file or directory: 'cc'"
#10.90       Running `gcc --version` gave "[Errno 2] No such file or directory: 'gcc'"
#10.90       Running `clang --version` gave "[Errno 2] No such file or directory: 'clang'"
#10.90       Running `nvc --version` gave "[Errno 2] No such file or directory: 'nvc'"
#10.90       Running `pgcc --version` gave "[Errno 2] No such file or directory: 'pgcc'"
#10.90       Running `icc --version` gave "[Errno 2] No such file or directory: 'icc'"
#10.90       Running `icx --version` gave "[Errno 2] No such file or directory: 'icx'"
# cc is the C compiler, gcc is the GNU C compiler, clang is a C/C++/Objective-C compiler, nvc is the NVIDIA HPC SDK compiler, pgcc is the Portland Group C compiler, icc is the Intel C compiler, and icx is the Intel C++ compiler. We need all this, as they are required to compile the C extensions for some of the Python packages we are using in our project.


#⁠# FROM python:3.8-slim-buster
# Here I'm using the python:3.10-alpine image as the base image


WORKDIR /flask-loan-app
# This will create a directory called flask-loan-app in the container

COPY session_6_CI/requirements.txt .
# This copies the requirements.txt file from the artefacts directory on your host machine to the current working directory in the container

RUN pip install -r requirements.txt
# This command installs the Python packages listed in requirements.txt

COPY session_6_CI/ /flask-loan-app/
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