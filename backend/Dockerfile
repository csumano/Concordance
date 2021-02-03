FROM tiangolo/uwsgi-nginx:python3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY test-requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r test-requirements.txt

COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT ["uwsgi"]

CMD ["--http", ":8000", "-w", "swagger_server.__main__","-p","16"]