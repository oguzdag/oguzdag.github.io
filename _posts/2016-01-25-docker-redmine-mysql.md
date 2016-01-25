---
layout: post
title: Docker üzerinde Redmine kurulumu ve dikkat edilmesi gerekenler
published: false
categories: 
  - docker
  - redmine
  - mysql
---

Her ne kadar kurumsal bir ortamda çalışsam da, daima bilginin paylaşılabilir olması gerektiğine inananlardanım. **"Kurumsal ortamda paylaşım olmaz mı?"** diye sorabilirsiniz. Lafı uzatmadan şunu söyleyebilirim, **"Hayır olmaz!"**. Gerçekten olmaz, kurumsal ortamda birbirine bilgi aktarmak diye birşey yoktur, fakat başkasının bilgisi ile prim yapmak çok revaçta bir konudur. Bu etik olmayan davranış şekilleri tamamen farklı bir bilim dalının konusu dolayısıyla çok fazla karıştırmayacağım. 

Konuya dönelim, ben paylaşımı severim, bilgimi daima paylaşmışımdır. İlk önce [Twiki](http://twiki.org/) ile başlamıştım bu paylaşımı yaygınlaştırma olayına. Eski blogumda da bununla ilgili [Dokümantasyon ve Twiki - I](http://ozidethonjava.blogspot.com.tr/2007/09/dokmantasyon-ve-twiki-i-dokmantasyon.html) ve [Dokümantasyon ve Twiki - II](http://ozidethonjava.blogspot.com.tr/2007/09/dokmantasyon-ve-twiki-ii-twiki.html) yazıları bu konularda az çok bilgi veriyor. Twiki implementasyonu zor bir Wiki idi. Kısa zaman sonra bunun yerine [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)yi koydum. 2009'da idi sanırım. Bir hayli doküman birikti bunun üzerinde. Neredeyse tüm operasyonlarımızı, tüm sorunlarımızı, tüm şemalarımızı, tüm dokümanlarımızı buraya kaydettik. Artık yanımda çalışan arkadaşların ayrılmaları sancı yaratmıyordu. Hatta yeni gelen arkadaşlara, **al şu wiki'den oku** demek o kadar keyifli idi ki. Gözlerindeki **"Kurumsal yerlerde Wiki'nin ne işi var?"** ifadesini görmelisiniz.

