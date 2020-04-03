# JSON post request receiver by Python + Flask

Notes
* To run Python + Flask server locally, "server.py".
* To run JSON post request client locally, "client.py".
* JSON post request result will be saved in /jsonpost folder.
* JMeter test script to burn-in server, "pyjsonreceiver-jmeter-tester.jmx".

Dockerization
* docker build -t easonlai/pyjsonreceiver .
* docker run -p 5000:5000 easonlai/pyjsonreceiver
* docker exec -it e5517f5977ba bash <- Interactive login into container and check the result folder /jsonpost.
* docker push easonlai/pyjsonreceiver

https://hub.docker.com/repository/docker/easonlai/pyjsonreceiver