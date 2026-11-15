---
title: "Nmap (Network Mapper) Blueprint"
type: tool
tags:
  - reconnaissance
  - networking
  - port-scanning
  - nmap
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/frameworks/mitre-attack]]"
  - "[[wiki/defenses/detection-engineering]]"
---

# Nmap (Network Mapper) Blueprint

Nmap is the industry standard utility for network discovery and vulnerability scanning. It utilizes raw IP packets in novel ways to determine what hosts are available on the network, what services they offer, and what operating systems they are running.

---

## 1. High-Yield Command Profiles

### Rapid Full-Port Scan (Offensive Reconnaissance)
```bash
nmap -p- --min-rate 1000 -T4 -oN scans/all_ports.txt 10.10.10.50
```

### Comprehensive Service & Script Enumeration
```bash
nmap -sC -sV -p 22,80,443,445,3389 -O -oA scans/detailed_scan 10.10.10.50
```

### Stealth SYN Scan with Decoys
```bash
nmap -sS -D RND:5 -g 53 -Pn 10.10.10.50
```

### Vulnerability Script Engine (NSE)
```bash
nmap --script "vuln and safe" -p 80,443,445 10.10.10.50
```

---

## 2. Key Flags Reference

| Flag | Purpose | Operational Note |
| :--- | :--- | :--- |
| `-sS` | TCP SYN (Stealth) scan | Default as root; does not complete full 3-way TCP handshake |
| `-sT` | TCP Connect scan | Used when unprivileged; completes full handshake |
| `-sU` | UDP scan | Slow; critical for DNS (53), SNMP (161), Kerberos (88) |
| `-sV` | Version detection | Probes open ports to determine service name and version |
| `-sC` | Default scripts | Runs standard collection of NSE scripts |
| `-O` | OS detection | Fingerprints TCP/IP stack options |
| `-Pn` | Skip host discovery | Treat all hosts as online (bypasses ICMP blocks) |

---

## 3. Defensive Detection

- **Firewall & IDS (Suricata/Snort):** Detect rapid SYN packets with no subsequent ACK.
- **Rate-Limiting:** Configure iptables or Cisco ASA to drop sources exceeding 50 SYN packets/second.
