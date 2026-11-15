---
title: "Security Scanners & Static Analysis Suite"
type: tool
tags:
  - sast
  - tool-suite
  - semgrep
  - gitleaks
  - trivy
  - yara
source_count: 2
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/defenses/vulnerability-auditing-methodology]]"
  - "[[wiki/defenses/automated-security-reporting]]"
---

# Security Scanners & Static Analysis Suite

This document indexes the essential automated scanning tools utilized during workspace and sandbox security audits, detailing their specific focus areas, invocation commands, and telemetry formats.

---

## 1. Scanner Directory & Capabilities

| Tool | Focus Area | Primary Targets | Execution Mode |
| :--- | :--- | :--- | :--- |
| **Semgrep** | Fast SAST semantic code analysis | Python, JS/TS, Go, Java, C#, PHP | Static code scanning |
| **Gitleaks** | High-entropy secrets and token detection | Git repos, `.env`, configs, JSON/YAML | Static pattern matching |
| **Trivy** | Vulnerability & misconfiguration scanner | Containers, dependencies, IaC, OS packages | Local DB lookup |
| **OSV-Scanner** | Open source vulnerability database lookup | Lockfiles (`package-lock`, `Cargo.lock`, `Pipfile`) | CVE/GHSA lookup |
| **YARA** | Malware pattern matching & file signatures | Binaries, scripts, suspicious documents | Rule-based string/byte scan |
| **Bandit** | Python-specific AST security linter | `.py` source trees | Static AST parsing |
| **Checkov** | Infrastructure-as-Code (IaC) security | Terraform, CloudFormation, Kubernetes, Docker | Static AST & policy eval |

---

## 2. Command Reference

### Semgrep (Code Flaws & Injections)
```bash
# Scan whole directory using auto-selected standard security rules
semgrep scan --config auto --json -o semgrep-results.json .
```

### Gitleaks (Hardcoded Credentials)
```bash
# Detect uncommitted or hardcoded secrets in current directory
gitleaks detect --source . --verbose --report-format json --report-path gitleaks-report.json
```

### Trivy (Dependencies & Filesystem)
```bash
# Audit filesystem for vulnerable packages and misconfigurations
trivy fs --scanners vuln,misconfig,secret --format json -o trivy-report.json .
```

### OSV-Scanner (Supply Chain CVEs)
```bash
# Scan all lockfiles in the repository
osv-scanner -r --format json . > osv-report.json
```

---

## 3. Graceful Fallback Strategy
When a tool is not installed in the operating environment, the agent must:
1. Disclose the tool limitation explicitly in the audit report.
2. Fall back to heuristic regex/AST script parsing using Python standard libraries (e.g., Python `ast` module for Python scripts, regex pattern banks for secrets).
3. Never fabricate scan results.
