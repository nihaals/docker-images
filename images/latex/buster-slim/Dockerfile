FROM debian:buster-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y --no-install-recommends \
    texlive-full \
    biber \
    latexmk \
    make \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*
