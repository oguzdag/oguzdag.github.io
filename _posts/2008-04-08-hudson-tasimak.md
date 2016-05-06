---
published: true
layout: post
title: "Hudson'ı taşımak"
categories: 
  - hudson
  - jenkins
---

Sürüm Sistemi'nizi (benim durumumda bu [Hudson](http://hudson.dev.java.net/) oluyor), daima sistemlerinizden ayrı bir makine üzerinde yürütmelisiniz. Yani, Hudson'ın kurulu olduğu makine üzerinde Uygulama Sunucusu (eğer kullanıyorsanız) veya veritabanı olmamalıdır. Neden? Çünkü eğer ağır, CPU tüketen testler çalıştırıyorsanız ve bu testleriniz uzun sürüyor ise bu makine üzerinde darboğazlar oluşmaya başlar, böylece siz **"kaş yaparken göz çıkarmış"** olursunuz. Ya da bir anda memory yetersizliğinden dolayı makine kasılmaya başlar ve sistemde hizmet veremez hale gelirsiniz.

Kısacası, bu tür risklerden kurtulmak adına Hudson'ı ayrı bir makine üzerinde yürütmelisiniz.

Hali hazırda Hudson'ı farklı bir makinede çalıştırıyorsanız, bu yazının devamını sadece Hudson'ı nasıl yedekleyebileceğinizi öğrenmek için de olsa okuyabilirsiniz.

Eğer Hudson'ı bizim gibi ortamlarınızdan birisi ile içiçe kullanıyorsanız, aşağıdakileri sırasıyla uygulayarak migrasyonu tamamlamış olursunuz.

## 1 - Çevresel klasör ve dosyaların arşivlenip aktarılması

İlk yapılması gereken işlem, aşağıda listede olan (benim aklıma gelenler bunlar, unuttuğum var ise lütfen ekleyin) dosya ve klasörleri arşivlemektir ve yeni Sürüm Makinesi üzerinde açmaktır.

- Yapılandırma Scriptleri
- Artefaktlar (JAR, SQL, XML, HTML)
- Yerel Repository (Yapılandırma Scriptlerinizde kullanıyorsanız) 
- ANT, Maven, PMD, SVNKit, JDK, Tomcat gibi araçlar (Şükür ki unzip yeterli)

##2 - HUDSON_HOME klasörünün arşivlenip aktarılması

