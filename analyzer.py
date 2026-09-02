import json
import random
import datetime
import csv
import time

# --- MÓDULO DE INTELIGÊNCIA DE AMEAÇAS ---
def query_threat_intel(ip_address):
    """
    Simula uma requisição a uma API de cibersegurança (como VirusTotal, CrowdStrike, ou IBM X-Force).
    Em um ambiente real corporativo/bancário, usaríamos a biblioteca 'requests' com uma API Key.
    """
    # Simulando um banco de dados interno de um banco com IPs conhecidos como maliciosos
    known_malicious = ['192.168.1.50', '203.0.113.42', '198.51.100.23']
    
    # Pequeno delay para simular o tempo de resposta da rede
    time.sleep(0.3)
    
    if ip_address in known_malicious:
        score = random.randint(75, 100) # Score alto indica perigo crítico
        threat_type = random.choice(["Botnet C&C (Comando e Controle)", "Nó de Phishing Bancário", "Gateway de Ransomware"])
    else:
        score = random.randint(0, 20) # Score baixo indica tráfego normal/seguro
        threat_type = "Limpo / Sem Ameaças Conhecidas"
        
    return {
        "ip": ip_address,
        "risk_score": score,
        "threat_type": threat_type,
        "timestamp": datetime.datetime.now().isoformat()
    }

# --- MÓDULO DE PROCESSAMENTO DE LOGS DO FIREWALL ---
def process_firewall_logs(input_file, output_file):
    print("="*60)
    print(" BANCO XYZ - SISTEMA AUTOMATIZADO DE RESPOSTA A INCIDENTES")
    print("="*60)
    print(f"[*] Carregando logs suspeitos do firewall: {input_file}\n")
    results = []
    
    try:
        with open(input_file, 'r') as file:
            ips = file.readlines()
            
        for ip in ips:
            ip = ip.strip()
            if not ip: continue
            
            print(f"[*] Analisando IP: {ip}...")
            intel_data = query_threat_intel(ip)
            results.append(intel_data)
            
            # Lógica de negócio: O Banco só quer ser alertado se o risco for maior que 70
            if intel_data['risk_score'] > 70:
                print(f"    [!] ALERTA CRÍTICO: Risco {intel_data['risk_score']}/100 - Categoria: {intel_data['threat_type']}")
                print(f"    [!] Ação Automática: Regra de bloqueio aplicada no WAF (Web Application Firewall).\n")
            else:
                print(f"    [+] IP Seguro. Permitindo tráfego.\n")
                
        # Gerando relatório estruturado (CSV) para a equipe de SOC (Security Operations Center)
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ip', 'risk_score', 'threat_type', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in results:
                writer.writerow(row)
                
        print("="*60)
        print(f"[+] Análise concluída com sucesso.")
        print(f"[+] Relatório gerado para a equipe de SOC em: {output_file}")
        print("="*60)
        
    except FileNotFoundError:
        print(f"[-] Erro crítico: O arquivo de log {input_file} não foi encontrado.")

if __name__ == "__main__":
    # Nomes dos arquivos de entrada e saída
    INPUT_LOG = "suspicious_ips.txt"
    OUTPUT_REPORT = "soc_incident_report.csv"
    
    # Inicia o pipeline de segurança
    process_firewall_logs(INPUT_LOG, OUTPUT_REPORT)
