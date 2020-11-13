FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"
#copy file with settings
COPY ./requirements.txt /requirements.txt
#install nessasary packs to temporary folder
RUN apk add --upgrade libpq
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers postgresql-dev
#install requirements
RUN pip install -r /requirements.txt
#delete temporary packs
RUN apk del .tmp

#create folder
RUN mkdir /project0001api
#copy files from host to guest machine
COPY ./project0001api /project0001api
#move to projects folder
WORKDIR /project0001api
#copy scripts folder
COPY ./scripts /scripts

#give permissions
RUN chmod +x /scripts/*
#create folders for static files
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

#add new user api for running app
RUN adduser -D api
#give api user permissions
RUN chown -R api:api /vol
RUN chmod -R 755 /vol/web 
#switch to user
USER api
#run shell script to start
CMD ["entrypoint.sh"]