FROM ubuntu:trusty

RUN echo "deb http://ppa.launchpad.net/pypy/ppa/ubuntu trusty main" > \
    /etc/apt/sources.list.d/pypy-ppa.list

RUN apt-key adv --keyserver keyserver.ubuntu.com \
                --recv-keys 2862D0785AFACD8C65B23DB0251104D968854915
RUN apt-get update

RUN apt-get install -qyy \
    -o APT::Install-Recommends=false -o APT::Install-Suggests=false \
    python-pip python-dev build-essential python-virtualenv pypy libffi6

RUN virtualenv -p /usr/bin/pypy /appenv
RUN . /appenv/bin/activate
RUN pip install flask
ADD . /code
WORKDIR /code
CMD python app.py