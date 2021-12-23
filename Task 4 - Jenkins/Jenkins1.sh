#!/bin/bash
echo "Dit werkt"
mkdir tempdir
# mkdir tempdir/templates
# mkdir tempdir/static
# cp sample_app.py tempdir/.
# cp -r templates/* tempdir/templates/.
# cp -r static/* tempdir/static/.
FROM httpd:2-alpine >> tempdir/Dockerfile
COPY ./index.html /usr/local/apache2/htdocs >> tempdir/Dockerfile
RUN apk update >> tempdir/Dockerfile
RUN sed -i 's@^#LoadModule rewrite_module modules/mod_rewrite\.so@LoadModule rewrite_module modules/mod_rewrite.so@' /usr/local/apache2/conf/httpd.conf >> tempdir/Dockerfile
RUN sed -i 's/^Listen 80/Listen 8081/g' /usr/local/apache2/conf/httpd.conf >> tempdir/Dockerfile
RUN sed -i 's/^<VirtualHost *:80>/<VirtualHost *:8081>/g' /usr/local/apache2/conf/extra/httpd-vhosts.conf >> tempdir/Dockerfile
EXPOSE 8081/tcp >> tempdir/Dockerfile
# cd tempdir
# docker build -t sampleapp .
# docker run -t -d -p 5050:5050 --name samplerunning sampleapp
# docker ps -a
