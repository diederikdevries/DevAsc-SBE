FROM httpd:2-alpine
COPY ./index.html /usr/local/apache2/htdocs
RUN apk update
RUN sed -i 's@^#LoadModule rewrite_module modules/mod_rewrite\.so@LoadModule rewrite_module modules/mod_rewrite.so@' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's/^Listen 80/Listen 8081/g' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's/^<VirtualHost *:80>/<VirtualHost *:8081>/g' /usr/local/apache2/conf/extra/httpd-vhosts.conf
EXPOSE 8081/tcp