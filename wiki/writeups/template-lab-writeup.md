---
title: "Lab Writeup Template & Kill Chain Blueprint"
type: writeup
tags:
  - writeup
  - lab
  - methodology
  - ctf
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/tools/nmap]]"
  - "[[wiki/attacks/kerberoasting]]"
  - "[[wiki/defenses/detection-engineering]]"
---

# Lab Writeup Template & Kill Chain Blueprint

> Use this template when logging HackTheBox, TryHackMe, Proving Grounds, or CTF challenges with the `/lab-debrief` slash command.

---

## Box Profile
- **Target Name:** `[Machine Name]`
- **Platform:** HackTheBox / TryHackMe / OffSec PG
- **Operating System:** Windows / Linux
- **Difficulty:** Easy / Medium / Hard / Insane
- **Primary Skills Practiced:** e.g., Active Directory, SQLi, Buffer Overflow, Binary Exploitation

---

## 1. Phase 1: External Reconnaissance
- Nmap discovery scan results:
  ```bash
  # Command executed
  ```
- Open ports and services identified:
  - Port 80 (HTTP - Apache 2.4.49)
  - Port 445 (SMB)
  - Port 88 (Kerberos)

---

## 2. Phase 2: Initial Foothold
- **Vulnerability / Misconfiguration:** `[[wiki/attacks/...]]` or `[[wiki/vulnerabilities/...]]`
- **Exploit Proof of Concept:**
  ```python
  # Exploit script or curl payload
  ```
- **Shell Acquired:** Low-privilege user (e.g. `www-data` or `corp\jdoe`).

---

## 3. Phase 3: Internal Enumeration & Privilege Escalation
- Automated discovery tooling used: `[[wiki/tools/bloodhound]]`, LinPEAS, or WinPEAS.
- Path to root / SYSTEM:
  - Sudo misconfiguration / Unquoted service path / Token impersonation.
- Final command execution:
  ```bash
  # Root execution
  ```

---

## 4. SOC Defensive Takeaways
- **What logged this activity?**
  - Windows Event ID 4688 / Sysmon Event ID 1 for suspicious parent-child process.
- **Recommended Sigma detection:** `[[wiki/defenses/...]]`
- **Hardening guidance:** How to permanently eliminate the root flaw.
