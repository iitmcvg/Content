# README

## Getting Started with Docker 

Firstly, download a compatible version of docker from here:

* For installation of Docker in Windows - https://download.docker.com/win/stable/DockerToolbox.exe 
* For installation of Docker in Linux(Ubuntu) - https://docs.docker.com/install/linux/docker-ce/ubuntu/   
* For installation of Docker in Mac -   
https://download.docker.com/mac/stable/DockerToolbox.pkg  


### Installation

* Before installation, additional software packages like Kitematic and Virtualbox can be unchecked. 
* The installer adds Docker Toolbox to your Applications folder.   
* On your Desktop, find the Docker QuickStart Terminal icon.  
* Click the Docker QuickStart icon to launch a pre-configured Docker Toolbox terminal.    
* If the system displays a User Account Control prompt to allow VirtualBox to make changes to your computer. Choose Yes.  
* The terminal does several things to set up Docker Toolbox for you. When it is done, the terminal displays the $ prompt.  
* Make the terminal active by clicking your mouse next to the $ prompt.
* The prompt is traditionally a $ dollar sign. You type commands into the command line which is the area after the prompt. Your cursor is indicated by a highlighted area or a | that appears in the command line. After typing a command, always press RETURN.

* Type the **docker run hello-world** command and press RETURN.
* The command does some work for you, if everything runs well, the command’s output looks like this:

```
$ docker run hello-world
 Unable to find image 'hello-world:latest' locally
 Pulling repository hello-world
 91c95931e552: Download complete
… … … …
```

### Running the Container

* Run the command **docker-machine ip** and make a note of the IP address shown as output.

* Run the container:
```
docker run -it --name cvi --rm -p 8888:8888 iitmcvg/session:intro_CV bash
```

The image has the following tools:

  * OpenCV 3.4.1
  * Tensorflow 1.10
  * Keras
  * Jupyter
  * Scientific python: Numpy, Scipy, Matplotlib ... etc.

* The command does some work for you. Downloading takes around 5 minutes. Be patient. Once the extraction is complete, you should see a terminal shell corresponding to the container (eg: root@xxxxxx).

* Now, update session contents by giving the following command:

```
git pull
```

* Run Jupyter with the following command.

```
jupyter notebook --ip=0.0.0.0 --allow-root
```

* If everything goes well, the command’s output should look like this:

```
Copy/paste this URL into your browser when you connect for the first time, to login with a token:

http://(f5e1f770bfe6 or 127.0.0.1) :8888/?token=e99ef0776ac2c2d848d580e7e86d10a5f8e187fe20be8ae3
```

* Copy this URL, replace everything within () to the IP address that you noted down in the first step and paste this new URL in your browser.

For example, http://192.168.99.100:8888/?token=e99ef0776ac2c2d848d580e7e86d10a5f8e187fe20be8ae3

* You are good to go if Jupyter Notebooks successfully opens up in your browser.



