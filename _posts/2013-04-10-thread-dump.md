---
published: true
layout: post
title: Websphere Thread Dump Okuma
categories: 
  - websphere
  - thread dump
---

## Konuyla Alakasız Önyazı

Klasik **"uzun zamandır blog yazmayan blogger"** girişi yapmayacağım. **"Aman bir yazı ile buraların tozunu alayım"** da demeyeceğim. İnsanız yazarız, yazmayız, motivasyon meselesi, uzun süredir motive değildim. Ama olaylar öyle gerektirdi motive oldum, bu nedenle yazıyorum. Bu yazıyı yazmamda emeği geçen JVM'lere, fiziksel makinelere, ve Türkçe kaynak eksikliğine buradan selam olsun.

## Konuyla Alakalı Önyazı

Thread Dump inceleyebilmek, J2EE teknolojisi ile haşır neşir olan sistemciler için çok önemli bir konudur. Yeni sistemci arkadaşlara sürekli olarak belirttiğim **"Bir problemde desen (pattern) yakalama"** yeteneğini bileylemek ve Thread Dump incelerken kullanmak gerekir. Çünkü Thread Dump okumak, öyle roman okumaya benzemez, içinde çoğunlukla tonla gereksiz kısım vardır ve düzyazı şeklinde okunması kesinlikle sistemci sağlığına zararlıdır.  Günümüzde, son 10 yılda, Java kullanılarak yazılan uygulama sayılarında artış, orta katmanda tercihlerin J2EE olarak değişmesi, uygulama sunucusu kavramının daha ön plana çıkması gibi bir yığın sebepten dolayı Thread Dump incelemek artık bir ekstra değil, bir gereklilik olmuştur. Bu yazı da özü itibariyle Thread Dump'ları teknik olarak anlatmak yerine (bu işi JVM gurularına bırakıyorum) bu konuda sizi fikir sahibi yapmak, hatta bunun biraz ötesine götürüp bazı yerlerde **"hmmm bu adam da biliyormuş"** dedirtmek için yazılmıştır. Umarım faydalı olur.

## Thread Dump nedir?

Thread Dump bir JVM'in dump alındığı anda tüm Thread'lerinin ne durumda olduğunu gösteren bir bilgi kümesidir. Vendor'dan vendor'a değişen bir yapısı olmasına rağmen benim size burada anlatacağım kısımlar çoğunlukla ortaktır. Dolayısıyla endişe etmeyin... Neyse uzatmayalım.  Bilindiği üzere JVM üzerinde çalışan tüm işler yine JVM içerisinde bu işi için yaratılan türlü thread'lerde çalışırlar. Uygulamaya hizmet eden bu thread'ler JVM ile kernel'in işbirliği ile oluşturularlar. Yani her bir thread için Kernel'de de o JVM process'ine bağlı thread'ler oluşturulur. İşte bu Thread'ler, aralarındaki ilişkiler, JVM ile ilişkileri ile ilgili bilgileri içeren bu bilgi kümesine _Thread Dump_ denir.

## Thread Dump ne zaman gereklidir?

Bir yazılımcı tarafından yazılan tüm uygulamalar zaman zaman performans sıkıntıları yaşarlar, bu beraber yaşamak zorunda kaldığımız bir gerçekliktir. Ve bu tür durumlarda Sistemci tarihinin ilk gününden beri ileri gelen bir sistemci atasözü olmuş şu sözleri söyleriz. **"Tamam logları inceleyelim"** burada bizim için log Thread Dump olacaktır. Sorunun net analizi için Thread Dump almak çok faydalı olacaktır. Özellikle sıkıntıya kimin sebep olmuş olabileceğinin belirlenmesinde, veya sıkıntıdan hangi işlemlerin muzdarip olduğunu anlamamızda çok önemli bir kaynaktır Thread Dump. Çünkü sorun anında hangi thread'in ne iş yaptığını bize söylüyor, daha ne olsun.

