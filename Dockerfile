FROM ubuntu:20.04


### Set environment variables
USER root
# Change default Shell to bash
SHELL ["/bin/bash", "-c"]
# Set Timezone
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
# Change Ubuntu repository to Kakao server in Republic of Korea
RUN sed -i 's/^deb http:\/\/archive.ubuntu.com/deb http:\/\/mirror.kakao.com/g' /etc/apt/sources.list
RUN sed -i 's/^deb http:\/\/security.ubuntu.com/deb http:\/\/mirror.kakao.com/g' /etc/apt/sources.list
# Configure default Pypi repository
RUN mkdir -p ~/.config/pip \
    && echo -e \
"[global]\n"\
"index-url=https://mirror.kakao.com/pypi/simple/\n"\
"trusted-host=mirror.kakao.com\n"\
        > ~/.config/pip/pip.conf

# Copy files
COPY isles /root/workspace/isles
COPY *.py /root/workspace/./

# Install essential packages
RUN apt update \
    && apt install -y \
        tzdata \
        beep \
        wget \
        git \
        zip \
        ca-certificates \
        apt-transport-https \
        python3 \
        python3-pip

RUN pip install \
        numpy \
        nibabel \
        tqdm \
        git+https://github.com/npnl/bidsio \
        scikit-learn

# Clean the cache
RUN apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/workspace
ENTRYPOINT [ "python3", "convert_to_BIDS.py"]