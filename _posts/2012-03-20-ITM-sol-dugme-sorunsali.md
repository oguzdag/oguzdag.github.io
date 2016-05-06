---
published: true
layout: post
title: ITM sol düğme sorunsalı
categories: 
  - ITM
---


Ooooo, bir hayli zaman olmuş, teknoloji veya sorunlara dair birşeyler karalamayalı... Geçenlerde kendi kendime söyleniyordum, şöyle kendi kendime çözebildiğim bir problem olsa da buralarda paylaşsam, hayrım dokunsa birilerine diye, nihayetinde bu tarz bir durum oluştu ve ben de burada paylaşayım dedim, çünkü herhangi bir şekilde bu sorunun Türkçe'si yok, ya da ben kısıtlı arama yeteneklerimle bulamadım...


Sorunumuz ITM (IBM Tivoli Monitoring) ürününde oluyor... Şu anda deneme aşamasında ITM 6.2.2 FP2 kullanıyoruz, ileride bu bilgiyi kullanacağım da ondan yazıyorum...


Neyse olay şöyle gelişiyor güzel güzel Query'lerden View'lar yaratıp, ardından bunu grafiklere çeviriyorsunuz, ardından Workspace'i kaydedip güzelce diğer Workspace'lerde dolaşıyorsunuz, sonra geri dönüp bir bakıyorsunuz ki Workspace'inizde o güzelim View'ların yerinde yeller esiyor... Yerine iğrenç bir buton "sol düğme" veya bir diğer iğrenç buton "sağ düğme" (Figür 1), bir de bu iki cibilliyetsiz butonun sağında, solunda, altında, üstünde bunu kapatabileceğiniz, düzenleyebileceğiniz bir opsiyon yok... Çaaaat, kaldınız o şekilde, yapılacak tek şey Workspace'i silip ardından yeniden yapmak...

![ss001.JPG]({{site.baseurl}}/images/ss001.JPG)


Ama adamlar (IBM) zaten bunu bulmuş da henüz biz Türkler buna dair birşey yapmamışız anlaşılan... Belki bulan vardır ama ben bulamayanlar için burada paylaşayım...

[Left / Right buttons are seen in the Workspaces of the TEMA agent.](http://www-01.ibm.com/support/docview.wss?uid=swg21431517)

Bu linkte çözümü anlatmış, fakat en sonuna da eklemişler, APAR IZ73237 ile çözdüğümüz kesindir diye

[IZ73237: MIXED AND LOWERCASE XML IN /CQ/SQLLIB FOR TEP AND TEPS SUPPORT FILES](http://www-01.ibm.com/support/docview.wss?uid=swg1IZ73237)

Yani aslında cevaba bir FP kadar yakınmışım da haberim yokmuş...

Neyse, öncelikle çözümü deneyeceğim, çünkü planımda ITM 6.2.3'e geçme var, ve bu FP bana çok mantıklı gelmiyor, sonuçları burada yazarım artık...

**Düzenleme :** 6.2.2 versiyonuna FP7 uyguladım ama sorun devam etti. Ayrıca, workaround'da anlatıldığı gibi kynpackage.xml dosyasının varyasyonları da verilen klasörde bulunmuyor. PMR açtık bakalım, çözümlerini deneyeceğiz.

**Düzenleme 2 :** Sıkıntının sebebi, plot-chart yapıldıktan sonra bunun duplicate edilmesi ile ilgili, yani temiz temiz workspace'ler yaparsanız hiçbir sıkıntı kalmıyor...
