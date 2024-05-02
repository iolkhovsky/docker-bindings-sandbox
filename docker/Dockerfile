FROM ubuntu:22.04

RUN mkdir /setup
WORKDIR /setup

COPY install.sh .
COPY requirements.txt .
RUN chmod +x install.sh
RUN ./install.sh
COPY build_opencv.sh .
RUN chmod +x build_opencv.sh
RUN ./build_opencv.sh
COPY install_bazel.sh .
RUN chmod +x install_bazel.sh
RUN ./install_bazel.sh

RUN mkdir /workspace
WORKDIR /workspace

CMD ["/bin/bash"]
