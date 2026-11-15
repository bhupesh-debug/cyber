# AGENTS.md — Cybersecurity LLM Wiki Schema & Operating Manual

> **Vault:** `cyber`  
> **Mission:** Build a persistent, compounding, authoritative Cybersecurity Knowledge Base and Skill Accelerator across offensive tradecraft, defensive engineering, threat intelligence, vulnerability research, and incident response.  
> **Operating Rule:** Every new advisory, writeup, CVE, exploit, lab debrief, or concept must strengthen, cross-link, and calibrate the existing knowledge graph rather than sitting in isolation.

---

## 1. Core Principles

1. **Compounding Knowledge:** The wiki sits between the human operator and raw sources. Information is read once, broken down into atomic entities, and woven into existing pages. Knowledge compounds over time.
2. **Attacker ⟷ Defender Duality:** Every offensive technique must link to its corresponding detection and mitigation (e.g., `[[attacks/kerberoasting]]` ↔ `[[defenses/active-directory-hardening]]` + `[[tools/bloodhound]]`).
3. **Immutability of Raw Sources:** The `raw/` directory contains original articles, advisories, reports, PCAPs, transcripts, and configs. **The LLM never modifies anything inside `raw/`.**
4. **LLM Owns the Wiki:** The LLM manages formatting, categorization, cross-referencing, index updating, and chronological logging in `wiki/`. The human directs, questions, clips sources, and verifies conclusions.
5. **Obsidian as the Security IDE:** Designed for Obsidian Graph View, Dataview queries, Canvas threat models, and local-first offline security workflows.

---

## 2. Directory Architecture

```
cyber/
├── AGENTS.md                  ← Master operating instructions & schema (Read first)
├── CLAUDE.md                  ← Agent alias file
├── GEMINI.md                  ← Agent alias file
├── COMMANDS.md                ← User guide for "/" slash commands
├── raw/                       ← Immutable source documents (LLM READ-ONLY)
│   ├── advisories/            ← CISA alerts, vendor security bulletins, threat intel briefs
│   ├── articles/              ← Clipped blog posts, research papers, DFIR case studies
│   ├── books_and_guides/      ← Cert notes (OSCP, CISSP, CEH), books, standards, cheat sheets
│   ├── writeups/              ← Lab reports, HackTheBox/TryHackMe walkthroughs, CTF solutions
│   ├── code_and_configs/      ← PoC scripts, Sigma rules, Snort/Suricata rules, Yara files
│   └── assets/                ← Architecture diagrams, attack flowcharts, screenshots
└── wiki/                      ← LLM-owned & maintained knowledge graph
    ├── index.md               ← Master categorized catalog (updated on EVERY ingest)
    ├── log.md                 ← Append-only chronological audit log
    ├── overview.md            ← High-level cybersecurity synthesis, threat landscape & philosophy
    ├── attacks/               ← MITRE ATT&CK techniques, offensive tactics, exploit chains
    ├── defenses/              ← Detection engineering, SIEM queries, hardening, Zero Trust
    ├── vulnerabilities/       ← CVE profiles, CWE root cause analysis, weaponization status
    ├── tools/                 ← Security tool dossiers (Nmap, Burp, BloodHound, Splunk, etc.)
    ├── architectures/         ← Cloud security, Active Directory, network design, IAM
    ├── writeups/              ← Structured lab debriefs, box breakdowns, IR tabletop notes
    ├── frameworks/            ← MITRE ATT&CK, NIST CSF, ISO 27001, OWASP Top 10, CIS
    ├── sources/               ← Per-source ingest summaries with key takeaways and change logs
    └── analyses/              ← Filed answers, comparative analyses, threat models, deep dives
```

---

## 3. Metadata & Page Conventions

Every markdown file in `wiki/` must begin with YAML frontmatter to support Obsidian Dataview, link graph navigation, and programmatic querying.

### Canonical Frontmatter Template

```yaml
---
title: "Descriptive Page Title"
type: attack | defense | vulnerability | tool | architecture | writeup | framework | source | analysis
tags:
  - cybersecurity
  - specific-domain # e.g., active-directory, web-security, cloud-iam, binary-exploitation
mitre_tactics: []   # e.g., [Initial Access, Privilege Escalation, Credential Access]
mitre_techniques: [] # e.g., [T1558.003]
severity: Critical | High | Medium | Low | Informational # Optional
source_count: 1
last_updated: YYYY-MM-DD
status: active | evolving | legacy | deprecated
related:
  - "[[wiki/attacks/example]]"
  - "[[wiki/defenses/example]]"
---
```

### Linking Standards
- Use Obsidian wikilinks: `[[relative/path/to/page]]` or `[[page-name]]`.
- Always link the **attacker technique**, **vulnerability**, **defensive mitigation**, **detection rule**, and **relevant tooling**.
- Preserve bidirectional context: if Page A links to Page B as a mitigation, ensure Page B references Page A under `Threats Mitigated`.

---

## 4. Standard Operational Workflows

### 🔵 1. INGEST (`/ingest <filepath or text>`)
When the user supplies an advisory, article, writeup, or drops a file into `raw/`:

1. **Inspect Source:** Read the raw content fully from `raw/` or the prompt.
2. **Extract Key Signals:**
   - Core threat/vulnerability/defense mechanism.
   - Attack vectors, prerequisites, impact.
   - Detection heuristics (event IDs, telemetry, log sources).
   - Mitigations & hardening guidance.
