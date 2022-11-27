FROM python:latest

WORKDIR /usr/app/src

COPY ./* ./

RUN pip install -r requirements.txt

# default mongo port
EXPOSE 27017

CMD [ "python", "analytics.py"]
