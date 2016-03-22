---
published: true
layout: post
title: "Sürekli Entegrasyon Pratikleri - II"
categories: 
  - sürekli entegrasyon
  - jenkins
  - hudson
  - private build
---

Sürekli entegrasyon sistemleri ile ilgili kazanımlarımı ve uygulamalarımı bu ikinci bölümde anlatmaya devam ediyorum. Serinin birinci bölümünü bu linkte bulabilirsiniz.

Bu yazıda size bir adet pratik anlatacağım ve bir adet de tavsiyede bulunacağım. Önce pratik,

**Pratik - SCM Kontrolü Mekanizmasını kullanarak kodların erken derlenmesini sağlayın**

Benimde yaklaşık olarak bir aydır uyguladığım bir pratik. Özellikle, belirli saatlerde çıkardığınız sürümlerde kodlara bağlı olarak derleme hataları ile karşılaşıyorsanız, ve her seferinde (sabırla) developer'ları arayıp, onlara kodların neresinde hata olduğunu, neyi düzeltmesi gerektiğini anlatıyor ve kodlarını SCM sistemine yeniden eklemelerini istiyorsanız. Tam size göre bir pratiği anlatacağım.

Tabi bu konuyu anlatmadan önce şunu belirtmeliyim, bu pratiğin bir diğer yöntemi (aslına bakarsanız, önerileni) lokal yapılandırmalardır.

**Nedir lokal yapılandırma (private build)?**

Developer kodlarını commit'lemek istediğinde, lokalinde bir yapılandırma çalışır, kodların bağımlılıklarına bağlı olarak bazı modülleri (veya uzatmadan hepsini) check-out eder, ardından derleme ve birim testi işlemlerini çalıştırır, ve eğer herhangi bir hata ile karşılaşılmazsa kodların commit edilmesine izin verilir.

**Neden lokal yapılandırma yerine erken-derleme pratiğini tercih ettim?**

Sebebi çok açık, bu tür yaklaşımlar (private build gibi), developer'ların bazı davranış biçimine (çevik geliştirme) sahip olmasını gerektirir. Benim bulunduğum ekipte bu tür bir yapıyı kurmak şimdilik zor olacağından, bu sistemi ileri bir tarihe erteleyip, bunun yerine sunucu tarafında çalışıp derleme ve test işlemlerinde oluşabilecek bir hatayı erken bulan bir sistem olan erken-derlemeyi tercih ettim.

**Dezavantajı yok mu bunun?**

Var, aslına bakarsanız kesinlikle büyük bir dezavantajı var. SVN'e bozuk kod gönderilmesi, her ne kadar erken uyarı sistemi ile developer'lar uyarılsa da, diğer bağlı modüllerin, bu bozuk kodu check-out etmesine ve sonra belki de saatlerce sorun ile uğraşmasına sebep olacaktır. Yani, ne olursa olsun **BOZUK (BROKEN) KODU COMMIT'LEMEYİN**...

**Eee uzatma da, nasıl yapılacağız onu anlat**

Hudson (favorim) kullanarak nasıl yapılabileceğini kısaca anlatacağım.

- Öncelikle, sürüm scriptlerinizden kodları derleyen (varsa, birim testlerini yapan) kısmı çıkarıp, ayrı bir dosya olarak kaydedin, unutmayın bunların dışındakileri yapmanıza gerek olmayabilir. 
- Sonra Hudson üzerinde yeni bir iş yaratın, ve bu dosyayı bu iş ile ilişkilendirin. İşin güzel yanı, check-out işlemini Hudson'a bırakacağız, SCM kontrolünü devreye alarak..
- SCM kontrolünü isteğe bağlı olarak saatte bir, veya yarım saatte bir olarak ayarlayın...
- Ve son olarak da bozuk yapılandırmalarda commit işlemini gerçekleşteren developer'lara e-posta atma seçeneğini işaretleyin. 

Ve bu kadar, artık Hudson yarım veya bir saatte, belirttiğiniz SCM yolunu kontrol edecek, herhangi bir değişiklikte yapılandırmayı çalıştıracak ve başarısız olduğu durumda e-posta aracılığı ile bilgilendirme yapacaktır... Erken uyarı sistemimiz artık çalışıyor.

**Var mı yaşadığın güzel bir örnek?**

Evet, bu blogu yazmadan birkaç saat evvel, bir toplantıdaydım, toplantıdan çıkıp yerime geçtim, e-postalarımı kontrol ederken Build failed in Hudson: XXXXX #14 konulu bir e-posta gördüm, sadece bana değil birkaç developer arkadaşıma da atılmıştı (erken-derleme ile ilgili Hudson üzerinde oluşturduğum işin otomatik attığı e-posta). Tabi bir saat olmuştu geleli.. Sonra e-postanın içerisinde ismi geçen developer'ları aradım, acaba bu bilgilendirme ellerine ulaştımı diye, haberimiz var, zaten düzeltip gönderdik dediler. Bunun bana nasıl bir haz verdiğini size anlatamam. Ben olmadığım durumda sistem çalışıp, insanları uyarmıştı... Sanırım sistem artık bir sürekli entegrasyon sistemi oluyordu.

**Tavsiye - Öğrenmeyi kolaylaştıran ve güzelleştiren bir yöntem önerebilirim..**

Öğretin, en azından öğretmeye çalışın.

[İbrahim'in bu linkteki blogu](http://www.ibrahimdemir.org/index.php/2008/03/16/sirket-ici-egitimin-onemi/)nu okumanız herşeyi anlatabilir. Öğrenirken, öğretmeye çalışarak, kendisini pekiştiriyor.
