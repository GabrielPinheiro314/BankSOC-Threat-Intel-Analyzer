# Bank SOC Threat Intel Analyzer

## 🛡️ Sobre o Projeto
Este projeto simula um fluxo de trabalho real de um **SOC (Security Operations Center)** no setor financeiro/bancário. 
Bancos recebem milhões de requisições por segundo. Analisar logs de firewall manualmente é impossível. O objetivo deste script em Python é automatizar a **Análise de Inteligência de Ameaças (Threat Intelligence)** e a **Resposta a Incidentes**.

## ⚙️ Como Funciona (Arquitetura Lógica)
1. **Coleta de Logs:** O script lê um arquivo gerado pelo WAF (Web Application Firewall) contendo endereços IP suspeitos que tentaram acessar o portal do banco.
2. **Enriquecimento de Dados (Threat Intel):** Cada IP é consultado em uma API de Inteligência de Ameaças (neste projeto, simulada, mas projetada para integrar com VirusTotal, CrowdStrike, etc.).
3. **Decisão Baseada em Risco:**
   - Se o *Risk Score* for maior que 70 (ex: tráfego vindo de uma Botnet conhecida), o sistema emite um alerta crítico e simula o bloqueio.
   - Se o IP for limpo, o tráfego é categorizado como seguro.
4. **Geração de Relatórios:** Um relatório em CSV (`soc_incident_report.csv`) é gerado automaticamente para que a equipe de auditoria e compliance possa revisar.

## 🚀 Tecnologias e Habilidades Demonstradas
- **Linguagem:** Python (Scripting, manipulação de arquivos, automação).
- **Conceitos de Cibersegurança:** Incident Response, Threat Intelligence, Risk Scoring, SOC Automation.
- **Compliance e Negócios:** O projeto foca em redução de Risco Cibernético e tempo de resposta (MTTR - *Mean Time To Respond*), métricas críticas para a alta gestão de bancos.

## 💻 Como Executar
Nenhuma dependência externa complexa é necessária. O script usa bibliotecas padrão do Python para simular a API de terceiros de forma contida.

1. Clone este repositório.
2. Garanta que o arquivo `suspicious_ips.txt` está no mesmo diretório.
3. Execute no terminal:
   ```bash
   python analyzer.py
   ```
4. Verifique a saída no console e o arquivo gerado `soc_incident_report.csv`.

## 📈 Próximos Passos (Melhorias Futuras)
- [ ] Integrar com a API REST real do VirusTotal usando a biblioteca `requests`.
- [ ] Conectar a saída (relatório CSV) a um dashboard do Splunk ou ELK Stack.
- [ ] Adicionar notificação via Slack/Microsoft Teams usando Webhooks para alertar a equipe de plantão do SOC.
