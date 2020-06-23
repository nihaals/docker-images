FROM debian:buster
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y \
  curl \
  wget \
  sudo \
  make \
  apt-transport-https \
  ca-certificates \
  gnupg \
  software-properties-common \
  jq \
  git \
  lsb-release \
  && \
apt-get autoremove -y && \
apt-get clean -y && \
rm -rf /var/lib/apt/lists/*
CMD ["bash"]
