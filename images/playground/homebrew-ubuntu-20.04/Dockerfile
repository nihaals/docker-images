FROM ubuntu:20.04

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL /bin/bash
ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH

RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y \
    build-essential \
    curl \
    file \
    git \
    sudo \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/* \
&& groupadd --gid $USER_GID $USERNAME \
&& useradd -mrs /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
&& chmod 0440 /etc/sudoers.d/$USERNAME \
&& sudo -u $USERNAME bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
USER $USERNAME
RUN brew install -s perl \
&& brew install \
    bash \
    bash-completion@2 \
    curl \
    git \
    gnupg \
    jq \
    less \
    make \
    nano \
    vim \
    wget
CMD ["/bin/bash"]
