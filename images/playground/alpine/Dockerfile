FROM alpine:latest
ENV SHELL /bin/bash
RUN apk update \
&& apk upgrade \
&& apk add \
    bash \
    ca-certificates \
    curl \
    git \
    gnupg \
    jq \
    less \
    make \
    nano \
    sudo \
    vim \
    wget \
&& rm -rf /var/cache/apk/*
CMD ["/bin/bash"]
