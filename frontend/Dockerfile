FROM nginx:latest

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./*.html /usr/share/nginx/html/

RUN chmod 755 -R /usr/share/nginx/html
