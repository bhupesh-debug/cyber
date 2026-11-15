---
title: "MITRE ATT&CK Framework Knowledge Hub"
type: framework
tags:
  - framework
  - threat-intel
  - mitre-attack
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/attacks/kerberoasting]]"
  - "[[wiki/defenses/detection-engineering]]"
---

# MITRE ATT&CK Framework Knowledge Hub

The **MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK)** framework is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. It serves as the primary taxonomy for categorizing offensive behaviors and structuring detection engineering in this wiki.

---

## 1. The 14 Enterprise Tactics

Adversary tactics describe the *why* of an attack technique — the adversary's tactical objective.

1. **Reconnaissance (TA0043):** Gathering information to plan future adversary operations.
2. **Resource Development (TA0042):** Establishing resources to support operations (infrastructure, accounts).
3. **Initial Access (TA0001):** Vectors used to gain an initial foothold (phishing, public-facing exploits).
4. **Execution (TA0002):** Techniques that result in adversary-controlled code running on a local or remote system.
5. **Persistence (TA0003):** Mechanisms to maintain access across restarts or changed credentials.
6. **Privilege Escalation (TA0004):** Gaining higher-level permissions (SYSTEM, root, Domain Admin).
7. **Defense Evasion (TA0005):** Avoiding detection (disabling security tools, obfuscating payloads).
8. **Credential Access (TA0006):** Stealing credentials such as usernames and passwords (`[[wiki/attacks/kerberoasting|Kerberoasting]]`).
9. **Discovery (TA0007):** Gaining knowledge about the internal network and system (`[[wiki/tools/bloodhound|BloodHound]]`, `[[wiki/tools/nmap|Nmap]]`).
10. **Lateral Movement (TA0008):** Accessing and controlling remote systems on a network.
11. **Collection (TA0009):** Gathering data of interest (documents, emails, audio).
12. **Command and Control (TA0011):** Communicating with compromised systems from external infrastructure.
13. **Exfiltration (TA0010):** Stealing data out of the target environment.
14. **Impact (TA0040):** Manipulating, interrupting, or destroying business and operational processes.

---

## 2. Vault Mapping Matrix

| Technique ID | Technique Name | Tactic | Vault Link | Defensive Counterpart |
| :--- | :--- | :--- | :--- | :--- |
| **T1558.003** | Kerberoasting | Credential Access | `[[wiki/attacks/kerberoasting]]` | `[[wiki/defenses/active-directory-hardening]]` |
| **T1190** | Exploit Public-Facing App | Initial Access | `[[wiki/attacks/sql-injection]]` | `[[wiki/frameworks/owasp-top-10]]` |
| **T1046** | Network Service Discovery | Discovery | `[[wiki/tools/nmap]]` | `[[wiki/defenses/detection-engineering]]` |
| **T1069.002** | Domain Groups Discovery | Discovery | `[[wiki/tools/bloodhound]]` | `[[wiki/defenses/active-directory-hardening]]` |
