import os 
import os.path


while True:
    os.system("clear")
    
    secenek = int(input("""
              Made By exs0r
       ___    ________        __  __            __          
      /   |  / _/ __ \      / / / /_  ______  / /____  _____
     / /| |  / // / / /_____/ /_/ / / / / __ \/ __/ _ \/ ___/
     / ___ |_/ // /_/ /_____/ __  / /_/ / / / / /_/  __/ /    
    /_/  |_/___/\____/     /_/ /_/\__,_/_/ /_/\__/\___/_/     
                         
    1] Port Tarama
    2] Subdomain Tarama
    3] Subfinder+Httpx+Subzy+Nuclei Taraması(Sızma Testi Denemesi)
    4] WAF Taraması

        Lütfen bir seçenek giriniz (1/2/3/4):  """))

    if secenek == 1:
        os.system("clear")


        hedef = input("Port Taraması İçin Hedef(HTTP veya HTTPS Olmadan)Giriniz:  ")
        os.system("clear")
        nmapsecenek = int(input("""

    NMAP Tarama Seçenekleri

1] Hızlı ve Versiyon Tespiti
2] Tüm Portları Tara (Uzun sürer)
3] Agresif Tarama(Detaylı Bilgi)

    Lütfen bir seçenek giriniz (1/2/3):  """))

        os.system("clear")
        if nmapsecenek == 1:
            os.system(f"nmap -Pn -sV {hedef}")

        elif nmapsecenek == 2:
            os.system(f"nmap -Pn -p- {hedef}")

        elif nmapsecenek == 3:
            os.system(f"nmap -Pn -A {hedef}")

        else:
            print("""Geçersiz seçenek numarası.
            
            """)

        print("                                       ")

    
        input("Ana menüye dönmek için Enter'a basın. ")

    if secenek == 2:
        os.system("clear")

        hedef = input("Subdomain Taraması İçin Hedef Giriniz:  ")
        os.system("clear")
        subdomsecenek = int(input("""
            Subdomain Tarama Seçenekleri
        1]Tara ve Kaydet(TXT Dosyasına)
        2]Sadece Tara

            Lütfen bir seçenek giriniz (1/2):  """))

        if subdomsecenek == 1:
            os.system(f"subfinder -d {hedef} --all -o subdomains.txt")
            print("Tarama sonuçları subdomains.txt dosyasına kaydedildi")


        elif subdomsecenek == 2:
            os.system(f"subfinder -d {hedef} --all ")
            print("Tarama sonuçlandı")


        input("Ana menüye dönmek için Enter'a basın. ")


    if secenek == 3:
        os.system("clear")
        sizmatestihedef = input("Sızma Testi İçin Hedef Giriniz:  ")
        print("Subdomainler Subfinder İle Taranıyor.")

        os.system(f"subfinder -d {sizmatestihedef} --all -o subdomains.txt > /dev/null 2>&1")
        print("Subdomainler tarandı")

        os.system("httpx -l subdomains.txt -o live.txt > /dev/null 2>&1")
        print("Canlı domainler filtrelendi")

        if os.path.exists("live.txt") and os.path.getsize("live.txt") > 0:
            os.system("subzy run --targets live.txt > takeover.txt 2>&1")
            print("Subzy ile Subdomain Takeover Taraması Yapıldı/ takeover.txt Dosyasına Kaydedildi")

            os.system("nuclei -l live.txt -t http -rate-limit 5 -bulk-size 2 -concurrency 2 -severity low,medium,high,critical -o nuclei_sonucları.txt -stats > /dev/null 2>&1")
            print("Tarama Tamamlandı Tüm Zafiyetler Başarıyla nuclei_sonucları.txt Dosyasına Kaydedildi ")
        else:
            print("Subdomainler Bulunamadığı İçin Nuclei İle Tarama Başlıyor.")
            os.system("clear")
            os.system(f"nuclei -u {sizmatestihedef} -t http -rate-limit 5 -bulk-size 2 -concurrency 2 -severity low,medium,high,critical -o nuclei_sonucları.txt -stats")
            print("Tarama Tamamlandı Tüm Zafiyetler Başarıyla nuclei_sonucları.txt Dosyasına Kaydedildi ")

        input("Ana menüye dönmek için Enter'a basın. ")

    if secenek == 4:

        os.system("clear")
        wafhedef = input("WAF Taraması İçin Hedef Giriniz: ")
        os.system(f"wafw00f {wafhedef}")

        print("                             ")


        input("Ana menüye dönmek için Enter'a basın. ")



