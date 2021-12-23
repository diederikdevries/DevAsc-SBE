#!/bin/bash
echo "Dit werkt"
mkdir tempdir
# mkdir tempdir/templates
# mkdir tempdir/static
# cp sample_app.py tempdir/.
# cp -r templates/* tempdir/templates/.
# cp -r static/* tempdir/static/.
echo "FROM httpd:2-alpine" >> tempdir/Dockerfile
echo "COPY ./index.html /usr/local/apache2/htdocs" >> tempdir/Dockerfile
echo "RUN apk update" >> tempdir/Dockerfile
echo "RUN sed -i 's@^#LoadModule rewrite_module modules/mod_rewrite\.so@LoadModule rewrite_module modules/mod_rewrite.so@' /usr/local/apache2/conf/httpd.conf" >> tempdir/Dockerfile
echo "RUN sed -i 's/^Listen 80/Listen 8081/g' /usr/local/apache2/conf/httpd.conf" >> tempdir/Dockerfile
echo "RUN sed -i 's/^<VirtualHost *:80>/<VirtualHost *:8081>/g' /usr/local/apache2/conf/extra/httpd-vhosts.conf" >> tempdir/Dockerfile
echo "EXPOSE 8081/tcp" >> tempdir/Dockerfile
# cd tempdir
# docker build -t sampleapp .
# docker run -t -d -p 5050:5050 --name samplerunning sampleapp
# docker ps -a
