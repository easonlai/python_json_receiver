FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add --no-cache bash
EXPOSE 5000
CMD python ./server.py