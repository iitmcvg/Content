# README

## Running the container

Run,

```
docker run -it --name cvi --rm -p 8888:8888 iitmcvg/session:intro_CV bash
```

To update the container image, run:
```
docker pull iitmcvg/session:intro_CV
```

To update the repo, run:
```
cd .. & cd ..
git pull
cd Sessions/CV_Intro_Session_1_2018/
```

The image has the following tools:

* OpenCV 3.4.1
* Tensorflow 1.10
* Keras
* Jupyter
* Scientific python: Numpy, Scipy, Matplotlib ... etc.

## Getting Started with Docker 

Firstly, download a compatible version of docker from here:

* For installation of Docker in Windows - https://download.docker.com/win/stable/DockerToolbox.exe  
* For installation of Docker in Linux(Ubuntu) - https://docs.docker.com/install/linux/docker-ce/ubuntu/   
* For installation of Docker in Mac -   
https://download.docker.com/mac/stable/DockerToolbox.pkg  


### Part-1 

* The installer adds Docker Toolbox, VirtualBox, and Kinematic to your Applications folder.   
* On your Desktop, find the Docker QuickStart Terminal icon.  
* Click the Docker QuickStart icon to launch a pre-configured Docker Toolbox terminal.    
* If the system displays a User Account Control prompt to allow VirtualBox to make changes to your computer. Choose Yes.  
* The terminal does several things to set up Docker Toolbox for you. When it is done, the terminal displays the $ prompt.  

* Make the terminal active by clicking your mouse next to the $ prompt.
* The prompt is traditionally a $ dollar sign. You type commands into the command line which is the area after the prompt. Your cursor is indicated by a highlighted area or a | that appears in the command line. After typing a command, always press RETURN.


* Type the docker run hello-world command and press RETURN.
* The command does some work for you, if everything runs well, the command’s output looks like this:

```
$ docker run hello-world
 Unable to find image 'hello-world:latest' locally
 Pulling repository hello-world
 91c95931e552: Download complete
… … … …
```
 To try something more ambitious, you can run an Ubuntu container with:
` docker run -it ubuntu bash`

 For more examples and ideas, visit: https://docs.docker.com/userguide/

### Part-2

* Run the command docker-machine ip and make a note of the IP address shown as output.

* Type the docker run -p 8888:8888 siva1911/session command and press RETURN.

* The command does some work for you, downloading takes around 5 minutes with good internet connectivity. Be patient and if everything runs well, the command’s output looks like this:

* Copy/paste this URL into your browser when you connect for the first time, to login with a token:

http://(f5e1f770bfe6 or 127.0.0.1) :8888/?token=e99ef0776ac2c2d848d580e7e86d10a5f8e187fe20be8ae3

* Copy this URL, replace everything within () to the IP address that you noted down in the first step* and paste this new URL in your browser.


For example, if pasting something like this onto the browser opens a screen as shown below, you are ready to go.  http://192.168.99.100:8888/?token=e99ef0776ac2c2d848d580e7e86d10a5f8e187fe20be8ae3


