---
layout: post
title: Jenkinsi Docker Üzerinde Çalıştırma
published: true
categories: 
  - jenkins
  - docker
---


Uzun süredir blog yazarım, ve daima blogların insanı sıkmaması taraftarıyımdır. Ben de o tarzda blog yazmaya karar verdim. Madem blog'un adı **Teknoloji Mutfağı**, o halde her tür implementasyonda bu mutfakta pişmiş bir yemek oluyor.

![Docker]({{site.baseurl}}/images/homepage-docker-logo.png) 

İlk yazı olarak [Docker](https://hub.docker.com/) ve [Jenkins](https://jenkins-ci.org/) olacak içeriğinde. Böylece hem Docker'a, hem de Jenkins'e giriş yapmış olacağım. 

![Jenkins]({{site.baseurl}}/images/jenkins_logo.png)

Açıkçası yıllardır Jenkins kullanıyorum, taa Hudson'dan beri , Docker ile de bu yakınlarda tanıştım. Aslında docker ile tanışmam bir başka open source uygulamayı en hafif ve laptop'uma en az kurulum ile nasıl hayata geçiririm derken buldum. Daha önce bir arkadaşım bahsetmişti ama bu kadar hoşuma gideceğini zannetmiyordum. Docker ile ilgili ileride çok daha açıklayıcı yazılar yazacağım, bu seferlik sadece Jenkins'i en hızlı ve en kurulumsuz şekilde nasıl ayağa kaldırıyoruz onu anlatacağım.

## Malzemeler

* 190 MB Docker Toolbox v1.9.1f (https://www.docker.com/docker-toolbox)
* 708 MB Jenkins ver.1.625.3
* Alabildiği kadar İşletim Sistemi Windows 8.1 

## Yapılışı

Malzemelerimizden Docker Toolbox'ı, hemen yanında bulunan linkten indirip kuruyoruz. Kurulum tamamlandıktan sonra Docker QuickStart Terminal'ı çalıştırıyoruz. Bu bize bir komut satırı ekranı açıyor, sürpriiiiiz, Docker dediğimiz bir komut satırı arayüzü, bir client yani. Yapmamız gereken [dockerhub](https://hub.docker.com/)'dan istediğimiz projeyi almak ve ardından çalıştırmak.

Komut şekli basit

> docker - komut - container

Komut satırı basit `docker pull jenkins` ile jenkins docker imajının son halini lokalimize alıyoruz.

```
$ docker pull jenkins
Using default tag: latest
latest: Pulling from library/jenkins
9ee13ca3b908: Pull complete
23cb15b0fcec: Pull complete
5e5f21412e19: Pull complete
df82ac64861d: Pull complete
ce5064412ef8: Pull complete
46cb1e153bac: Pull complete
65e700d53fe2: Pull complete
e4c1902ba8e2: Pull complete
041291567735: Pull complete
38bbdcdf22d3: Pull complete
ee4c5fbd36c4: Pull complete
d4849089125b: Pull complete
20d5b56ce07a: Pull complete
0f5dea7dfc5b: Pull complete
03146e17cab8: Pull complete
56b017425a9d: Pull complete
cd7b57d2dd48: Pull complete
caddf6da8997: Pull complete
7f6985b7763d: Pull complete
b188b3306bfe: Pull complete
908ef1cf00c8: Pull complete
d50a5ae10995: Pull complete
943cf2d379e0: Pull complete
268d99f210c3: Pull complete
72d6788c4cf5: Pull complete
715450d4ed36: Pull complete
c5344d64bc07: Pull complete
63c8beb95b2f: Pull complete
c9bf8ee44a75: Pull complete
9dcf64060fae: Pull complete
c37f2cb6820f: Pull complete
b368fe5ad08f: Pull complete
eb09f4d99ddf: Pull complete
Digest: sha256:f0459bf4d127c4e6d710c745075017a3448a7416d46d547f51928c763a184bc1
Status: Downloaded newer image for jenkins:latest
```

Hooop jenkins lokal imajların arasına geldi.

```
USER@OGUZ MINGW64 ~
$ docker images
```

![icerik.png]({{site.baseurl}}/images/icerik.png)


Şimdi yapmamız gereken tek şey aşağıdaki komutla çalıştırmak

```
$ docker run -p 8080:8080 -p 50000:50000 jenkins
```

Eğer 8080 ve 50000 portları yerine docker'ın kendisinin otomatik olarak port atamasını istiyorsanız aşağıdaki satır yeterli.

```
$ docker run -P jenkins
```

Farkındaysanız, neredeyse `-p`veya `-P` dışında hiç parametre yok, o da container içerisindeki port'ları docker'a hangi port'lardan map edeceğimizi söylüyoruz.

**_Önemli not :_** docker run komutunda eğer `-v` parametresini kullanıyorsanız, path yazarken "/" yerine "//" kullanın, windows'un handikaplarından birisi (https://github.com/docker/docker/issues/18290)

**Örnek:**

```
docker run -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins
```
yerine
``` 
docker run -p 8080:8080 -p 50000:50000 -v //your//home://var//jenkins_home jenkins
```

Ve ta-tam artık Jenkins'imiz servise hazır. `docker ps -a` komutu ile çalışan jenkins container'ının portunu kontrol edin ve ardından `http://192.168.99.100:<port>` ile giriş yapabilirsiniz. Afiyetle çalışabilirsiniz.
