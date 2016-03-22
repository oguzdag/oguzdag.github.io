---
published: true
layout: post
title: Websphere Transaction Recovery
categories: 
  - websphere
  - transaction recovery
---

En gıcık konulardan birisidir Transaction Recovery konusu... Gıcık, gıcık, gıcık, gıcık... Ama bir o kadar da önemlidir... Websphere bugüne kadar kimseye muhtaç olmadan transaction'larını yönetmiş, yeri gelmiş onlara annelik yapmış, yeri gelmiş onlara babalık yapmıştır... Bir evlat olmuştur transaction'lar onun için... Fakat ani bir kaza geçirdiğinde transaction'lar panik olmuşlar ve ne yapacaklarını şaşırmışlardır... Bu hikayemizin konusu da, panik olan bu transaction'ların o an düşünebildikleri tek şey ile ilgili... Transaction Recovery...

**Nedir Transaction Recovery?**

Google translate açıyoruz ve "Transaction Recovery" kısmını oraya yapıştırıyor ve karşılığına bakıyoruz... "İşlem Kurtarma"... Bence gayet mantıklı bir çeviri... Evet tam herşey güllük gülistanlıkken ve Websphere umarsızca çalışırken, bir anda Websphere'a birşey olsa üzerindeki işlemler ne olacak? Devam edenler... Evet bunlar Recovery için bir yerlere yazılacak ve sonra birisinin gelip kendilerini kurtarmasını bekleyecek... İşte birilerinin gelip onları kurtarması işlemine Transaction Recovery deniyor...

**Kim Transaction Recovery yapar?**

Normal şartlar altında, hangi sunucu göçtü ise, o sunucu tam anlamıyla açıldıktan sonra Transaction Recovery yapar... Yani herhangi bir High Availability ayarı yapılmamışsa...

**Neden High Availability ayarı yapayım ki?**

Neden diye sormayı benim kızım da çok sever, "baba neden ipad kullanıyorsun?", "baba neden merdiven var?", "baba neden bıyıkların siyah?", yani çok ama çok alışığım ben neden sorusuna... Bu noktada High Availability neden var sorusuna da şu şekilde bir cevap vereyim... Diyelim ki in-flight işlemlerden bir tanesi veritabanına lock koydu ve websphere uygulama sunucusu göçtü, lock da veritabanında kaldı, kurtarma işlemi yapılana kadar veritabanındaki lock, bulunduğu yere ulaşmaya çalışanlara sıkıntı çıkaracaktır... Kurtarma işleminin de sunucu tam anlamıyla açılana kadar yapılmadığını biliyoruz. Bu durumda sunucunun açılmasını gecikterecek herhangi bir şey, veritabanındaki bu lock'ın sıkıntı yaratmaya devam etmesini sağlayacaktır. Bu durum hoş değildir. İşte High Availability ayarları yapılırsa, bu sunucunun açılışı beklenmeden recovery işlemi yapılıp sorun daha erken ve hızlı bir biçimde çözülebilir..

**Oooo iyiymiş, peki nasıl yapacağız bu işi??**

Hah bu sorular beni konuya iyice ısındırıyor... Anlatayım madem... Bu işlemin olabilmesi için elimizde bir cluster olmalı, uygulama sunucuları bu cluster'a dahil olmalı ve lease-based locking protocol'ü destekleyen bir ortak alana sahip olmalıyız.. NFSV4'ün lease-based locking protocol desteği var onu biliyorum... Bunlar elimizde ise, Cluster üzerinde ve uygulama sunucuları üzerinde aşağıdaki ayarları yapmamız yeterli. Sonrası Websphere'in işi..

Cluster üzerinde ;

```Servers > Clusters > WebSphere application server clusters > cluster_name
```
seçildikten sonra, Enable failover of transaction log recovery seçeneği işaretlenir.

Sunucu üzerinde ;

```Application servers > server_name > Compensation service
```

girildikten sonra, aşağıdaki seçenekler doldurulur

Enable service at server startup - enabled

Recovery log directory - Recovery loglarının duracağı ortak alan

Diğer alanları olduğu gibi bırakıyoruz.

**Son bir sözün var mı?**

Evet ben bu ayarları yakın zamanda yapmayı planlıyorum, yaptığımda çıkabilecek arızaları bu posta yazacağım. Yani anlayacağınız ben teoride doktorum, pratikte sadece hasta bakıcı...
