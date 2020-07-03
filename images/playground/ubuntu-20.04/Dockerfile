FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL /bin/bash
RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    git \
    gnupg \
    jq \
    less \
    lsb-core \
    make \
    nano \
    software-properties-common \
    sudo \
    vim \
    wget \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]
