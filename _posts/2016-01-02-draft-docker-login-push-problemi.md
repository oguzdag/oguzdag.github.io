---
published: false
layout: post
title: Docker Login/Push Problemi
---

docker'a image push etmek istenirse, öncelikle login olmak gerekir.


$ docker login
Username: oguzdag
Password:
Email: oguz.dag@gmail.com

Error response from daemon: Unexpected status code [403] : <html><body><h1>403 Forbidden</h1>

Request forbidden by administrative rules.

</body></html>


bu hatanın sebebi


https://github.com/docker/docker/issues/18019


workaround ise


https://github.com/docker/hub-feedback/issues/473


docker login --username=myuser --password=mypassword --email=myemail https://index.docker.io/v1/