## Thread Dump nasıl alınır?

Bu yazıda bahsedeceğim belki de tek linux komutu bu olacak, o kadar az teknik yani... Basit, process'e SIGQUIT sinyali göndereceksiniz.. Linux veya Unix de ```kill -3 PID```, Windows'ta çalışan JVM penceresine CTRL+BREAK yapmak yeterli

## Thread Dump alınırken neleri etkilerim?

Bu soruyu nasıl bu listeye aldım ben de bilmiyorum ama önemli olabilecek bir durum çünkü kimse Thread Dump alırken kimseyi veya hiçbirşeyi etkilemediğini iddia edemez...Thread Dump alınırken tüm thread'lere tek tek hangi durumda oldukları sorulur, ve bu sorguya cevap verebilmek için threadler işlerini durdurmak zorunda kalır. Saniyeler seviyesinde olsa da, işlem **"pause"** olur.

## Thread Dump dosyasını nerede bulabilirim?

Genelde aktar'larda bulabilirsiniz, veya Eminönü'nde Mısır Çarşısı'nda bulabilirsiniz.. Ya da cümleme aldırmaz ve ulan ne geyik adamsın söyle işte adam gibi diyebilirsiniz...

IBM Websphere için; profil klasörünün hemen altına atılır, yani /AppServer/profiles/Custom01 gibi. Hangi sunucu için alınıyorsa thread dump, bu sunucunun bağlı olduğu node'un profiline bakılmalı. Fakat eğer sunucu üzerinde bir environment variable ile LOG_ROOT değiştirilmişse, bu klasör kontrol edilmelidir.

JBoss için; bin klasörünün altına atıyordu yanlış hatırlamıyorsam.

Tomcat için; catalina.out dosyasının içine yazıyor, arkadaş diyor ki "catalina.out o kadar boş ki, doldurmalıyım  bunu, neyle neyle, hah thread dump istedi arkadaş, bunu yazayım bari"

## Thread Dump neleri içerir?

Thread Dump dosyası Thread'lerin durumlarını, hangi işlemi yaptıklarını, aralarında olan ilişkileri, JVM ile ilgili özet bilgi (min heap, max heap, JVM parametreleri, GC çıktıları) içerir.

Fakat en önemli içeriği, işlemlerin Stack Trace'leridir, bu biraz yazılımsal bir konu olsa da yazılım ekibi ile aynı dili konuşabilmek adına bir sistemcinin de bilmesi gereken bir ayrıntır. Ayrıca buradaki önemli ayrıntılardan birisi de Stack Trace'ler içerisinde metodun hangi satırında beklenildiği bilgisi de vardır ki bu yazılımcı için değerli bir donedir. Yani yazılımcıya, "Hey arkadaş, ne Thread Dump'lar gördüm, içinde Thread yoktular, ne Thread'ler gördüm, onları içeren bir Thread Dump'ları yoktular" dersek, yazılımcı doğal olarak bize gülecektir. Ama onun yerine "Hey arkadaş, thread dump'ı inceledim ve birçok thread'in senin A sınıfının B metodunda X satırında beklediğini gördüm, inceleyebilir misin?" dersek, yazılımcı içinden "İlginç, A sınıfımın B metodu olduğunu ve bu metodun X. satırda yer aldığını nereden biliyor, demek ki bildiği birşeyler var, ben en iyisi istediğini yapayım da inceleyeyim" diyecektir. Espri bir yana, yazılımcı ile aynı dili konuşabilen sistemci sorunları daha iyi aktarabilecektir. Bu da böyle biline... Devam edelim...

Tabi thread dump içerisindeki tüm thread'ler sizinle ilgili değildir. Hatta büyük bir kısmı JVM'in kendi işleri ve sistemsel düzenlemeleri sağlaması ile ilgili olabilir. Bu yazı adım adım bir thread dump incelemesi olmayacağı için burada tek tek detayları vermeyeceğim. Fakat uzun süredir Websphere ile çalıştığım için bir thread dump'ı incelerken sıklıkla baktığım yerleri paylaşacağım. Diğer tüm detayları IBM'in sayfalarında falan bulabilirsiniz. Ya da ne bileyim google'a yazın **"Thread Dump Detail"** çıkar muhakkak birşeyler.

