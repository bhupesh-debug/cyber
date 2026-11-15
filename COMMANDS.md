# COMMANDS.md — Slash Command Reference Guide

This guide details how to operate your **Cybersecurity LLM Wiki** using natural slash commands. When working with your agent (Antigravity, Claude Code, Gemini CLI, OpenCode, Codex), you simply type or prefix your prompt with one of these commands.

The agent reads `AGENTS.md` and executes the corresponding workflow, updating your Obsidian graph automatically.

---

## Quick Reference Table

| Command | Action | Primary Output | Files Touched |
| :--- | :--- | :--- | :--- |
| **`/ingest`** | Ingest raw advisory, article, writeup, or book | Extracts takeaways, cross-links concepts | `wiki/sources/`, `wiki/attacks/`, `wiki/defenses/`, `index.md`, `log.md` |
| **`/query`** | Deep question answering across the wiki | High-context synthesized answer + filed analysis | `wiki/analyses/` (if compounding), `log.md` |
| **`/lint`** | Health check & consistency audit | Contradiction, orphan, and blindspot report | `wiki/log.md` |
| **`/threat-model`** | Architecture STRIDE/PASTA threat modeling | Actionable threat matrix & mitigations | `wiki/analyses/threat-model-<target>.md`, `index.md`, `log.md` |
| **`/cve`** | Deep dive into a specific CVE / vulnerability | Technical root cause, PoC status, detection rules | `wiki/vulnerabilities/<cve>.md`, `wiki/defenses/`, `index.md`, `log.md` |
| **`/lab-debrief`** | Turn HTB/THM/CTF lab solutions into skills | Kill chain analysis, tradecraft & SOC telemetry | `wiki/writeups/<box>.md`, `wiki/tools/`, `index.md`, `log.md` |
| **`/detection-rule`** | Craft Sigma / YARA / SPL detection signatures | Formatted detection rules + telemetry requirements | `wiki/defenses/<rule>.md`, `wiki/attacks/`, `index.md`, `log.md` |
| **`/synthesize`** | Aggregate cross-cutting topics | Comprehensive doctrine / comparison paper | `wiki/analyses/<topic>.md`, `index.md`, `log.md` |
| **`/cert-prep`** | Generate exam drill & syllabus mapping | Flashcards, attack-defense cheat sheet | `wiki/analyses/cert-<exam>.md`, `index.md`, `log.md` |
| **`/overview-update`**| Re-calibrate master cybersecurity thesis | Updates `wiki/overview.md` with latest trends | `wiki/overview.md`, `log.md` |

---

## 1. `/ingest` — Ingest a New Source

### Purpose
Takes a new piece of raw cybersecurity intelligence (a CISA alert, security blog, pentest report, research paper, or tool documentation), reads it, builds a permanent source summary, and updates all related attack, defense, tool, and architecture pages.

### Syntax
```text
/ingest <path-in-raw-or-url-or-pasted-text>
```

### Examples
- `/ingest raw/advisories/cisa-alert-aa24-active-directory.pdf`
- `/ingest raw/articles/dirty-pipe-root-cause-analysis.md`
- `/ingest https://embracethered.com/blog/posts/2024/kerberoasting-deep-dive/`
- `/ingest [Pasted text of a vendor patch bulletin]`

### What the Agent Does
1. Reads the source without modifying it in `raw/`.
2. Extracts core threat mechanics, affected systems, prerequisites, detection heuristics, and mitigations.
3. Creates a new summary at `wiki/sources/<slug>.md`.
4. Finds related pages in `wiki/attacks/`, `wiki/defenses/`, `wiki/vulnerabilities/`, and `wiki/tools/`, adding the newly gained context. If new concepts appear, creates dedicated atomic pages.
5. Updates `wiki/index.md` and appends an entry to `wiki/log.md`.

---

## 2. `/query` — Knowledge Base Synthesis

### Purpose
Queries your compounding knowledge base rather than general internet data. The agent traverses your internal markdown notes, synthesizes insights, provides internal citations, and saves valuable analyses so they don't disappear into chat history.

### Syntax
```text
/query <your technical cybersecurity question>
```

### Examples
- `/query What are the primary bypasses for AMSI in our notes and how are we currently detecting them?`
- `/query Compare pass-the-hash vs pass-the-ticket: mechanics, detection event IDs, and mitigation strategies.`
- `/query Which active directory attack paths lead to Domain Admin without requiring unconstrained delegation?`

### What the Agent Does
1. Checks `wiki/index.md` to locate all relevant pages across attacks, defenses, tools, and writeups.
2. Reads the files and synthesizes an authoritative answer with `[[wikilinks]]`.
3. If the answer provides a valuable strategic comparison, it files it permanently into `wiki/analyses/<analysis-title>.md`.
4. Logs the query in `wiki/log.md`.

---

## 3. `/lint` — Vault Health Check & Graph Audit

### Purpose
Audits the wiki for inconsistencies, missing backlinks, orphan files, and defensive blindspots (e.g., attacks documented without corresponding detection rules).

### Syntax
```text
/lint
```

### What the Agent Does
1. Scans `wiki/` for:
   - **Orphans:** Pages with zero incoming links.
   - **Contradictions:** Conflicting guidance (e.g., outdated crypto recommendations).
   - **Defensive Blindspots:** Attacks documented in `wiki/attacks/` lacking detection entries in `wiki/defenses/`.
   - **Missing Tools:** Common tools mentioned without a profile in `wiki/tools/`.
   - **Stale CVEs:** Unpatched or evolving zero-days needing updated exploit telemetry.
2. Emits a clean prioritized report in chat.
3. Logs the audit pass in `wiki/log.md`.

---

## 4. `/threat-model` — Architectural Threat Assessment

