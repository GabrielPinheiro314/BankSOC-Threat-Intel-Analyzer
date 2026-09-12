import json
import random
import datetime
import csv
import time

# --- THREAT INTELLIGENCE MODULE ---
def query_threat_intel(ip_address):
    """
    Simulates a request to a cybersecurity API (like VirusTotal, CrowdStrike, or IBM X-Force).
    In a real corporate/banking environment, we would use the 'requests' library with an API Key.
    """
    # Simulating a bank's internal database of known malicious IPs
    known_malicious = ['192.168.1.50', '203.0.113.42', '198.51.100.23']
    
    # Small delay to simulate network response time
    time.sleep(0.3)
    
    if ip_address in known_malicious:
        score = random.randint(75, 100) # High score indicates critical danger
        threat_type = random.choice(["Botnet C&C", "Banking Phishing Node", "Ransomware Gateway"])
    else:
        score = random.randint(0, 20) # Low score indicates normal/safe traffic
        threat_type = "Clean / No Known Threats"
        
    return {
        "ip": ip_address,
        "risk_score": score,
        "threat_type": threat_type,
        "timestamp": datetime.datetime.now().isoformat()
    }

# --- FIREWALL LOG PROCESSING MODULE ---
def process_firewall_logs(input_file, output_file):
    print("="*60)
    print(" XYZ BANK - AUTOMATED INCIDENT RESPONSE SYSTEM")
    print("="*60)
    print(f"[*] Loading suspicious firewall logs from: {input_file}\n")
    results = []
    
    try:
        with open(input_file, 'r') as file:
            ips = file.readlines()
            
        for ip in ips:
            ip = ip.strip()
            if not ip: continue
            
            print(f"[*] Analyzing IP: {ip}...")
            intel_data = query_threat_intel(ip)
            results.append(intel_data)
            
            # Business logic: The bank only wants alerts if the risk is > 70
            if intel_data['risk_score'] > 70:
                print(f"    [!] CRITICAL ALERT: Risk {intel_data['risk_score']}/100 - Category: {intel_data['threat_type']}")
                print(f"    [!] Automated Action: Blocking rule applied to WAF (Web Application Firewall).\n")
            else:
                print(f"    [+] Safe IP. Allowing traffic.\n")
                
        # Generating structured report (CSV) for the SOC (Security Operations Center) team
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ip', 'risk_score', 'threat_type', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in results:
                writer.writerow(row)
                
        print("="*60)
        print(f"[+] Analysis successfully completed.")
        print(f"[+] Report generated for the SOC team at: {output_file}")
        print("="*60)
        
    except FileNotFoundError:
        print(f"[-] Critical Error: The log file {input_file} was not found.")

if __name__ == "__main__":
    # Input and output file names
    INPUT_LOG = "suspicious_ips.txt"
    OUTPUT_REPORT = "soc_incident_report.csv"
    
    # Start the security pipeline
    process_firewall_logs(INPUT_LOG, OUTPUT_REPORT)
