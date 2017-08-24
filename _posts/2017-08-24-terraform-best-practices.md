---
published: false
layout: post
title: Terraform geliştirme pratikleri
categories: 
  - terraform
---

## Giriş
Püffff... Acayip tozlanmış burası... Parmaklarım da paslanmış biraz. Ama bunun üstesinden gelmenin en kolay yolu, lafı hiç uzatmadan direk konuya girmek. Terraform konumuz, Terraform 3 yaşında henüz versiyon olarak 0.10.0 nasıl yepyeni dimi? Vee etrafta hiç Türkçe terraform blog yok. Yani en azından ben bulamadım, bilen duyan var ise insanlık namına paylaisın... Neyse ben bir blog yazayım bari. Etrafta o kadar örnek var ki ama hepsi çoğunlukta yazılıp bitirilmiş terraform projeleri, sonuç var ama gidiş yolu yazılmamış. Bu konuda biraz bilgilenmek gerektiğini düşünüyorum. Ayrıca bir de repom var bu terraform AWS işleri için.

## Terraform pratikleri
Açıkçası bu pratikler tek bir blogdan alınmadı çoğunlukla okuma araştırma uygulama ve sonunda ulaşılan sonuçlar. Hızlıca sıralayalım. Ama ana ilham kaynağım [https://charity.wtf/tag/terraform/](https://charity.wtf/tag/terraform/). Kızın biraz ağzı bozuk ama inanın yaşamış görmüş sistemci. 

### Tek bir tf dosyası mı? Canına mı susadın?
Evet tek bir tf dosyası ile çalışabilrisin, evet terraform buna izin veriyor, ama doğru bir yöntem mi? Diyelim ki koskoca bir network tasarladın, sonra security group'lar sonra NACL tanımları, role'ler, dur daha yeni başlıyoruz, AutoScaling Group, Launch Configuration vs. vs. Ne oldu o dosya? 1500 satır mı? 3000 mi? E hadi aradığını bul bakalım. Bunun yerine gruplama yöntemine git. Ayır mantıksal gruplara, ben ne yapıyorum? networking diyorum, içine network component'leri, roles_groups diyorum hoop içine 

