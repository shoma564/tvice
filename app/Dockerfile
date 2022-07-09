##FROM alpine:3.13
FROM ubuntu:18.04


##RUN apk add --update py3-pip
RUN apt -y update
RUN apt -y install python3 python3-pip curl wget
RUN apt autoremove
RUN pip3 install --upgrade pip setuptools
RUN apt -y install nodejs npm


RUN mkdir -p /usr/src/app/
COPY ./requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
RUN npm cache clean && npm install n -g && n stable && ln -sf /usr/local/bin/node /usr/bin/node

#COPY ./pyapp /usr/src/app/
#COPY ./pyapp/templates/ /usr/src/app/templates/

EXPOSE 5000

WORKDIR /usr/src/app/
CMD ["python3", "/usr/src/app/app.py"]
