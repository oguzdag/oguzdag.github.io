---
published: true
layout: post
title: Websphere FFDC Logları
categories: 
  - websphere
  - ffdc
---

FFDC logları Websphere'in uyarı sistemleri arasında önemli sayılabilecek bir yerdedir. Peki nedir FFDC? Ne anlama gelir? Nasıl kullanılır?

**Nedir FFDC?**

FFDC, "First Failure Data Capture" ifadesinin baş harflerinden oluşur. Anlamı ise, sorun ilk oluştuğu anda gerekli verileri topla demektir. Türkçesi İHVT yani, "İlk Hatada Veriyi Topla", güzel uydurulmuş bir sözcükler öbeği, mangalda kızartılmış bir hellim gibidir, muhakkak ki keyifle yenmelidir. Tamam uydurma güzel olmadı, bundan sonra da FFDC diye devam edelim madem.

**FFDC mi IBM içindir? IBM mi FFDC için?**

FFDC kimin için tasarlanmıştır sorusunun cevabı ise kesinlikle Developer değildir. FFDC logları IBM labında gecesini gündüzüne katıp, deliler gibi önündeki PMR'ları çalışan o güzel yüzlü, iyi niyetli IBM insanları içindir. Her ne kadar çok fazla PMR çözebilme özellikleri olmasa da (kişisel deneyimlerimden dolayı böyle söylüyorum, allah için kişilik olarak hiç bir zararlarını görmedim) bu FFDC'lere bakarak sorunun ilk oluştuğu anı ve gerekli çevresel bilgileri buradan çıkarırlar.

**FFDC Server'ımı göçertti**

Yalan, vallahi yalan, yok öyle birşey, FFDC'nin Uygulama sunucusuna getirdiği herhangi bir performans etkisi yoktur. Yani getirse getirse, tahtıravallinin bir tarafında oturan 13 kiloluk 3 yaşında bir kız çocuğuna, karşı tarafa konmuş bir sinek kadar getirir... Ne güzel canlandı değil mi kafanızda?

**Hadi şu FFDC'leri yönetelim**

İkinci kez bir paragrafa olumsuz bir cümle ile başlama kusurunu işliyorum, fakat bunu da yapamazsınız, FFDC loglama olayını yöneteceğiniz herhangi bir Admin özelliği bulunmuyor. Ne kötü değil mi? Kimbilir Websphere 15 de olur (Bu arada ben hala Websphere 8.5 olayını anlayabilmiş değilim, arkadaş ne oldu 8.1,8.2,8.3 ve 8.4'e, ya bırakın açıklama yapmayın)

Kısacası FFDC önemlidir, türkçeye çevirilmesi gaflettir, olduğu gibi bırakılmalıdır.. Okunmalı ve IBM insanlarına okumaları için gönderilmelidir... Haa bir de performans etkisi yoktur.