## Thread Dump incelerken nelere bakılır?

Burada yaklaşık olarak 7 senedir Websphere kullandığımız için burada anlatacaklarım IBM Websphere'den alınmış Thread Dump için olacaktır. Hani başka bir thread dump'a bakıp da "lan nerede bu adamın dediği" deyip sonra da "anaaa sallamış lan, yok öyle birşey" demeyin... Var, sadece benim baktığım thread dump değişiklik gösterebilir. Neyse tekrar devam edelim. Dediğim gibi önemli gördüğüm yerleri yazacağım, IBM thread dump'da her satır ne iş yapar zaten sitelerinde yazıyor. Ben de biliyorum çoğunu ama anlatmak gerekli değil.

### 1. Thread Dump neden alınmış?

```
1TISIGINFO     Dump Event "user" (00004000) received 
```
Thread dump içerisinde bu satır dump'ın neden atıldığını gösterir. Benim örneğim "user", yani "ben yaptım", ama bu eğer OutOfMemory olsaydı, OutOfMemory olacaktı.

### 2. OutOfMemory durumu mu var?


```
0SECTION       MEMINFO subcomponent dump routine
NULL           =================================
1STHEAPFREE    Bytes of Heap Space Free: 1bee0198 
1STHEAPALLOC   Bytes of Heap Space Allocated: 40000000
```
Bu kısım hexadecimal, yani bunu decimal'a çevirirseniz, max heap ve boş miktarı görebilirsiniz. Bu da faydalı bir bilgidir. Bazen OutOfMemory heap'in farklı bölümlerinde gerçekleşebilir, yani native memory'de verebilir, permanent space de, dolayısıyla JVM heap de mi yoksa, başka bir yerde mi anlamak için iyi bir nokta burası.

### 3. Sonra nereye bakacağız?

```
1XMTHDINFO     All Thread Details
```
Ta-tam.. Asıl bakılması gereken yer burası, thread'lerim ne iş yapıyor? Thread Dump içerisinde yukarıdaki ifadeyi arayın, sonrasında aşağıda doğru scroll etmeye başlayın. Çünkü tüm Thread bilgileri bundan sonrasında yer alıyor. Buradan sonra tamamiyle deneyiminizle hareket etmeniz gerekiyor. Ne kadar çok sıkıntıda Thread Dump incelerseniz, o kadar tecrübe kazanır ve o kadar "Desen" yakalarsınız... Ama yine ufak bir tüyo, standard bir J2EE uygulaması kullanıyorsanız "WebContainer" threadlerine bakmanızda fayda var. Aynı tür thread'lerin hepsinin beklediği ortak bir kaynak var mı bu da bakılabilecek ayrı bir konudur.

## **Thread Dump okuma ile ilgili faydalı araçlar**

Burada yine IBM'in ürünü olan IBM Thread Dump Analyzer kullanabilirsiniz, Thread Dump'ı okumak istiyorsanız, okutabilirsiniz. Ayrıca 5'er dakika ara ile alınan 4-5 Thread Dump dosyasını Thread Dump Analyzer ile açarak, thread'lerde oluşan değişiklikleri falan görebilirsiniz...

## Son Söz

Söyleyebileceğim tek son söz, aslında bu blogda bir son söz olmayacağı, burada yazdıklarım yaklaşık yarım günümü aldı, çok fazla araştırma yapmadım açıkçası, yani yanlışlar muhakkak ki çıkacaktır, o nedenle sıklıkla revize edebilirim... Edersem de bunu muhakkak bir yerlerde belirtirim... Yani okuyup kaçmayın, yanlışlık varsa yorumlayın düzeltelim...
