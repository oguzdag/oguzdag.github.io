---
published: true
layout: post
title: "Yeni bir Hudson Plugin'i - CI Game"
categories: 
  - jenkins
  - hudson
  - cigame
---

Bu plugin'i ilk gördüğüm zaman, yüzüme geniş bir gülümseme yayıldı. [CI Game](http://hudson.gotdns.com/wiki//display/HUDSON/The+Continuous+Integration+Game+plugin) ha, çok zekice :) açıkçası uzun süredir, bu tarz bir olay düşünüyordum.. Gerek yapılandırmaların sık sık bozulmasından, gerekse yapılandırmaları bozan insanları kafamda sürekli bir sıraya sokmaya çalışmak gibi bir psikopatlıktan dolayı, acaip hoşuma giden bir plugin oldu..

Tabi hiç zaman kaybetmeden, indirip Hudson'a entegre ettim.. Daha önceki yazılarımda bahsettiğim bir sürekli entegrasyon pratiği olan erken derleme işi için aktif hale getirdim. Çünkü elimde, SVN ilişkisini Hudson'ın kontrol ettiği (People listesinin doldurulması açısından) tek iş bu idi. Diğer işlerde şimdilik SVN bağlantısını, svn task'ları ile ant scriptleri götürüyor.

Oyunun mantığı çok basit, bu eklentiyi yüklediğiniz zaman, sol navigasyon barında **"Leader Board"** diye bir link ortaya çıkıyor.

![CIGame001.jpg]({{site.baseurl}}/images/CIGame001.jpg)

Bu linkte tıkladığınızda bir **"Skor Tahtası"** ile karşılaşıyorsunuz. Skor tahtasında developer'ların bir listesi var (Hudson'ın SVN commitlerine bağlı olarak oluşturduğu People listesinden üretiliyor), bu liste bir skorlama sonucu oluşturuluyor, skorlama ise çok basit :

- Sürüm bozan her developer -10 puan
- Bozuk bir sürümü istediğiniz kadar bozabilirsiniz 0 puan
- Hatasız çıkarılan her sürüm +1 puan
- Her başarısız yeni test -1 puan
- Her başarılı yeni test +1 puan

Buna göre liste oluşuyor.. Ve bu listeye bakarak, en azından bir fikir sahibi olabiliyorsunuz. Puan kazanmanın birçok yolundan birisi de, herkesin hemfikir olduğu sık sık commit yapılması, yani büyükçe bir değişiklik kümesini 3 gün üzerinde çalışıp, tek defada commitleyip, +1 puan almak yerine, bunu mantıklı 3 altkümeye bölüp hergün bir altkümeyi commitleyip, toplamda +3 puan almak sanırım daha lezzetli..

Sürekli Entegrasyon Sistemi'ni eğlenceli hale getirmek adına, çok güzel bir plugin...

