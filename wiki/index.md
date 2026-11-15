---
title: "Cybersecurity Knowledge Master Index"
type: index
last_updated: 2026-11-13
status: active
---

# Cybersecurity Knowledge Master Index

> Master catalog of all persistent knowledge nodes in the **cyber** vault.
> Updated continuously on every `/ingest`, `/query`, and `/lint` operation.

---

## 🧭 Navigation & Core Documents
- 📘 **Operating Schema & Rules:** `[[AGENTS.md]]`
- ⚡ **Slash Commands Manual:** `[[COMMANDS.md]]`
- 🎯 **Strategic Synthesis & Doctrine:** `[[wiki/overview]]`
- 📜 **Chronological Audit Trail:** `[[wiki/log]]`

---

## 🏛️ Frameworks & Standards
| Node | Focus | Tags | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/frameworks/mitre-attack]]` | 14 Enterprise Tactics & Matrix | `#framework`, `#mitre-attack` | Active |
| `[[wiki/frameworks/owasp-top-10]]` | Critical Web Application Flaws | `#appsec`, `#owasp` | Active |

---

## ⚔️ Attacks & Threat Tradecraft
| Node | Tactic / Vector | MITRE ID | Severity | Status |
| :--- | :--- | :--- | :--- | :--- |
| `[[wiki/attacks/kerberoasting]]` | Active Directory Service Ticket Cracking | T1558.003 | High | Active |
| `[[wiki/attacks/sql-injection]]` | Dynamic Database Query Manipulation | T1190 | Critical | Active |

---

## 🛡️ Defenses & Detection Engineering
| Node | Focus Area | High-Value Telemetry | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/defenses/active-directory-hardening]]` | Administrative Tiering & Kerberos Hardening | Event 4769, 4624, LAPS | Active |
| `[[wiki/defenses/detection-engineering]]` | Sigma Authoring & Telemetry Lifecycle | Sysmon, Windows Event Logs | Active |
| `[[wiki/defenses/vulnerability-auditing-methodology]]` | Multi-Pillar Static & Cross-File Audit Lifecycle | SAST, Secrets, Supply-Chain | Active |
| `[[wiki/defenses/automated-security-reporting]]` | Big Four Executive PDF Report Generation | ReportLab, Severity Roadmaps | Active |

---

## 🪲 Vulnerabilities & CVE Deep Dives
| Node | CVE ID | CVSS | CWE | Status |
| :--- | :--- | :--- | :--- | :--- |
| `[[wiki/vulnerabilities/log4shell-cve-2021-44228]]` | CVE-2021-44228 | 10.0 | CWE-502 | Active |

---

## 🛠️ Security Tool Dossiers
| Node | Primary Function | Primary Environment | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/tools/bloodhound]]` | Active Directory Attack Path Graph Analysis | Windows / Linux / Neo4j | Active |
| `[[wiki/tools/nmap]]` | Port Scanning & Service Enumeration | Cross-platform | Active |
| `[[wiki/tools/security-scanners-suite]]` | Automated SAST, Secrets & Vulnerability Scanners | Semgrep, Gitleaks, Trivy, YARA | Active |

---

## 📚 Ingested Sources
| Source Node | Original File | Author / Origin | Key Insights |
| :--- | :--- | :--- | :--- |
| `[[wiki/sources/elite-cybersecurity-audit-agent]]` | `raw/articles/elite-cybersecurity-forensics-audit-agent.md` | Bhupesh Chandra Dimri | Universal file forensics, multi-pillar auditing, PDF reporting |
| `[[wiki/sources/antigravity-sandbox-auditor]]` | `raw/articles/antigravity-autonomous-sandbox-auditor.md` | Bhupesh Chandra Dimri | Autonomous sandbox discovery, cross-file correlation, verdict model |
| `[[wiki/sources/big-four-intaglio-engraving-engine]]` | `raw/articles/big-four-intaglio-engraving-design-engine.md` | Bhupesh Chandra Dimri | Big Four + Luxury Banknote Intaglio Guilloché Vector Design Engine |

---

## 🏗️ Architecture & Blueprints
| Node | Architecture Pattern | Key Principles | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/architectures/zero-trust-architecture]]` | NIST SP 800-207 Zero Trust | Explicit Verify, Least Privilege, Assume Breach | Active |

---

## 🔬 Analyses & Threat Models
| Node | Analysis Type | Primary System | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/analyses/threat-model-web-auth]]` | STRIDE Threat Model | SPA + OAuth 2.0 API Gateway | Active |
| `[[wiki/analyses/master-cybersecurity-and-geospatial-threat-dossier]]` | Master Threat & Address Dossier | TeamsSetup.bat + C2 Physical Attribution | Active |

---

## 📝 Lab Walkthroughs & CTF Notes
| Node | Category | Target | Status |
| :--- | :--- | :--- | :--- |
| `[[wiki/writeups/template-lab-writeup]]` | Blueprint / Template | Lab Walkthrough & Kill Chain | Active |
| `[[wiki/writeups/malware-analysis-fake-teams-screenconnect]]` | Malware Triage | Fake Teams Dropping ScreenConnect RAT | Active |

---

## 🔮 Optional: Obsidian Dataview Query Snippet
If you have the **Dataview** Obsidian plugin installed, paste this block into any page to generate a live dynamic index:

```dataview
TABLE type AS "Type", severity AS "Severity", last_updated AS "Last Updated"
FROM "wiki"
WHERE file.name != "index" AND file.name != "log"
SORT last_updated DESC
```
