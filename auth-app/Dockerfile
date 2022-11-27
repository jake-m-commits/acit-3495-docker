FROM python:latest

# get code
COPY flaskApp /app/flaskApp

# Create app directory
WORKDIR /app/flaskApp

# install deps
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
