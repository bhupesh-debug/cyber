# 🛡️ Cybersecurity LLM Wiki & Digital Forensics Intelligence Vault

> A persistent, compounding Cybersecurity Knowledge Base, Threat Intelligence Repository, and Autonomous Forensic Auditing System built on the **LLM Wiki Pattern**.

[![Platform](https://img.shields.io/badge/Platform-Obsidian%20%7C%20Markdown-7C3AED.svg)](https://obsidian.md)
[![Design Standard](https://img.shields.io/badge/Report%20Standard-Big%20Four%20%2B%20Intaglio%20Engraving-14243A.svg)](#-master-executive-dossier)
[![Security Focus](https://img.shields.io/badge/Security-MITRE%20ATT%26CK%20%7C%20OWASP-DC2626.svg)](#-knowledge-graph-architecture)

---

## 🏛️ Vault Architecture

```
cyber/
├── AGENTS.md                  ← Master operating manual & schema (Read first by AI agents)
├── COMMANDS.md                ← User manual for "/" slash commands (/ingest, /query, /lint...)
├── CLAUDE.md / GEMINI.md      ← Agent interface aliases
├── Master_Executive_Report/   ← Consolidated Big Four + Intaglio Engraved Master PDF Dossier
│   └── Master_Cybersecurity_Forensic_and_Geospatial_Dossier.pdf
├── GPS_Address_Intelligence/  ← High-precision reverse geocoding & address verification suite
│   ├── GPS_Address_Report.pdf
│   ├── GPS_Address_Results.xlsx
│   ├── GPS_Address_Results.csv
│   ├── maps/ (map_snapshot.png)
│   └── verification/ (raw_nominatim.json, raw_census.json)
├── Cybersecurity_Audit/       ← Malware triage & forensic audit deliverables
│   ├── 01_Original_Files/     (TeamsSetup.bat sample)
│   └── 05_Final_PDF_Report/   (Cybersecurity_Audit_Report_TeamsSetup_2026-11-14.pdf)
├── raw/                       ← Immutable source documents (Read-only)
│   ├── advisories/
│   ├── articles/
│   ├── books_and_guides/
│   └── writeups/
└── wiki/                      ← Persistent, compounding LLM knowledge graph
    ├── index.md               ← Master categorized catalog & dynamic Dataview queries
    ├── log.md                 ← Append-only chronological audit log
    ├── overview.md            ← Strategic doctrine & threat landscape synthesis
    ├── attacks/               ← MITRE ATT&CK tradecraft (Kerberoasting, SQLi...)
    ├── defenses/              ← Detection engineering (Sigma, Active Directory hardening...)
    ├── vulnerabilities/       ← CVE profiles & root-cause analyses (Log4Shell...)
    ├── tools/                 ← Tool dossiers (BloodHound, Nmap, Security Scanners...)
    ├── architectures/         ← Zero Trust, Cloud IAM, Microsegmentation
    ├── writeups/              ← Deep lab breakdowns & malware investigations
    ├── frameworks/            ← MITRE ATT&CK, NIST CSF, OWASP Top 10
    ├── sources/               ← Per-source ingest summaries & takeaways
    └── analyses/              ← Filed answers, threat models & comparative matrices
```

---

## 🔬 Featured Case Study: Disguised Teams Dropper & C2 Attribution

This vault contains an end-to-end investigation linking endpoint malware execution directly to physical hosting data center attribution:

1. **Endpoint Dropper (`TeamsSetup.bat`):**
   - **Masquerading:** Deceptive borderless Microsoft Edge app-mode window (`--app=`) displaying official Teams branding.
   - **Privilege Escalation:** Hidden PowerShell command executing `-Verb RunAs` to force UAC elevation.
   - **Living-off-the-Land RMM Abuse:** Silently downloads and installs **ConnectWise ScreenConnect** client (`ScreenConnect.ClientSetup.msi`), granting attackers persistent unattended access under `NT AUTHORITY\SYSTEM`.
   - **Anti-Forensics:** Force-kills the decoy browser process and deletes staging files, logs, and installers.
2. **C2 Infrastructure (`zoompetr[.]com`):**
   - Typosquatted domain resolving to IPv4 `135.84.215.218` (Hyonix VPS, AS399114).
3. **Physical Address Resolution (`33.441300° N, -112.042100° W`):**
   - Reverse geocoded across OpenStreetMap Nominatim and the US Census Bureau TIGER system with 100% consensus:
   - **Resolved Physical Address:** `East Sky Harbor Circle North, Central City, Phoenix, Maricopa County, Arizona 85034, United States (Census Tract 1139)`.

---

## 📄 Executive PDF Deliverables

- 📄 **[Master Dossier PDF](Master_Executive_Report/Master_Cybersecurity_Forensic_and_Geospatial_Dossier.pdf)** — Unified 6-page Big Four Consulting + Intaglio Banknote Engraved Report.
- 📄 **[GPS Address Report PDF](GPS_Address_Intelligence/GPS_Address_Report.pdf)** — High-precision geospatial resolution & multi-provider verification report.
- 📄 **[Cybersecurity Audit PDF](Cybersecurity_Audit/05_Final_PDF_Report/Cybersecurity_Audit_Report_TeamsSetup_2026-11-14.pdf)** — Deep forensic decompilation of `TeamsSetup.bat`.

---

## ⚡ Slash Commands Reference

Interact with this vault using your AI agent (Antigravity, Claude Code, Gemini CLI):

| Command | Action |
| :--- | :--- |
| **`/ingest <source>`** | Extracts insights, cross-links 5–15 atomic wiki pages, updates master catalog and log. |
| **`/query <question>`** | Synthesizes an answer with citations from compiled graph nodes; files valuable analyses back into `wiki/analyses/`. |
| **`/lint`** | Health-checks the vault: identifies orphan notes, contradictions, and defensive blindspots. |
| **`/threat-model <system>`** | Executes STRIDE/PASTA threat assessment, generating an actionable mitigation matrix. |
| **`/cve <CVE-ID>`** | Produces technical root-cause breakdown, exploitability status, and detection rules. |
| **`/lab-debrief <target>`** | Converts lab walkthroughs into persistent offensive tradecraft and SOC telemetry lessons. |

See [COMMANDS.md](COMMANDS.md) for full syntax and examples.

---

## 👤 Author
**Bhupesh Chandra Dimri**  
*Cybersecurity Forensics Specialist, Threat Intelligence Researcher & Geospatial Analyst*
