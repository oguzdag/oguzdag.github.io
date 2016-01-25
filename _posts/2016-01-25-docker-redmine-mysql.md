---
layout: post
title: Docker üzerinde Redmine kurulumu ve dikkat edilmesi gerekenler
published: true
categories: 
  - docker
  - redmine
  - mysql
---


Her ne kadar kurumsal bir ortamda çalışsam da, daima bilginin paylaşılabilir olması gerektiğine inananlardanım. **"Kurumsal ortamda paylaşım olmaz mı?"** diye sorabilirsiniz. Lafı uzatmadan şunu söyleyebilirim, **"Hayır olmaz!"**. Gerçekten olmaz, kurumsal ortamda birbirine bilgi aktarmak diye birşey yoktur, fakat başkasının bilgisi ile prim yapmak çok revaçta bir konudur. Bu etik olmayan davranış şekilleri tamamen farklı bir bilim dalının konusu dolayısıyla çok fazla karıştırmayacağım. 

Konuya dönelim, ben paylaşımı severim, bilgimi daima paylaşmışımdır. İlk önce [Twiki](http://twiki.org/) ile başlamıştım bu paylaşımı yaygınlaştırma olayına. Eski blogumda da bununla ilgili [Dokümantasyon ve Twiki - I](http://ozidethonjava.blogspot.com.tr/2007/09/dokmantasyon-ve-twiki-i-dokmantasyon.html) ve [Dokümantasyon ve Twiki - II](http://ozidethonjava.blogspot.com.tr/2007/09/dokmantasyon-ve-twiki-ii-twiki.html) yazıları bu konularda az çok bilgi veriyor. Twiki implementasyonu zor bir Wiki idi. Kısa zaman sonra bunun yerine [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)yi koydum. 2009'da idi sanırım. Bir hayli doküman birikti bunun üzerinde. Neredeyse tüm operasyonlarımızı, tüm sorunlarımızı, tüm şemalarımızı, tüm dokümanlarımızı buraya kaydettik. Artık yanımda çalışan arkadaşların ayrılmaları sancı yaratmıyordu. Hatta yeni gelen arkadaşlara, **al şu wiki'den oku** demek o kadar keyifli idi ki. Gözlerindeki **"Kurumsal yerlerde Wiki'nin ne işi var?"** ifadesini görmelisiniz.

MediaWiki ile birlikte JIRA kullanıyorduk, 10 dolara 10 kullanıcı lisansı almıştım. Entegrasyonu olmasa da, işleri yürütebiliyorduk. Sonra zamanla kurumsal kültürün altında kaldım ve JIRA lisansımı yenilemedim, Wiki'yi ise zorla ayakta tutuyordum. Ve [Docker](https://hub.docker.com/) ile tanıştım. Docker ile tanıştıktan ve imajları gördükten sonra artık beni kimsenin durduramayacağını düşünmeye başladım. Docker Hub'da yok yok :) Neyse yine konu başka yerlere dağılıyor.

İlk tercihim Tuleap'tı dürüst konuşmak gerekirse, ama Docker container'ını ayağa kaldırmakta o kadar zorlandım ki. Tam hoop docker container ayakta dediğimde, bu seferde kullanıcı adı ve şifre kısımları ile ilgili sıkıntı yaşadım. Ben de [Redmine](http://www.redmine.org/)'ı denemeye karar verdim. Denemekle kalmadım hayata geçirdim ve MediaWiki üzerindeki tüm bilgileri Redmine üzerine alarak çalışır hale getirdim.

Aşağıdaki komut Redmine için gerekli olan MySQL'in çalışması için gerekli.

**Komut:**

```
docker run -d -name redminesql -v /data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=redmine mysql
```

**Parametreler:**

	-d : daemon olarak çalıştırır
	-name redminesql : container'ın adı belirleniyor.
	-v /data/mysql:/var/lib/mysql : mysql datasını host üzerinde başka bir lokasyona mount ediyor. Bunun yapılma sebebi olası bir migrasyon esnasında Redmine datalarını taşıyabilmek.
	-e MYSQL_ROOT_PASSWORD=secret : MySQL root şifresi Redmine için setleniyor.
	-e MYSQL_DATABASE=redmine : Redmine için veritabanı yaratılıyor.

Bu komut da Redmine'ı çalıştırmak için gerekli

**Komut:**

```
docker run -d --name myredmine -v /data/redmine:/usr/src/redmine/files -p 3000:3000 --link redminesql:mysql redmine
```

**Parametreler:**

	-d, -name, -v : Yukarıdaki aynı işleri yapıyor. Burada -v parametresi ile host'a mount edilen alanda Redmine üzerinde yapılan dokümantasyon esnasında yüklenen dosyalar var.
	-p 3000:3000 : Container'ın 3000 portunu, host'un 3000 portuna map ediyor.
  	--link redminesql:mysql : Container'ın mysql bağlantısını, redminesql Container'ına bağlıyor.

Bunları yaptıktan sonra yapmanız gereken http://<IP>:3000 portunu browser'ınıza yazmak. İlk admin ile login olduğunuzda "Default Configuration" ı yüklemeyi unutmayın, aksi takdirde bir çok özellik eksik oluyor.

Mail notifikasyon ile ilgili konu üzerinde çalışıyorum, başarır başarmaz onu da blog olarak yazacağım.
