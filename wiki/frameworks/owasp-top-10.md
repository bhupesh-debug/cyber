---
title: "OWASP Top 10 Web Application Vulnerabilities"
type: framework
tags:
  - appsec
  - web-security
  - owasp
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/attacks/sql-injection]]"
  - "[[wiki/analyses/threat-model-web-auth]]"
---

# OWASP Top 10 Web Application Vulnerabilities

The Open Web Application Security Project (OWASP) Top 10 provides a standard awareness document for developers and security professionals representing the most critical security risks to web applications.

---

## The Core Risk Categories

1. **A01:2021 - Broken Access Control:** Users acting outside of intended permissions (IDOR, privilege escalation, bypass of access checks).
2. **A02:2021 - Cryptographic Failures:** Sensitive data exposure, transmission of plaintext data, weak cryptographic algorithms or hardcoded keys.
3. **A03:2021 - Injection:** Cross-site scripting (XSS), SQL Injection (`[[wiki/attacks/sql-injection]]`), Command Injection, and ORM injection.
4. **A04:2021 - Insecure Design:** Missing threat modeling, architectural flaws, absence of rate-limiting, untrusted business logic.
5. **A05:2021 - Security Misconfiguration:** Unhardened cloud permissions, default accounts/passwords, overly verbose error messages, open S3 buckets.
6. **A06:2021 - Vulnerable and Outdated Components:** Using third-party libraries or frameworks with known CVEs (`[[wiki/vulnerabilities/log4shell-cve-2021-44228]]`).
7. **A07:2021 - Identification and Authentication Failures:** Permitting brute force, credential stuffing, missing multi-factor authentication, session fixation.
8. **A08:2021 - Software and Data Integrity Failures:** Unsigned auto-updates, insecure deserialization, untrusted CI/CD pipelines.
9. **A09:2021 - Security Logging and Monitoring Failures:** Insufficient logging of authentication attempts, failure to trigger SOC alerts on malicious activity.
10. **A10:2021 - Server-Side Request Forgery (SSRF):** Web applications fetching remote resources without validating the user-supplied URL (exploiting cloud metadata endpoints like `http://169.254.169.254/`).

---

## Defensive Countermeasures
- Parameterized queries and prepared statements for injection prevention.
- Enforce Zero Trust token validation (OAuth 2.0 / JWT signed with RS256/ES256).
- Rigorous threat modeling (`[[wiki/analyses/threat-model-web-auth]]`).
