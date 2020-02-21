FROM python:3.6

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-pip \
    build-essential \
    swig \ 
    libpulse-dev \ 
    libasound2-dev \ 
    software-properties-common \
    zip \
    unzip \
    yasm \
    libtbb2 \
    libtbb-dev \
    libpng-dev \
    libtiff-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*


RUN pip3 install pathlib2 theano
RUN pip3 install pandas numpy
RUN pip3 install --upgrade pocketsphinx
RUN pip3 install --user -U nltk
RUN python3 -m nltk.downloader -d /usr/local/share/nltk_data all
RUN pip3 install SpeechRecognition

RUN pip3 install Flask

EXPOSE 5000
WORKDIR /usr/src/app
COPY . .
CMD[ "python3", "./app.py"]


