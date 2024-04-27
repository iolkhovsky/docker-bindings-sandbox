FROM ubuntu:22.04

RUN mkdir /setup
WORKDIR /setup

COPY install.sh .
COPY requirements.txt .
RUN chmod +x install.sh
RUN ./install.sh

RUN mkdir /workspace
WORKDIR /workspace

CMD ["/bin/bash"]
