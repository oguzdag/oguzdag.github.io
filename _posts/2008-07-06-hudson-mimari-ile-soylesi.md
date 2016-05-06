---
published: true
layout: post
title: "Hudson'ın mimarı ile bir söyleşi"
categories: 
  - hudson
  - jenkins
---

Bir hayli uzun zamandır bloguma herhangi bir şey yazamıyordum.. Araya yaz tatilim, IBM Websphere ile ilgili performans problemleri ve tuning işlemleri girince bu kadar uzun bir ara vermek zorunda kaldım... Ben de blog yazılarıma bu şekilde bir söyleşi ile döneyim dedim...

[Kohsuke Kawaguchi](http://www.kohsuke.org/)'ye, [Hudson](http://hudson.dev.java.net/) projesini ortaya çıkaran, ve şu anda tam zamanlı olarak bu işe vaktini ayıran kişiye, Hudson hakkında aklıma gelen bazı soruları sorma fırsatı buldum.. [J1](http://java.sun.com/javaone/sf/) sırasında bu soruları sormuştum, Hudson ve yürüttüğü diğer Sun projeleri ile ilgili J1'de görevli olduğu için biraz rötarlı olarak cevap verdi, ben de bu soru ve cevapları orijinal hali ile (ingilizce olarak) aşağıda sizlerle paylaşmak istedim... Cevapları okudukça açık kaynak projelerde izlenmesi gereken tavrı ve bir açık kaynak projesi etrafında oluşan atmosferi daha yakından anlayabileceksiniz... Çok içten ve yeterli (baştan savma değil) cevaplar beni yeterince memnun etti... Sorular ve cevaplar hakkında yorumlarınızı bekliyorum...

İşte Koshuke'ye yönelttiğim sorular ve cevapları

**Question 1 - Who is Kohsuke Kawaguchi, can you briefly give some information?**

**Answer -**OK, I'm a software engineer working for Sun Microsystems. Lately I'm spending more and more time on Hudson, but before that, I was (and am) in a part of Sun that does JavaEE, and I've been mostly working on XML. So I've been involved in technologies like JAXP, JAXB, and JAX-WS, and their implementations.

I'm originally from Japan, and in the United Status for 7 years now. At home, I have a 3-year old daughter who deprives me of my programming time.

**Question 2 - Where did this Hudson idea came from? We know you think the name "Hudson" to serve you as servant. But why did you need another Continuous Integration Server?**

**Anwer -**It started when I was working on the JAXB RI. At that time we had 3 people (including me) who's working on the code, and we are all busy checking in changes every day, but I'm very bad at making sure all my changes are committed. So from time to time, my colleagues discovered that they can't build the RI after they update from the CVS repository.

So I started developing some shell scripts, which essentially does what my colleages do (pull from CVS, do a build), but do it much more frequently. So I can be notified by that program before my colleagues catch that problem.

I also wanted to implement some web application, because I work in the JavaEE group and we do servers! I was not very happy with the webtier technology, and I thought I had a better idea. So another motivation was to try out my idea for real, to see if it works. This became Stapler eventually.

And so I was thinking about how to turn this little app into a webapp, and I was greatly inspired by now deceased CI application called "Damage Control." So I started mimicking its UI, but by using Java and Stapler.

**Question 3 - Wakaleo consulting is running a poll about CIServers in this link, Hudson at the top, what do you think about this, this poll reflects the recent usage of CIServers? (BTW, I voted for Hudson)**

**Answer -**You have to take any poll with a grain of salt, but seeing more adoption is a motivator for any open-source developer, I think.

In any case, I try not to worry too much about those polls. It's more fun to think about features to implement, and making people happy by fixing bugs quickly. Adoption should follow if I do a good job.

**Question 4 - In Nabble Forums, you are replying every post, on your own. Is this task, a little bit hard to maintain?**

**Answer -**But for me, interacting with users directly is very important. First, it's a motivator --- open-source development is just like any other volunteer effort. We do this because we want to see happy faces, and in our context that means helping people through e-mails.

Another reason it's important is often it gives me insights about where are rough edges. If you see multiple people making the same mistake, that means your software is wrong, not them. The only way to get a good sense of where they are is to do the user support yourself.

**Question 5 - What do you think about the community around Hudson, how many committers do you have (not bug reporters)?, translators are one of them?**

**Answer -**According to Ohloh, I have 69 contributers. This includes people doing translations and plugin developments.

One thing I'm trying with Hudson is a different way of running a community. Traditionally in open-source community, the bar for a commit access is rather high. You have to start by sending in patches, helping users, and do those things for a long time, while anxiously waiting for the day you are offered a commit access.

That makes sense for high-profile projects like Linux kernel, where there are tons of wanna-be developers that you have to chase away by a stick, but for most of open-source projects that are small, that's completely wrong trade off.

Most of the time, we struggle to get even one more committers. If you can even get one guy who's potentially interested in helping the development, you should be very happy. Having a high bar to contribution is only going to discourage that. That's not what you want.

So in Hudson, we give away commit access very liberally, which is reflected in a larger number of committers. The plugin system really works well here, because it eliminates a part of the reasons why there's such a high bar to the entry; namely, to make sure people you'll have to work with are nice people.

So far I think this model is going well.

**Question 6 - What do Sun think about Hudson? because you are an employee of SunMicrosystems? And I don't think that Sun didn't notice Hudson.**

**Answer -**We are talking to various people internally at Sun to figure out how it fits with our broader strategy. So stay tuned for more on this in the future.

And lots of Sun projects are built and tested on Sun. So in a sense it's already used widely as one of the tools.

**Question 7 - What is the maturity of Hudson in your viewpoint? I mean Hudson now can compete with CruiseControl, but is it enough to say Hudson is mature enough?**

**Answer -**It's hard to think of software as maturity. I think there's no question that it's quite usable --- otherwise not so many people would be using it. But there are a lot of issues and RFEs filed, so there's no doubt that there are more work ahead.

I think that's one thing I really like about the tool development; IMO, there's really no such thing as "mature enough" in tools. There are nearly infinite room of improvements in any front, and it's fun to make a tool better.

I still have a lot of feature ideas and I do hope to implement them in time.

**Question 8 -What is the chance of Hudson, against some proprietary CIServers such as Bamboo, BuildForge, AntHill?**

**Answer -**I think Hudson already marginalized several commercial offerings. Even if you are charging for a product and spending that money to hire developers and/or designers, that alone is not a sufficient recipe for successful software.

In a long run, I think an open-source project prevails, especially in the tools market. For example, GCC dominates the C compiler market. Subversion and CVS dominates the VCS market. It's very hard to compete with the eco-system of an open-source software development, and we are starting to see some commercial interests around the development of Hudson.

So I think Hudson is so far on the right track for the world domination. We'll just have to keep working hard.

**Question 9 - What is the distribution of Hudson usage all over the world? Do you have any reference list?**

**Answer -**Hudson tends to be run behind a firewall, so it's very hard to accurately know who's using. But judging from Ohloh and time of the day when people send in e-mails, there is a large adoption in Europe and the U.S.

I think additional translation would help us reach broader audience. Being from Japan, I know that the localization makes a real difference in some regions.
