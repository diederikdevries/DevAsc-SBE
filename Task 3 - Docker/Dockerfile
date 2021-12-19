FROM httpd:2-alpine
COPY ./index.html /usr/local/apache2/htdocs
RUN apk update
RUN sed -i 's@^#LoadModule rewrite_module modules/mod_rewrite\.so@LoadModule rewrite_module modules/mod_rewrite.so@' /usr/local/apache2/conf/httpd.conf