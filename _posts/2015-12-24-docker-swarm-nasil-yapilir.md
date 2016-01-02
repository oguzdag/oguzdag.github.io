---
layout: post
title: "Docker Swarm nasıl yapılır ve nasıl test edilir?"
published: true
categories: 
  - docker swarm
  - docker
  - carina
---

Docker Swarm gerçekten çok çok çok önemli bir araç. Özellikle docker'ı kişisel bilgisayarınızdan çıkarmaya karar vermişseniz ve deneme aşamasından kullanma aşamasına geçmişseniz, bilmeniz gereken bir araç. Docker swarm, docker'ları bir harmoni içerisinde yönetmenizi ve container'larızı uygun docker'da konumlandırmanızı sağlayan önemli bir cluster aracı. Özellikle Docker'ın, bir development ortamından daha fazlası olduğunu, production için de bir alternatif olduğunu kanıtlıyor. Yakın zamanda [anons edildi](http://blog.docker.com/2015/11/swarm-1-0/), Docker Swarm 1.0 production ortamında kullanılabilecekti. Ve hatta [kapsamlı stress testi de yapıldı](https://blog.docker.com/2015/11/scale-testing-docker-swarm-30000-containers/). Sonuçlar o kadar umut verici ve adamlar o kadar kendilerine güveniyorlar ki, yazının sonuna şunun yazmışlar 

> "We’ll continue to test Swarm, pushing its limits and using the results to harden it." 

buram buram kendine güven kokuyor açıkçası.

![logo-title-final-swarm-2d-copy.png]({{site.baseurl}}/images/logo-title-final-swarm-2d-copy.png)


