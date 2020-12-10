# Test amacli client scripti, Caner Aydin Youtube kanali icin hazirladim.

from selenium import webdriver
from datetime import datetime
import glob, os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


servis_ip_adresi = "https://192.168.2.209:8080" # Web servisin URL ya da IP'si
kul_adi = "KullaniciAdiGizli" #Servise giris icin ilgili islemi yapmaya yetkili kullanici adi ve sifre
sifre = "SifremiKimseylePaylasmamayaCalisiyorum" #Servise giris icin ilgili islemi yapmaya yetkili kullanici adi ve sifre

opts = Options()
opts.add_argument('--ignore-certificate-errors') # SSL hatalarını atlamak için kullanıyoruz

driver = webdriver.Chrome(
    executable_path='/Users/Caner-MacPro/Documents/chromedriver', options=opts); #Otomatik Chrome calistiran yapi, Chromedriver adresini girmeyi unutmayin.

driver.get(servis_ip_adresi) #Chrome'u acip ilgili adrese gidecek
driver.implicitly_wait(1) #Sayfa yavas acilirsa diye max 1 sn bekleyecek
time.sleep(1) #1 saniye mola
driver.find_element_by_xpath("/html/body/div[1]/section/form/div[4]/input").send_keys(kul_adi) #XPATH'e gore kul_adi kutusunu bulacak ve girecek
driver.find_element_by_xpath("/html/body/div[1]/section/form/div[5]/input").send_keys(sifre) #XPATH'e gore sifre kutusunu bulacak ve girecek
driver.find_element_by_xpath("/html/body/div[1]/section/form/div[7]/button").click() #Submit butonuna tiklayacak

driver.implicitly_wait(3)
time.sleep(1)


driver.find_element_by_xpath("/html/body/div[1]/section/kl-app/kl-app-header/header/div[3]/kl-app-navigation/kl-menu/div[2]/a/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/kl-app/kl-layout/section/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw/kl-auto-data-table/div/div[2]/table/tbody/tr[4]/td[3]/kl-auto-data-table-cell/div/a/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[3]/kl-auto-segmented-form-group/div[1]/div/a[3]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[3]/kl-auto-segmented-form-group/div[2]/div/kl-auto-form-set-wrapper/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw/kl-plugin-loader/div/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw/kl-auto-segmented-form-group/div[1]/div/a[2]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[3]/kl-auto-segmented-form-group/div[2]/div/kl-auto-form-set-wrapper/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw/kl-plugin-loader/div/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw/kl-auto-segmented-form-group/div[2]/div/kl-auto-form-set-wrapper/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[5]/kl-auto-form-trigger/div/div/div/div[1]/a/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[2]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[4]/kl-auto-link/div/a/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[3]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[3]/kl-auto-data-table/div/div[1]/kl-auto-toolbar/div/kl-auto-toolbar-item[1]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

bugun = datetime.now() #Bugunun tarih ve saatini aliyor
bugun2 = bugun.strftime("%m-%d-%Y-%H:%M") #Tarih ve saati verilmis formata cevirdi

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[4]/kl-auto-textbox/div/input").send_keys("Firewalldan Engellenen IP " + bugun2) #Kural adini bugunun tarihi ile birlikte Firewall'dan Engellenen IP seklinde yazdi

coktansecmeli = Select(driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[6]/kl-auto-select/div/div/select"))
coktansecmeli.select_by_index(1) #Ust satirla birlikte, Select itemi bir dropdown menuden item secmeye yariyor

driver.implicitly_wait(3)
time.sleep(1)

coktansecmeli = Select(driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[10]/kl-auto-select/div/div/select"))
coktansecmeli.select_by_index(2)
driver.implicitly_wait(3)
time.sleep(1)

coktansecmeli = Select(driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[18]/kl-auto-select/div/div/select"))
coktansecmeli.select_by_index(2)
time.sleep(1)

###### ONEMLİ --> Su anda ilgili klasordeki log dosyasini okuyacagiz
for file in glob.glob("*.log"): #o klasordeki tum .log dosyalarini buluyor
    print(file)

dosya1 = open(file, 'r')
ipler = dosya1.readlines() #Buldugu dosyayi aciyor, satir satir okuyor, "ipler" isimli liste yaziyor.
print(ipler)

ipler_dedup = [*{*ipler}] #İlgili listede birden cok ayni deger varsa siliyor (ayni IP'den birden cok atak gelmis olabilir)
print(ipler_dedup) #Listenin dedup edilmis halini ekrana yaziyor

for x in ipler_dedup: #Listedeki her bir IP icin ilgili ekrana IP'yi girip submit ediyor.
    driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[20]/kl-auto-data-table/div/div[1]/kl-auto-toolbar/div/kl-auto-toolbar-item[1]/kl-auto-locale/span").click()
    driver.find_element_by_xpath("/html/body/div[1]/section/kl-app/kl-flyout-panel/div/div/section/div/kl-flyout-panel-content/kl-auto-form-set/div/kl-auto-form/kl-auto-control-set/kl-auto-raw[4]/kl-auto-textbox/div/input").send_keys(x)
    driver.find_element_by_xpath("/html/body/div[1]/section/kl-app/kl-flyout-panel/div/div/section/div/kl-flyout-panel-content/kl-auto-form-set/div/kl-auto-form/div[2]/div[2]/div/button[1]/kl-auto-locale/span").click()
    driver.implicitly_wait(3)
    time.sleep(2)

driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[4]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/div[2]/div[2]/div/button[1]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)


driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[3]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/div[2]/div[2]/div/button[1]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl[2]/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/div[2]/div[2]/div/button/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)


driver.find_element_by_xpath("/html/body/div[1]/section/div/kl-popup-xl/div[2]/section/div/kl-router-outlet/div/kl-auto-form-set/div/kl-auto-form/div[2]/div[2]/div/button[2]/kl-auto-locale/span").click()
driver.implicitly_wait(3)
time.sleep(1)

time.sleep(1)

driver.quit()

os.remove(file)