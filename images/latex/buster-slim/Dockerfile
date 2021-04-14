FROM debian:buster-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y --no-install-recommends \
    texlive-full \
    biber \
    latexmk \
    make \
    python3-pygments \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*
RUN apt-get update \
&& apt-get install -y --no-install-recommends cpanminus gcc libc6-dev \
&& cpanm -n -q Log::Log4perl \
&& cpanm -n -q XString \
&& cpanm -n -q Log::Dispatch::File \
&& cpanm -n -q YAML::Tiny \
&& cpanm -n -q File::HomeDir \
&& cpanm -n -q Unicode::GCString \
&& apt-get remove -y cpanminus gcc libc6-dev \
&& apt-get clean autoclean \
&& apt-get autoremove -y \
&& rm -rf /var/lib/{apt,dpkg,cache,log}/
