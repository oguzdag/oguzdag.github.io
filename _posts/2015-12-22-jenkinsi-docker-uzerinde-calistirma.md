---
layout: post
title: Jenkinsi Docker Üzerinde Çalıştırma
published: true
---

## Başlarken

Uzun süredir blog yazarım, ve daima blogların insanı sıkmaması taraftarıyımdır. Ben de o tarzda blog yazmaya karar verdim. Madem blog'un adı **Teknoloji Mutfağı**, o halde her tür implementasyonda bu mutfakta pişmiş bir yemek oluyor.

İlk yazı olarak [Docker](https://hub.docker.com/) ve [Jenkins](https://jenkins-ci.org/) olacak içeriğinde. Böylece hem Docker'a, hem de Jenkins'e giriş yapmış olacağım. Açıkçası yıllardır Jenkins kullanıyorum, taa Hudson'dan beri , Docker ile de bu yakınlarda tanıştım. Aslında docker ile tanışmam bir başka open source uygulamayı en hafif ve laptop'uma en az kurulum ile nasıl hayata geçiririm derken buldum. Daha önce bir arkadaşım bahsetmişti ama bu kadar hoşuma gideceğini zannetmiyordum. Docker ile ilgili ileride çok daha açıklayıcı yazılar yazacağım, bu seferlik sadece Jenkins'i en hızlı ve en kurulumsuz şekilde nasıl ayağa kaldırıyoruz onu anlatacağım.

## Malzemeler

* 190 MB Docker Toolbox v1.9.1f (https://www.docker.com/docker-toolbox)
* 708 MB Jenkins ver.1.625.3
* Alabildiği kadar İşletim Sistemi Windows 8.1 

## Yapılışı

Malzemelerimizden Docker Toolbox'ı, hemen yanında bulunan linkten indirip kuruyoruz. Kurulum tamamlandıktan sonra Docker QuickStart Terminal'ı çalıştırıyoruz. Bu bize bir komut satırı ekranı açıyor, sürpriiiiiz, Docker dediğimiz bir komut satırı arayüzü, bir client yani. Yapmamız gereken [dockerhub](https://hub.docker.com/)'dan istediğimiz projeyi almak ve ardından çalıştırmak.

Komut şekli basit

> docker - komut - container

Komut satırı basit `docker pull jenkins` ile jenkins docker imajının son halini lokalimize alıyoruz.
