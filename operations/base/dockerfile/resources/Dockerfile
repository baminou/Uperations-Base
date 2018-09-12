FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev
RUN cd /usr/local/bin
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
RUN pip3 install pipreqs

COPY . /app

RUN pipreqs /app
RUN pip3 install -r /app/requirements.txt

ENTRYPOINT ["python3","/app/main.py"]