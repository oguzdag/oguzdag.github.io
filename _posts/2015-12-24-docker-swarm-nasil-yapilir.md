---
layout: post
title: Docker Swarm nasıl yapılır ve nasıl test edilir?
published: true
categories: 
  - docker swarm
  - docker
  - carina
---

## Başlarken

Docker Swarm gerçekten çok çok çok önemli bir araç. Özellikle docker'ı kişisel bilgisayarınızdan çıkarmaya karar vermişseniz ve deneme aşamasından kullanma aşamasına geçmişseniz, bilmeniz gereken bir araç. Docker swarm, docker'ları bir harmoni içerisinde yönetmenizi ve container'larızı uygun docker'da konumlandırmanızı sağlayan önemli bir cluster aracı. Özellikle Docker'ın, bir development ortamından daha fazlası olduğunu, production için de bir alternatif olduğunu kanıtlıyor. Yakın zamanda [anons edildi](http://blog.docker.com/2015/11/swarm-1-0/), Docker Swarm 1.0 production ortamında kullanılabilecekti. Ve hatta [kapsamlı stress testi de yapıldı](https://blog.docker.com/2015/11/scale-testing-docker-swarm-30000-containers/). Sonuçlar o kadar umut verici ve adamlar o kadar kendilerine güveniyorlar ki, yazının sonuna şunun yazmışlar 

> "We’ll continue to test Swarm, pushing its limits and using the results to harden it." 

buram buram kendine güven kokuyor açıkçası.
