FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get upgrade -y

ADD entrypoint.sh /
ADD requirements.txt /
ADD main.py /

RUN pip install -r /requirements.txt
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
