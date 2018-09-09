ARG UBUNTU_VERSION=16.04
FROM ubuntu:${UBUNTU_VERSION}

LABEL maintainer="CVI cvigroup.cfi@gmail.com"

# arguments
ARG USE_PYTHON_3_NOT_2=True
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}
ARG TF_PACKAGE=tensorflow

# Linux packages
RUN apt-get update && \
    apt-get -y install \
    git \
    libsm6 \
    libxext6 \
    libgtk2.0-dev \ 
    ${PYTHON} \
    ${PYTHON}-pip \
    software-properties-common \
    unzip \
    vim \
    wget && \
    apt-get clean && \
    add-apt-repository ppa:george-edison55/cmake-3.x && \
    apt-get -y install cmake && \ 
    rm -rf /var/lib/apt/lists/* && \
    apt-get update
    
# Python packages
RUN ${PIP} install --upgrade \
    pip \
    argparse \
    bleach \
    h5py \
    html5lib \ 
    jupyter \
    keras \
    matplotlib \
    numpy \
    natsort \
    opencv-python \
    opencv-contrib-python \
    setuptools \
    scikit-image \
    scipy \
    ${TF_PACKAGE} \
    tqdm 

# Bashrc
COPY bashrc /etc/bash.bashrc
RUN chmod a+rwx /etc/bash.bashrc 

# Sess update
COPY update_sess.sh /update_sess.sh

# Repo for session
RUN git clone https://github.com/iitmcvg/Content.git
RUN chmod a+rw /Content 
WORKDIR /Content/Sessions/CV_Intro_Session_1_2018
#RUN mv /CV_Intro_Session_1_2018 /session && chmod a+rwx /session 
RUN mkdir /.local && chmod a+rwx /.local

#WORKDIR /session
CMD ["bash"]
