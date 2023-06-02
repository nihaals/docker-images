FROM ubuntu:20.04
WORKDIR /build
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    git \
    openmpi-bin libopenmpi-dev libvtk6.3 libvtk6-dev \
&& rm -rf /var/lib/apt/lists/* \
&& git clone https://github.com/CFDEMproject/LIGGGHTS-PUBLIC.git \
&& cd LIGGGHTS-PUBLIC \
&& git checkout bbd23c8521fe0a4f3f5bfd0d3dc9a7dddd68d90b \
&& cd src \
&& make auto \
&& ./lmp_auto -help # Smoke test
ENTRYPOINT ["/build/LIGGGHTS-PUBLIC/src/lmp_auto"]
