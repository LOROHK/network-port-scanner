#!/usr/bin/env python3
# 🔍 Python Port Scanner - Network Security Tool

import socket
import time

def get_service_name(port):
    """Get common service name for well-known ports"""
    common_services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
        995: "POP3S", 3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB"
    }
    return common_services.get(port, "Unknown")

def scan_port(host, port):
    """Scan a single port on the target host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

def main():
    print("🔍 Python Port Scanner")
    print("======================")
    
    target = input("Enter target host (localhost or IP): ").strip()
    if not target:
        target = "localhost"
    
    try:
        start_port = int(input("Start port (1-65535): ") or "70")
        end_port = int(input("End port (1-65535): ") or "85")
    except:
        print("❌ Invalid port numbers. Using default range 70-85")
        start_port, end_port = 70, 85
    
    print(f"\n🎯 Scanning {target} from port {start_port} to {end_port}")
    print("⏳ This may take a moment...\n")
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            service = get_service_name(port)
            print(f"✅ Port {port} is OPEN ({service})")
            open_ports.append(port)
        else:
            print(f"❌ Port {port} is closed")
        
        time.sleep(0.1)
    
    print(f"\n📊 Scan Complete!")
    print(f"📍 Target: {target}")
    print(f"🔓 Open ports: {open_ports if open_ports else 'None found'}")
    print(f"📈 {len(open_ports)} open ports out of {end_port - start_port + 1} scanned")

if __name__ == "__main__":
    main()