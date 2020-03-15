FROM ubuntu:18.04
MAINTAINER Inhyuk Choi <dlsgur9710@naver.com>

EXPOSE 8000

RUN apt-get -y update
RUN apt-get -y update
RUN apt-get -y install python3.8 python3-pip python3.8-dev libmysqlclient-dev
RUN ln -sf /usr/bin/python3.8 /usr/bin/python3

RUN pip3 install --upgrade pip
RUN apt-get -y update

RUN mkdir /code
WORKDIR /code

ADD requirement.txt /code/
RUN pip3 install -r requirement.txt

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh
CMD ["/bin/bash", "start.sh"]



