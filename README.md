
# 🛡️ Automated Recon & Vulnerability Scanner

<div align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Linux%20%2F%20Kali-orange?style=for-the-badge&logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/Security-Pentesting-red?style=for-the-badge&logo=kalilinux&logoColor=white">

  <p><b>Made by exs0r</b></p>
  <p>Siber güvenlik meraklıları ve penetration testerlar için geliştirilmiş, popüler recon araçlarını tek bir menüde birleştiren akıllı otomasyon scripti.</p>

</div>

---

## 🚀 Özellikler

* **1] Port Taraması (Nmap):** Hedef IP/Domain üzerinde hızlı versiyon tespiti, tüm port taraması veya agresif tarama modları.
* **2] Subdomain Taraması (Subfinder):** Hedef sisteme ait alt alan adlarını bulma ve isterseniz `.txt` dosyasına kaydetme.
* **3] Otomatik Sızma Testi Pipeline (Subfinder + Httpx + Subzy + Nuclei):** 
  * Subdomainleri toplar ve canlı olanları (`live.txt`) filtreler.
  * Canlı adreslerde **Subdomain Takeover** taraması yapar (`takeover.txt`).
  * Zafiyet taraması gerçekleştirir (`nuclei_sonucları.txt`).
  * *Akıllı Fallback:* Eğer canlı subdomain bulunamazsa, otomatik olarak ana hedefi doğrudan `nuclei` ile tarar.
* **4] WAF Taraması (Wafw00f):** Hedef web uygulamasında Web Application Firewall (WAF) olup olmadığını tespit eder.

---

## 📦 Gereksinimler

Bu aracın sorunsuz çalışabilmesi için sisteminizde aşağıdaki araçların kurulu ve PATH ortam değişkenine ekli olması gerekir:

* Python 3.x
* [Nmap](https://nmap.org/)
* [Subfinder](https://github.com/projectdiscovery/subfinder)
* [Httpx](https://github.com/projectdiscovery/httpx)
* [Subzy](https://github.com/LukaSikic/subzy)
* [Nuclei](https://github.com/projectdiscovery/nuclei)
* [Wafw00f](https://github.com/EnableSecurity/wafw00f)

---

## ⚙️ Kurulum ve Çalıştırma

Depoyu klonlayın ve scripti çalıştırın:

```bash
# Repoyu klonlayın
git clone https://github.com/exs0r9v/AIO-Hunter.git
cd AIO-Hunter

# Scripti çalıştırın (Root yetkisi gerekebilir)
sudo python3 aio-hunter.py
