# Güvenlik Otomasyonu Video Serisi - 2
 ## Selenium - Python ile Web Arayüz Otomasyonu (API ve SOAR yok!), Örnek Senaryo
 
Bu bölümümüzde, hem API'ları, hem de SOAR gibi bir otomasyon platformu olmayan basit bir ortamda, iki farklı güvenlik ürününü nasıl birbiri ile konuşturabileceğimizi ele alıyoruz. Müşterimiz Firewall'unda engellenen IP adreslerini, Endpoint Security ürününde de engellemek isterse, API kullanmadan bunu nasıl yapabiliriz? Bir günde binlerce kuralı bir cihazdan diğerine taşımanız gerekirse en kolay ve en otomatik bir şekilde bu işlemi nasıl tasarlarız? Selenium Webdriver ile, web arayüzleri içerisinde otomatik aksiyon aldırmamız mümkün mü? Syslog'dan gelen verileri, diske toplayacak bir dinleyici script'i yazabilir miyiz?

Video linki: https://youtu.be/wWwVtO3iqg0

İlerideki videolarda SOAR ve API'lar yardımıyla da otomasyon örnekleri paylaşacağız.

### Videoda kullanilan script'ler:
* listener_orjinal.py --> Belirtilen port ve adresten Syslog dinleyip, diske yazan script'in orjinali. Çalıştırıldığında sonuçları youlogfile.log dosyasına yazıyor.
* syslog_listener.py --> Syslog dinleyen script'imizin bizim ihtiyaçlarımıza göre değiştirilmiş hali. Çalıştırıldığında sonuçları zararliip_dd_mm_yyyy_hh:mm.log dosyasına yazıyor.
* Action.py --> zararliip_dd_mm_yyyy_hh:mm.log dosyasi içeriğini, Kaspersky Security Center içindeki ilgili alana web arayüzü üzerinden yazan script.

* zararliip_dd_mm_yyyy_hh:mm.log --> Firewall'dan dinlediğimiz ve diske kaydettiğimiz zararlı IP listedi.
* youlogfile.py --> Firewall'dan dinlediğimiz ve diske kaydettiğimiz, filtrelenmemiş raw syslog verisi.
* Crontab_entry.md --> Script'i belirli araliklarla calistirmak icin gerekli Crontab entry'si

### Videoda kullanılan ilgili adresler:
* Chrome için Webdriver: https://chromedriver.chromium.org/downloads
* Chrome Webdriver Option'ları: https://chromedriver.chromium.org/capabilities
* Chrome için XPATH Finder Plug-in: https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph?hl=en
* Selenium Webdriver Find Element metodları: https://selenium-python.readthedocs.io/locating-elements.html
* Örnek bir Firewall Log Reference Guide (Palo Alto için): https://docs.paloaltonetworks.com/pan-os/8-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions
* Regex tasarlama ve test aracı: https://www.regexr.com
* Örnek bir Log & Reporting yapılandırma dökümanı (Sonicwall için): https://www.sonicwall.com/techdocs/pdf/sonicos-6-5-logs-and-reporting.pdf
* Örnek Crontab kullanımı: https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/
* Crontab builder araci: https://crontab.guru/
* PYCharm: https://www.jetbrains.com/pycharm/download/
