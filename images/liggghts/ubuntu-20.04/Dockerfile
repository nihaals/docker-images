FROM ubuntu:20.04 AS build
WORKDIR /build
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    git \
    libopenmpi-dev libvtk6-dev \
&& rm -rf /var/lib/apt/lists/* \
&& git clone https://github.com/CFDEMproject/LIGGGHTS-PUBLIC.git \
&& cd LIGGGHTS-PUBLIC/src \
&& make auto

FROM ubuntu:20.04
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openmpi-bin libvtk6.3 \
&& rm -rf /var/lib/apt/lists/*
COPY --from=build /build/LIGGGHTS-PUBLIC/src/lmp_auto /liggghts
ENTRYPOINT ["/liggghts"]