Docker Swarm kullanarak clusterlama ve ölçekleme yapan bildiğim [Carina](https://getcarina.com/) var. İyi düşünülmüş ve doğru konumlandırılmış bir çözüm. Daha bir çok çözümün bu alanda çıkacağını tahmin ediyorum ama ilk olmak daima farklılık yaratır.Carina ile ilgili daha fazla bilgi [web sayfalarında](https://getcarina.com/docs/overview-of-carina/) var tabii ki. Açık açık yazmışlar, neyi docker, neyi docker-swarm ve neyi kendileri yapıyor.

## Malzemeler

- Docker Toolbox v1.9.1f kurulu olması yeterli
- Haa bir de bu işlem Windows 8.1 üzerinde yapılacak.

## Yapılışı

Öncelikle burada yapacağımız tüm işlemleri Docker Quickstart Terminal kullanarak çalıştıracağız. Kinematic içerisindeki CLI veya komut satırı işime yaramıyor, çünkü komutların arasında linux komutları da var.

Eğer docker ile herhangi bir makine yaratmamış isek, şu anda elimizde bir adet makine olması gerekiyor. O da "default". Aşağıdaki komut ile kontrol edebilirsiniz.

`docher-machine ls`

```
NAME             ACTIVE   DRIVER       STATE     URL                         SWARM                   DOCKER    ERRORS
default          *        virtualbox   Running   tcp://192.168.99.100:2376                           v1.9.1
```

`docker info` komutu ile de içerisinde bulunduğumuz makinenin hangisi olduğunu anlayabiliriz.

```
Containers: 2
Images: 103
Server Version: 1.9.1
Storage Driver: aufs
 Root Dir: /mnt/sda1/var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 107
 Dirperm1 Supported: true
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 4.1.13-boot2docker
Operating System: Boot2Docker 1.9.1 (TCL 6.4.1); master : cef800b - Fri Nov 20 19:33:59 UTC 2015
CPUs: 1
Total Memory: 996.2 MiB
***Name: default***
ID: BP6H:6Y2J:DWYN:B7YY:LOP7:GFUN:BNPB:QB3I:TIAJ:ALSI:XWYG:GL4D
Debug mode (server): true
 File Descriptors: 22
 Goroutines: 38
 System Time: 2015-12-24T11:45:39.915413626Z
 EventsListeners: 0
 Init SHA1:
 Init Path: /usr/local/bin/docker
 Docker Root Dir: /mnt/sda1/var/lib/docker
Labels:
 provider=virtualbox
 ```

burada Name yanında yazan default hangi makine içerisinde bulunduğumuzu gösteriyor.

Emin olduktan sonra, Swarm yaratma işlemine başlıyoruz.

```
docker run swarm create
0cd9d7ca0e14ff4d1960a3cd9c135ac8
```

Bu hashcode önemli çünkü sonrasında kullanacağız bunu. Bu komuttan hemen sonra swarm-master makinesini yaratıyoruz.

```
docker-machine create -d virtualbox --swarm --swarm-master 
--swarm-discovery token://0cd9d7ca0e14ff4d1960a3cd9c135ac8 swarm-master
```

Sonrasında iki adet client yaratıyoruz.

```
docker-machine create -d virtualbox --swarm --swarm-discovery token://0cd9d7ca0e14ff4d1960a3cd9c135ac8 swarm-agent-00
docker-machine create -d virtualbox --swarm --swarm-discovery token://0cd9d7ca0e14ff4d1960a3cd9c135ac8 swarm-agent-01
```

Sonra swarm-master'a geçip kontrollerimizi yapıyoruz. Swarm-master makinesine geçmek için;

```
eval $(docker-machine env --swarm swarm-master)
```

`docker info` ile kontrol ettiğimizde 3 node görünüyor.

```
 Containers: 4
Images: 3
Role: primary
Strategy: spread
Filters: health, port, dependency, affinity, constraint
Nodes: 3
 swarm-agent-00: 192.168.99.105:2376
   Status: Healthy
   Containers: 1
   Reserved CPUs: 0 / 1
   Reserved Memory: 0 B / 1.021 GiB
   Labels: executiondriver=native-0.2, kernelversion=4.1.13-boot2docker, operatingsystem=Boot2Docker 1.9.1 (TCL 6.4.1); master : cef800b - Fri Nov 20 19:33:59
TC 2015, provider=virtualbox, storagedriver=aufs
 swarm-agent-01: 192.168.99.106:2376
   Status: Healthy
   Containers: 1
   Reserved CPUs: 0 / 1
   Reserved Memory: 0 B / 1.021 GiB
   Labels: executiondriver=native-0.2, kernelversion=4.1.13-boot2docker, operatingsystem=Boot2Docker 1.9.1 (TCL 6.4.1); master : cef800b - Fri Nov 20 19:33:59
TC 2015, provider=virtualbox, storagedriver=aufs
 swarm-master: 192.168.99.104:2376
   Status: Healthy
   Containers: 2
   Reserved CPUs: 0 / 1
   Reserved Memory: 0 B / 1.021 GiB
   Labels: executiondriver=native-0.2, kernelversion=4.1.13-boot2docker, operatingsystem=Boot2Docker 1.9.1 (TCL 6.4.1); master : cef800b - Fri Nov 20 19:33:59
TC 2015, provider=virtualbox, storagedriver=aufs
CPUs: 3
Total Memory: 3.064 GiB
Name: swarm-master
```

Hepsinin portları aynı. `docker ps -a` yapıldığında ise her bir agent'ta birer swarm-agent, master'da ise bir master bir agent açık olduğunu görürüz.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
9aa654c525ef        swarm:latest        "/swarm join --advert"   About a minute ago   Up About a minute                       swarm-agent-01/swarm-agent
24e200e3ca4e        swarm:latest        "/swarm join --advert"   2 minutes ago        Up 2 minutes                            swarm-agent-00/swarm-agent
ebbab9db7b32        swarm:latest        "/swarm join --advert"   5 minutes ago        Up 6 minutes                            swarm-master/swarm-agent
ed8842080831        swarm:latest        "/swarm manage --tlsv"   6 minutes ago        Up 6 minutes                            swarm-master/swarm-agent-master 
```

docker run ile bir uygulama çalıştırılmak istendiğinde agent'lardan birisi üzerinde çalışacaktır.

`docker run hello-world`

komutundan sonra

`docker ps -a`


yapıldığında aşağıda görüldüğü gibi, swarm-master üzerinde run yapmamıza rağmen swarm-agent-00'ın işi aldığı görülecektir.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED                  STATUS                     PORTS               NAMES
ae3414a0a1e1        hello-world         "/hello"                 Less than a second ago   Exited (0) 4 seconds ago                       swarm-agent-00/drunk_wing
9aa654c525ef        swarm:latest        "/swarm join --advert"   2 minutes ago            Up 2 minutes                                   swarm-agent-01/swarm-agent
24e200e3ca4e        swarm:latest        "/swarm join --advert"   3 minutes ago            Up 3 minutes                                   swarm-agent-00/swarm-agent
ebbab9db7b32        swarm:latest        "/swarm join --advert"   6 minutes ago            Up 6 minutes                                   swarm-master/swarm-agent
ed8842080831        swarm:latest        "/swarm manage --tlsv"   6 minutes ago            Up 7 minutes                                   swarm-master/swarm-agent-master
```

## Son Söz

Denemelerimde bazı sıkıntılar yaşadım, mesela bu yarattığım makineleri kaynak çok tüketiyor sonra geri açarım diye kapattıktan sonra açtığımda hata aldım, o nedenle yeniden yaratmak zorunda kaldım.

Bu arada bu işlemleri yaparken network bağlantımda bazı sıkıntılar oldu, o nedenle vm yaratılmasına rağmen swarm konfigürasyonu yarım kaldığı için "docker ps -a" komutunda göremedim.

Bunları tekrar yaratıp, çözümlerini en kısa zamanda yazacağım.

Şu aşamada daha güçlü bir laptop alıp, lokalime kapsamlı bir docker swarm kurmalıyım.
