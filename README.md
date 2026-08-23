# 🛡️ Automated Recon & Vulnerability Scanner

<div align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Linux%20%2F%20Kali-orange?style=for-the-badge&logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/Security-Pentesting-red?style=for-the-badge&logo=kalilinux&logoColor=white">

  <p><b>Made by exs0r</b></p>
  <p>An intelligent automation script designed for cybersecurity enthusiasts and penetration testers, combining popular recon tools into a single interactive menu.</p>

</div>

---

## 🚀 Features

* **1] Port Scanning (Nmap):** Fast version detection, full port scanning, or aggressive scan modes on target IPs/domains.
* **2] Subdomain Enumeration (Subfinder):** Discover subdomains belonging to the target system and optionally save them to a `.txt` file.
* **3] Automated Pentesting Pipeline (Subfinder + Httpx + Subzy + Nuclei):** 
  * Gathers subdomains and filters live hosts (`live.txt`).
  * Performs **Subdomain Takeover** checks on live targets (`takeover.txt`).
  * Executes vulnerability scanning (`nuclei_sonucları.txt`).
  * *Smart Fallback:* If no live subdomains are found, it automatically switches to scan the root target directly with `nuclei`.
* **4] WAF Detection (Wafw00f):** Detects if a Web Application Firewall (WAF) is protecting the target web application.

---

## 📦 Prerequisites

To run this tool smoothly, ensure the following tools are installed on your system and added to your PATH environment variable:

* Python 3.x
* [Nmap](https://nmap.org/)
* [Subfinder](https://github.com/projectdiscovery/subfinder)
* [Httpx](https://github.com/projectdiscovery/httpx)
* [Subzy](https://github.com/LukaSikic/subzy)
* [Nuclei](https://github.com/projectdiscovery/nuclei)
* [Wafw00f](https://github.com/EnableSecurity/wafw00f)

---

## ⚙️ Installation & Usage

Clone the repository and run the script:

```bash
# Clone the repository
git clone [https://github.com/exs0r9v/AIO-Hunter.git](https://github.com/exs0r9v/AIO-Hunter.git)
cd AIO-Hunter

# Run the script (Root privileges may be required)
sudo python3 aio-hunter.py


```
Disclaimer
This tool is developed for educational purposes and authorized security testing only. Unauthorized scanning of targets you do not own or have explicit permission to test is illegal. The user assumes all responsibility for any misuse or damage caused by this program.