3. **Create Source Summary:** Save in `wiki/sources/<slug>.md`.
4. **Update or Create Entity Pages (Touches 3–12 pages):**
   - **Attacks:** Update or create page in `wiki/attacks/` (link MITRE ID).
   - **Vulnerabilities:** Update or create page in `wiki/vulnerabilities/` (link CVE/CWE).
   - **Defenses:** Add detection signatures/hardening into `wiki/defenses/`.
   - **Tools:** Update tool dossiers in `wiki/tools/` if novel usage or command switches appeared.
   - **Frameworks:** Link to relevant framework in `wiki/frameworks/`.
5. **Update `wiki/index.md`:** Ensure every new or heavily revised page is registered in the master index.
6. **Append to `wiki/log.md`:** Add an entry:
   `## [YYYY-MM-DD] ingest | <Source Title> | Added/updated: [[wiki/...]], [[wiki/...]]`
7. **Calibrate `wiki/overview.md`:** If this source updates the threat landscape or core operational doctrine, adjust `wiki/overview.md`.

---

### 🟢 2. QUERY (`/query <question>`)
When the user asks technical questions, seeks attack vectors, or requests mitigation architecture:

1. **Search Index First:** Scan `wiki/index.md` and relevant wiki pages.
2. **Synthesize Response:** Provide a deep, cited answer drawing directly from the compiled wiki files.
3. **Compound the Answer:** If the answer involves novel analysis, comparison, or architecture breakdown, **save it into `wiki/analyses/<analysis-slug>.md`** so the exploration becomes permanent.
4. **Log the Query:**
   `## [YYYY-MM-DD] query | <Question Summary> | Produced: [[wiki/analyses/...]]`

---

### 🟡 3. LINT (`/lint`)
Health check the wiki across all nodes:

1. **Check Broken Links & Orphans:** Find pages without incoming or outgoing wikilinks.
2. **Detect Contradictions:** Compare overlapping advice (e.g., deprecated TLS configs vs. modern zero-trust standards).
3. **Identify Defensive Blindspots:** Offensive techniques in `wiki/attacks/` lacking corresponding detection in `wiki/defenses/`.
4. **Spot Missing Tooling:** Techniques mentioning tools without a dedicated `wiki/tools/` dossier.
5. **Generate Remediation Plan:** Output a concise list of fixes and append summary to `wiki/log.md`.

---

### 🔴 4. THREAT MODEL (`/threat-model <system/component>`)
When assessing a system architecture:

1. Analyze components, data flows, trust boundaries, and protocols.
2. Apply **STRIDE** or **PASTA** methodology.
3. Map threats to existing `wiki/attacks/` and vulnerabilities to `wiki/vulnerabilities/`.
4. Produce a prioritized defensive matrix with links to `wiki/defenses/`.
5. File result as `wiki/analyses/threat-model-<target>.md`.

---

### 🟣 5. LAB DEBRIEF (`/lab-debrief <box/challenge>`)
When analyzing a solved machine (HTB, THM, Proving Grounds, CTF):

1. Break down the kill chain: Reconnaissance → Initial Foothold → Internal Enumeration → Privilege Escalation → Persistence.
2. Document exact commands, exploitation mechanics, and misconfigurations.
3. Extract generalizable principles: "Why was this vulnerable?" and "What telemetry would have alerted the SOC?".
4. File writeup in `wiki/writeups/<box-name>.md` and cross-link all exploited tools, vulnerabilities, and attacks.

---

### 🛡️ 6. DETECTION RULE GENERATION (`/detection-rule <technique>`)
When building defensive alerts:

1. Identify data source requirements (Windows Event Log IDs, Sysmon, Zeek, EDR sensors).
2. Write standardized detection logic (Sigma format, Splunk SPL, or YARA rule).
3. Document false positive baselines and tuning guidance.
4. Integrate rule into `wiki/defenses/` and cross-link back to the attack technique.

---

## 5. Domain Knowledge Taxonomies

To maintain organization, categorize nodes into these canonical pillars:

| Category | Primary Focus | Examples |
|---|---|---|
| **Attacks** | Offensive tradecraft, exploit chains, tactics | Kerberoasting, Pass-the-Hash, SQLi, SSRF, Process Injection, DLL Hijacking |
| **Defenses** | Detection rules, hardening, SIEM/SOAR, EDR, Zero Trust | Active Directory Hardening, Sigma Rules, AppLocker, Network Segmentation |
| **Vulnerabilities** | CVE root cause, memory corruption, logic flaws | Log4Shell, EternalBlue, Spring4Shell, Dirty COW, CWE-89 |
| **Tools** | Offensive and defensive tooling blueprints | Nmap, Burp Suite, BloodHound, Mimikatz, Ghidra, Wireshark, Splunk |
| **Architectures** | Enterprise, cloud, infrastructure topologies | Active Directory Forest, AWS Multi-Account IAM, Kubernetes RBAC, ZTA |
| **Frameworks** | Industry benchmarks and matrices | MITRE ATT&CK, NIST CSF, OWASP Top 10, CIS Benchmarks, CISSP CBK |
| **Writeups** | Practical lab and CTF breakdowns | HTB Forest, THM Kerberos, Real-World Breach Post-Mortems |
| **Analyses** | Syntheses, comparative analyses, threat models | EDR Evasion vs Detection, OAuth 2.0 Security Comparison |

---

## 6. Instructions for the LLM Agent

- **Never delete or overwrite raw sources** inside `raw/`.
- **Always update `wiki/index.md`** and **append to `wiki/log.md`** on operations.
- Avoid generic high-level fluff: include concrete commands, Windows Event IDs, Linux telemetry points, protocol specs, and code snippets.
- Use GitHub Flavored Markdown alerts (`> [!NOTE]`, `> [!WARNING]`, `> [!TIP]`, `> [!IMPORTANT]`) where critical.
- Cross-link rigorously: every technical term should strive to link to an established wiki page (`[[like this]]`).
