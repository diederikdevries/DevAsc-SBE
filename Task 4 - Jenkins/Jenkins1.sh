#!/bin/bash
echo "Aanmaken tempdir..."
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
echo "Inhoud van Dockerfile"
cat tempdir/Dockerfile

cd tempdir
cp ../index.html .
docker build -t examapp .
docker run -t -d -p 8081:8081 --name examrunning examapp
docker ps -a