### Purpose
Performs a rigorous STRIDE or PASTA threat modeling assessment on an application, enterprise infrastructure, cloud environment, or network design.

### Syntax
```text
/threat-model <system-description-or-file>
```

### Examples
- `/threat-model Banking API with OAuth 2.0 PKCE, AWS API Gateway, and Lambda microservices`
- `/threat-model raw/code_and_configs/k8s-multi-tenant-cluster.yaml`

### What the Agent Does
1. Deconstructs data flows, trust boundaries, entry points, and privileged assets.
2. Identifies specific threats across Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.
3. Links threats to existing `wiki/attacks/` and `wiki/frameworks/owasp-top-10`.
4. Delivers an actionable mitigation roadmap mapped to `wiki/defenses/`.
5. Files the assessment in `wiki/analyses/threat-model-<target-slug>.md` and updates `wiki/index.md`.

---

## 5. `/cve` — Deep Vulnerability Analysis

### Purpose
Generates a comprehensive technical dossier on a CVE: root-cause breakdown at the memory/logic level, exploitation mechanics, weaponization status in the wild, and defensive signatures.

### Syntax
```text
/cve <CVE-ID>
```

### Examples
- `/cve CVE-2021-44228` (Log4Shell)
- `/cve CVE-2023-38831` (WinRAR Code Execution)
- `/cve CVE-2024-3094` (XZ Utils Backdoor)

### What the Agent Does
1. Researches and documents the CWE, CVSS v3/v4 score, vulnerable functions, and memory layout/protocol breakdown.
2. Checks exploit availability (PoC, Metasploit, actively exploited in the wild / CISA KEV).
3. Drafts defensive detection signatures (YARA, Snort, or Sigma).
4. Creates `wiki/vulnerabilities/<cve-slug>.md`, links it to affected `wiki/tools/` or `wiki/architectures/`, updates `wiki/index.md`, and logs the event.

---

## 6. `/lab-debrief` — Box Walkthrough & CTF Translation

### Purpose
Translates a raw lab walkthrough (HackTheBox, TryHackMe, OffSec Proving Grounds, PortSwigger Web Security Academy) into compounding offensive tradecraft and defensive lessons.

### Syntax
```text
/lab-debrief <box-name-or-filepath>
```

### Examples
- `/lab-debrief raw/writeups/htb-forest-walkthrough.md`
- `/lab-debrief PortSwigger Lab: Blind SQL injection with out-of-band data exfiltration`

### What the Agent Does
1. Maps the machine's full attack path:
   - External Recon & Port Enumeration.
   - Initial Access Vector.
   - Internal Lateral Movement & PrivEsc.
2. Extracts generalizable tactics and updates tool dossiers in `wiki/tools/`.
3. Adds "SOC Defense Takeaways": What exact Windows Event IDs or Linux auditd logs would catch this attack chain?
4. Files the writeup in `wiki/writeups/<box-name>.md` and updates `wiki/index.md`.

---

## 7. `/detection-rule` — SIEM, Sigma & YARA Engineering

### Purpose
Develops production-grade detection logic mapped to a MITRE ATT&CK technique or offensive playbook.

### Syntax
```text
/detection-rule <technique-or-behavior>
```

### Examples
- `/detection-rule T1003.001 LSASS Memory Dumping via MiniDumpWriteDump`
- `/detection-rule Unusually high Kerberos TGS requests for service accounts (Kerberoasting)`
- `/detection-rule Suspicious PowerShell downloading external payload with WebClient`

### What the Agent Does
1. Identifies the required telemetry (e.g., Sysmon Event ID 10, Windows Security Event ID 4769, Auditd `sys_execve`).
2. Generates standard **Sigma**, **Splunk SPL**, or **YARA** detection code.
3. Documents tuning tips, false positive edge cases, and testing commands.
4. Saves rule to `wiki/defenses/detection-<technique-slug>.md` and links back to `wiki/attacks/`.

---

## 8. `/cert-prep` — Exam Syllabus & Skills Drills

### Purpose
Accelerates study and practical preparation for certifications (OSCP, OSEP, CISSP, CEH, Sec+, PNPT, CRTO).

### Syntax
```text
/cert-prep <cert-name> <focus-area>
```

### Examples
- `/cert-prep OSCP Active Directory exploitation chains and pivoting`
- `/cert-prep CISSP Domain 3 Security Architecture and Engineering`
- `/cert-prep CRTO Cobalt Strike beacon payload staging and evasion`

### What the Agent Does
1. Cross-references the official exam syllabus with your existing wiki pages.
2. Highlights knowledge gaps and untested commands.
3. Generates high-yield command cheat sheets, concept flashcards, and step-by-step methodologies.
4. Files the drill guide into `wiki/analyses/cert-<cert-name>-<focus>.md`.

---

## 9. Obsidian Tips & Best Practices

- **Side-by-Side Dual Pane:** Keep your LLM agent on one side of your monitor and **Obsidian** on the other. Watch the files update and links light up in real time!
- **Obsidian Graph View:** Open Graph View (`Ctrl + G`). Color-code your graph by directory:
  - `path:wiki/attacks` → Red
  - `path:wiki/defenses` → Blue
  - `path:wiki/vulnerabilities` → Orange
  - `path:wiki/tools` → Green
  - `path:wiki/frameworks` → Purple
- **Web Clipper:** Use the Obsidian Web Clipper extension to grab writeups, CISA alerts, and CVE disclosures directly into `raw/articles/` or `raw/advisories/`.
- **Dataview Queries:** All wiki pages have YAML frontmatter (`type`, `tags`, `mitre_tactics`, `severity`, `last_updated`). You can create instant dynamic dashboard tables anywhere in Obsidian.
