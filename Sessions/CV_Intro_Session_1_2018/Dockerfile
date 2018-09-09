ARG UBUNTU_VERSION=16.04
FROM ubuntu:${UBUNTU_VERSION}

LABEL maintainer="CVI cvigroup.cfi@gmail.com"

ENV OPENCV_DIR "$LIB_DIR/opencv"
RUN mkdir -p "$OPENCV_DIR"

# Pick up some dependencies
RUN apt-get update && \
    apt-get -y install wget git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
apt-get install -y software-properties-common && \
add-apt-repository ppa:george-edison55/cmake-3.x && \
apt-get install -y cmake && \
apt-get update

ARG USE_PYTHON_3_NOT_2=True
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}

RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip

RUN ${PIP} install --upgrade \
    pip \
    setuptools

ARG TF_PACKAGE=tensorflow
RUN ${PIP} install ${TF_PACKAGE}

COPY bashrc /etc/bash.bashrc
RUN chmod a+rwx /etc/bash.bashrc

RUN ${PIP} install jupyter scikit-image scipy numpy matplotlib keras opencv-python

RUN apt-get -y install unzip

COPY bashrc /etc/bash.bashrc
RUN chmod a+rwx /etc/bash.bashrc

RUN mkdir /session && chmod a+rwx /session 
RUN mkdir /.local && chmod a+rwx /.local
WORKDIR /session
EXPOSE 8888

RUN apt update && apt install -y libsm6 libxext6 libgtk2.0-dev
RUN  apt-get install -y git vim  curl
RUN ${PIP} install h5py natsort argparse tqdm html5lib bleach opencv-contrib-python

RUN git clone https://github.com/iitmcvg/Content.git 
RUN mv Content/Sessions/CV_Intro_Session_1_2018/ /session && rm -rf /Content

WORKDIR /session
CMD ["bash"]