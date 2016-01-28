---
layout: post
title: Mevcut çalışan bir MongoDB'yi Docker üzerine taşıma
published: true
categories: 
  - docker
  - mongodb
---
Docker ile ilgili kendimi geliştirmek üzere bir çalışma listesi hazırladım. **"docker run, docker run, docker run"** tekrarları ile çok birşey öğrenemeyeceğimi bildiğim için böyle birşey yaptım. Listeyi görmeniz lazım, abik gubik şeyler var, kimisini hayata geçirmeden sildim bile. Docker konusunda ancak bu şekilde ustalaşabileceğimi düşünüyorum. Ve bu listede yaptığım ve blog olarak yayınlayabileceğim nitelikte olanları da burada paylaşmaya karar verdim. Zaten Teknoloji Mutfağı dememin sebebi de bu. Buraya dış dünyada bulduğum bir blogun çevirisini falan koymak istemiyorum. Bu mutfakta yemek yapıp bu yemeğin tarifini okuyanlar ile paylaşmak istiyorum. 

İşte bu sefer de bunu yapacağım. 

Önce durum analizi; lokalimde bir takım web sayfalarındaki bilgileri indirip bunları veritabanına atan birşeyler yazıyorum.. Hayır, burada paylaşabileceğim bir konu değil bu. Evet, ne kullandığımı anlatacağım tabii ki. Python ile yazıyorum, arka tarafta veritabanı olarak da [MongoDB](https://www.mongodb.org/) kullanıyorum. MongoDB'yi ise, tamamen hayatıma çeşitlilik getirmek için kullanıyorum. Dedim ya yeni şeyler denemeye bayılırım. Demedim mi? Demediysem şimdi söyleyeyim. Yeni şeyler denemeye bayılırım. Neyse, sadede gelelim. 

**Ubuntu 14.04 üzerinde çalışan MongoDB nasıl Docker üzerine taşınır?**

Öncelikle MongoDB'nin data'yı nerede tuttuğunu bulmamız lazım. 

```
$ ps -ef | grep mongod
mongodb   1188     1  0 Oca26 ?        00:02:29 /usr/bin/mongod --config /etc/mongod.conf
oguzdag   7321  4304  0 12:55 pts/4    00:00:00 grep --color=auto mongod
```
Konfigürasyon dosyası ```/etc/mongod.conf``` içerisinde aşağıdaki satırlar data dosyalarının nerede olduğunu gösteriyor.

```
storage:
  dbPath: /var/lib/mongodb
```

MongoDB servisini kapatıyoruz.

```
$ sudo service mongod stop
```

MongoDB ile ilgili tüm paketleri siliyoruz.

```
$ sudo apt-get remove mongodb-org
$ sudo apt-get remove mongodb-org-mongos mongodb-org-server mongodb-org-shell mongodb-org-tools
```

MongoDB'nin data klasörünü çalıştıracağımız MongoDB Docker Container'ına parametre olarak veriyoruz.

```
$ docker run --name mongodb -v /var/lib/mongodb:/data/db -p 127.0.0.1:27017:27017 -d mongo:latest
```

_**Problem:**_
**begin**
burada -p ile verdiğimiz parametreye 127.0.0.1 vermemizin sebebi ise, 

```-p 127.0.0.1:27017:27017``` yerine ```-p 27017:27017``` verildiğinde ya da bu parametre hiç set edilmediğinde (default olarak container'ın 27017 portu hostun 27017 portuna map olur) Python ile yazdığım kodlar MongoDB'ye bağlanmaya çalıştığında aşağıdaki hatayı alıyor

_pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [Errno 111] Connection refused_
**end**

Artık MongoDB Docker container üzerinde çalışıyor ve verileri de kaybetmedik. Bunu test etmek de kolay. 

```
$ sudo apt-get install mongodb-org-shell=3.2.1
```

```
$ mongo
MongoDB shell version: 3.2.1
connecting to: test
Server has startup warnings: 
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] 
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] 
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/defrag is 'always'.
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2016-01-27T11:35:02.055+0000 I CONTROL  [initandlisten] 
> use XXXXXXXXX
switched to db XXXXXXXXX
> db.getCollectionNames()
[ "XXXX", "YYYY", "ZZZZ" ]
> db.XXXX.find().count()
16333
> 
```

_**Problem**_
**begin**
Burada Mongo Shell'in özellikle 3.x versiyonunu yüklememizin sebebi ise https://docs.mongodb.org/manual/reference/method/db.getCollectionNames/ sayfasında ufak bir ayrıntı olarak anlatılan 

For MongoDB 3.0 deployments using the WiredTiger storage engine, if you run db.getCollectionNames() from a version of the mongo shell before 3.0 or a version of the driver prior to 3.0 compatible   version, db.getCollectionNames() will return no data, even if there are existing collections. For more information, see WiredTiger and Driver Version Compatibility.
**end**

Şimdilik bu kadar. Listemdeki bir sonraki implementasyonu yapıncaya kadar.


