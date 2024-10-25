![image](https://github.com/user-attachments/assets/06846b6f-665a-4156-9b34-02328bad4dcf)
![image](https://github.com/user-attachments/assets/ce69c66a-b7cb-4e5e-a3bf-67a922bcede4)

Not all modules are finished!

RapidSploit is an advanced automation toolkit designed to streamline exploitation, payload generation, and vulnerability scanning, leveraging the power of Metasploit and Nmap. Built with versatility in mind, RapidSploit is ideal for penetration testers and security professionals who require a fast, automated way to manage exploit payloads, network scans, and multi-level vulnerability assessments—all from a single, intuitive interface.

Key Features
Metasploit Exploitation Automation
Rapidly execute common and custom Metasploit exploits against target devices. Includes options like the well-known MS17-010 (EternalBlue) SMB exploit, Apache Struts RCE, Tomcat Manager Upload, and Android reverse TCP. Easily configure target and listener IPs and ports for efficient, precise exploitation.

Automated Payload Generation
Generate custom reverse shell payloads across platforms, supporting Windows, Android, and Linux. RapidSploit uses msfvenom to create tailored payloads for remote code execution, saved locally for easy deployment in social engineering or direct attack scenarios.

Vulnerability Scanning
Discover network vulnerabilities with both Nmap and Metasploit auxiliary modules. RapidSploit can perform:

Nmap Vulnerability Scan: Uses Nmap's NSE scripts to detect and report on vulnerabilities across multiple services.
Metasploit Auxiliary Scans: Includes dedicated scans for SMB, FTP, SSH, and custom auxiliary modules to detect version-based vulnerabilities.
Phishing and Credential Harvesting
Set up phishing pages and credential harvesting sites using the Social Engineering Toolkit (SET), including Evil Twin attacks for Wi-Fi phishing.

Network Mapping and Discovery
Automatically map network devices and discover live hosts with the option to interactively select targets. Supports quick scans to retrieve IP addresses, hostnames, and device details for efficient targeting.

Post-Exploitation and Persistence
Automate post-exploitation techniques and establish persistence on compromised devices, allowing for continuous access and further exploitation.

Payload Delivery via HTTP and SMB
Rapidly deploy payloads through HTTP or SMB file-sharing options to maximize delivery flexibility.

Bluetooth and Wi-Fi Exploits
Additional exploit support for Bluetooth and Wi-Fi, including Evil Twin and deauth attacks for Wi-Fi phishing.

Why Use RapidSploit?
RapidSploit simplifies complex workflows by uniting Metasploit, Nmap, and social engineering capabilities into one efficient toolkit. Its interactive prompts and easy-to-navigate interface make it beginner-friendly yet powerful enough for advanced users. Whether you need fast network mapping, exploit automation, or advanced persistence setup, RapidSploit provides a unified solution for rapid, effective penetration testing and vulnerability assessment.




# Metasploit Automation Script

This script automates several Metasploit tasks, including running exploits, generating payloads, and performing network vulnerability scans using both Nmap and Metasploit auxiliary modules. It is designed to streamline exploitation and vulnerability scanning processes.

## Features

- **Run Metasploit Exploits**: Execute popular exploits like MS17-010 (EternalBlue) and Apache Struts 2.
- **Generate Payloads**: Generate reverse shell payloads for Windows, Android, and Linux.
- **Vulnerability Scanning**: Scan networks using Nmap’s NSE vulnerability scripts or Metasploit auxiliary modules.

## Installation

### Prerequisites

- **Kali Linux or Debian-based OS** with Metasploit and Nmap installed
- `sudo` privileges to run the script

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/metasploit-automation-script.git
cd metasploit-automation-script
