---
title: "BloodHound Active Directory Attack Path Analysis"
type: tool
tags:
  - active-directory
  - red-team
  - blue-team
  - graph-theory
source_count: 1
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/attacks/kerberoasting]]"
  - "[[wiki/defenses/active-directory-hardening]]"
---

# BloodHound Active Directory Attack Path Analysis

BloodHound is an Active Directory and Azure/Entra ID graph analysis tool. It uses graph theory to reveal hidden and unintended relationships, permissions, and attack paths within an Active Directory domain.

---

## 1. Architecture

- **Data Ingestors (Collectors):** SharpHound (C# binary or PowerShell script) or BloodHound.py (Python). They query Active Directory using LDAP, RPC, and SAMR protocols.
- **Database Backend:** Neo4j graph database storing nodes (Users, Groups, Computers, Domains, OUs, GPOs) and edges (MemberOf, GenericAll, WriteDacl, AdminTo, CanRDP, HasSession).
- **Frontend Client:** Electron / React application for visual graph querying and Cypher queries.

---

## 2. Ingestion & Collection

From an authenticated Windows domain-joined machine:
```powershell
.\SharpHound.exe -c All --outputdirectory C:\Temp --zipfilename domain_data
```

From an authenticated Linux machine (using BloodHound.py):
```bash
bloodhound-python -u 'jdoe' -p 'Password123' -d 'corp.local' -ns 10.10.10.1 -c All --zip
```

---

## 3. High-Yield Cypher Queries

### Find Shortest Path to Domain Admins
```cypher
MATCH p=shortestPath((n:User)-[r:MemberOf|HasSession|AdminTo*1..]->(m:Group {name:'DOMAIN ADMINS@CORP.LOCAL'}))
RETURN p
```

### Find Kerberoastable Users with Path to High-Value Targets
```cypher
MATCH (u:User {hasspn:true})
MATCH (g:Group {name:'DOMAIN ADMINS@CORP.LOCAL'})
MATCH p=shortestPath((u)-[*1..]->(g))
RETURN p
```

---

## 4. Blue Team Applications

Defenders use BloodHound for **Attack Path Management (APM)**:
1. **Identify Shadow Admins:** Accounts that are not members of `Domain Admins` but possess `GenericAll` or `WriteDacl` permissions over high-privileged groups.
2. **Eliminate Transitive Sessions:** Pinpoint workstations where Domain Admins leave active sessions exposed to local administrator compromise.
3. **Audit Group Nesting:** Collapse convoluted group inheritance structures.
