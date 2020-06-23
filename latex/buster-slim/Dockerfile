FROM debian:buster-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      texlive-full \
      biber \
      latexmk \
      make \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
