---
title: "SQL Injection (SQLi)"
type: attack
tags:
  - web-security
  - injection
  - appsec
  - owasp
mitre_tactics:
  - Initial Access
mitre_techniques:
  - T1190
severity: Critical
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/frameworks/owasp-top-10]]"
  - "[[wiki/analyses/threat-model-web-auth]]"
---

# SQL Injection (SQLi)

## 1. Core Mechanics

SQL Injection occurs when untrusted user input is directly concatenated or interpolated into a dynamic database query rather than being treated as separate parameter data. This allows an attacker to alter the query logic, execute administrative commands, read arbitrary tables, bypass authentication, and occasionally achieve remote code execution (e.g., via `xp_cmdshell` or `INTO OUTFILE`).

---

## 2. Exploitation Variants

1. **In-Band SQLi (Classic):**
   - **Error-Based:** Inducing database errors (e.g. division by zero, conversion errors) to leak table contents directly in error responses.
   - **UNION-Based:** Appending results from arbitrary tables using `UNION SELECT ...`.
2. **Inferential SQLi (Blind):**
   - **Boolean-Based:** Inferring characters of data by evaluating true/false HTTP response variations.
   - **Time-Based:** Forcing database sleeps (e.g. `pg_sleep(5)`, `WAITFOR DELAY '0:0:5'`) to infer data bit-by-bit.
3. **Out-of-Band (OAST):** Triggering DNS or HTTP requests from the database server to an external listener (e.g., PortSwigger Collaborator, interactsh).

---

## 3. Defensive Countermeasures

> [!IMPORTANT]
> Input sanitization or blacklisting is insufficient. Parameterization is mandatory.

- **Parameterized Queries (Prepared Statements):** Ensure database engines compile query structures prior to binding parameter variables.
  ```python
  # SECURE EXAMPLE (Python psycopg2 / sqlite3)
  cursor.execute("SELECT id, username FROM users WHERE username = %s AND password_hash = %s", (username, pwd_hash))
  ```
- **Object-Relational Mapping (ORM):** Use modern ORMs (SQLAlchemy, Prisma, Hibernate) correctly without falling back on raw SQL string interpolation.
- **Principle of Least Privilege:** Database application accounts must never run as `sa`, `root`, or `DBA`. Restrict access only to required tables.
- **Web Application Firewall (WAF):** Provides defense-in-depth inspection of HTTP GET/POST payloads for known SQL injection heuristics.