[Versioning a Hudson job configuration](http://www.testearly.com/2008/03/24/versioning-a-hudson-job-configuration/) isimli yazıda Hudson'ın hangi kısımlarını yedeklemenizin yeterli olacağı, olası bir felaket anında nelere dikkat etmeniz gerektiği yazılı... Özellikle bu tür yedeklerin Repository'de tutulmasının çok faydalı olacağı da ayrıca belirtilmiş.

Eğer Hudson'ı uzun bir zamandır kullanıyorsanız (mesela 2 yıl), bir hayli birikmiş yapılandırma geçmişi ve çalışma alanı dosyalarınız olacaktır. Bunların kapladığı yer ise repository'nize bağlı olarak gigabyte'ları bulabilir.. Fakat, bir acil durum anında, veya bir migrasyon sonrasında büyük ihtimalle bu dosyalara ihtiyacınız olmayacak, dolayısıyla yukarıda linkini verdiğim yazıda da belirtildiği gibi aşağıdaki komut Hudson'ın tüm konfigürasyonunu "workspace" ve "builds" olmaksızın tek bir dosyaya yedekleyecek, ve benim örneğimdeki gibi, sıkıştırılmış dosyanızın boyutu 700 MB'dan 25 MB'a inecektir.

> tar --create --gzip --file=hudson.tgz --exclude='workspace/*' --exclude='builds/*' .hudson/

Bu dosyanızı yeni Sürüm Makinesinde açmanız yeterli olacaktır.

##3 - Ortam Değişkenlerinin Düzenlenmesi

Dosyaların taşınması işleminden sonra karşılaşabileceğiniz ilk sorun Ortam Değişkenleri'nin bulunumaması olacaktır. Dolayısıyla konfigürasyon dosyalarında veya profil dosyalarında bu değişkenleri bulup düzenlemeniz gerekecektir (Mesela Tomcat kullanıyorsanız, JAVA_HOME değişkeni büyük olasılıkla catalina.sh içerisindedir, ya da HUDSON_HOME değişkeni .profile dosyasına yazılır, veya Tomcat içerisinde webapp altında war dosyası içerisinde web.xml'de belirtilmiştir. Daha detaylı bilgi için [tıklayınız](http://hudson.gotdns.com/wiki/display/HUDSON/Administering+Hudson)). Aşağıda önem sırasına göre ortamınızda değiştirmeniz gerekebilecek değişkenleri listelemeye çalıştım, unuttuğum olabilir, eklerseniz sevinirim.

- HUDSON_HOME (Önemli)
- JAVA_HOME
- ANT_HOME
- MAVEN_HOME

##4 - Hudson Pluginlerinin Yüklenmesi Sorunu

Benim yaşadığım ufak bir problem ve çözümü ile Hudson'ı başarılı bir şekilde çalışır hale getirebilirsiniz. Hudson'ın başlangıcı esnasında aşağıdaki gibi bir hata alırsanız

```
    SEVERE: Failed to load a plug-in jabber
    hudson.util.IOException2: Failed to initialize
    at hudson.PluginWrapper.load(PluginWrapper.java:253)
    at hudson.PluginManager.(PluginManager.java:90)
    at hudson.model.Hudson.(Hudson.java:332)
    at hudson.WebAppMain$2.run(WebAppMain.java:155)
    Caused by: java.lang.NoClassDefFoundError: hudson/plugins/jabber/im/IMMessageTargetConversionException
    at hudson.plugins.jabber.im.transport.JabberPluginImpl.start(JabberPluginImpl.java:23)
    at hudson.PluginWrapper.load(PluginWrapper.java:250)
    ... 3 more
```

Yapmanız gereken, [HUDSON_HOME]/plugins dizininde daha önce yüklediğiniz pluginlerin oluşturduğu dizinleri silmektir. Sadece hpi uzantılı dosyaları bırakmanız yeterli.

##5 - Doğru JDK kurulması

Mevcut Sürüm Sistemi makinesi ile yeni kullanacağınız Sürüm Sistemi makinesinin işlemci, işletim sistemi ve bunun gibi bazı farklarından dolayı aynı JDK'yı kullanamayabilirsiniz, bu nedenle yeni Sürüm Sistemi makineniz için doğru olan JDK'yı indirip ayarlamayı unutmayın.

##6 - Locale ayarlarının düzenlenmesi

Eğer yeni Sürüm Makineniz, hakikaten yeni kurulmuş ise, çok büyük ihtimalle dil ayarları (locale) yapılmamış olacaktır. Bu nedenle taşımanız gereken ayarlardan bir tanesi de dil ayarları olacaktır.

##7 - Sürüm numaralarının düzenlenmesi

Eğer geçmiş yapılandırmaları tamamen temizleyip, bembeyaz bir sayfa açmak istiyorsanız, sürüm numaralarını da sıfırlamanız gerekiyor. Yapmanız gereken [HUDSON_HOME]/jobs klasöründe ilgili işin içerisine girip nextBuildNumber dosyasının içeriğini 0(sıfır) yapmak...

##Son Söz

Yukarıda belirtilen işlemlerin dışında Sürüm Sisteminize özel bazı yüklemeler yapmanız gerekebilir. Benim yaptığım migrasyonda SVN Client kurulumu bu tür bir yükleme idi..

Bunların sonunda, şu an Sürüm Sistemini 4 CPU ve 8 GB bir makine üzerinde taşıdım, ileride birim, kabul ve entegrasyon testleri de devreye girdiğinde bu makine tüm bu işleri kaldırabilecek güçte olacaktır. Bunun rahatlığıyla artık kodlar üzerinde yapılabilecek diğer işlemlere başlayabilirim.

