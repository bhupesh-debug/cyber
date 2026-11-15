---
title: "Threat Model: Modern Web Authentication & API Architecture"
type: analysis
tags:
  - threat-model
  - stride
  - auth
  - web-security
source_count: 2
last_updated: 2026-11-13
status: active
related:
  - "[[wiki/frameworks/owasp-top-10]]"
  - "[[wiki/attacks/sql-injection]]"
  - "[[wiki/architectures/zero-trust-architecture]]"
---

# Threat Model: Modern Web Authentication & API Architecture

This analysis documents a reference STRIDE threat model evaluating an enterprise Single Page Application (SPA) communicating with microservices via an API Gateway and OAuth 2.0 / OIDC Identity Provider.

---

## 1. System Architecture & Trust Boundaries

```mermaid
flowchart LR
    User["Client Browser (SPA)"]
    Gateway["API Gateway / PEP"]
    IdP["OIDC Identity Provider (Okta / Auth0)"]
    ServiceA["User Microservice"]
    ServiceB["Payment Microservice"]
    DB[("Customer Database")]

    User -->|1. Auth Redirect| IdP
    IdP -->|2. Issue JWT (Access + ID)| User
    User -->|3. Bearer JWT over HTTPS| Gateway
    Gateway -->|4. Validate Signature & Route| ServiceA
    Gateway -->|4. Validate Signature & Route| ServiceB
    ServiceA -->|5. SQL Query| DB
```

---

## 2. STRIDE Threat Analysis Matrix

| Threat Category | Specific Attack Vector | Risk Level | Mitigation Architecture |
| :--- | :--- | :--- | :--- |
| **Spoofing** | JWT token theft via Cross-Site Scripting (XSS) in local storage | High | Store tokens in `HttpOnly`, `SameSite=Strict`, `Secure` cookies; implement strict Content-Security-Policy (CSP). |
| **Tampering** | Parameter manipulation or algorithm switching (`alg: none`) in JWT header | Critical | Enforce explicit asymmetric verification (RS256/ES256) at API Gateway; reject `none` and symmetric fallback. |
| **Repudiation** | Lack of immutable audit logging on privileged transactions (e.g. fund transfers) | Medium | Ship structured, tamper-proof logs to centralized WORM (Write Once Read Many) SIEM storage. |
| **Information Disclosure** | Verbose error stack traces leaking database schematics | High | Configure global exception interceptors to sanitize public errors; store detailed traces only in internal logs. |
| **Denial of Service** | Credential stuffing on login endpoints | High | IP and account-based adaptive rate limiting, Web Application Firewall (WAF), CAPTCHA tripwires. |
| **Elevation of Privilege** | Insecure Direct Object References (IDOR) on `/api/v1/users/{id}` | Critical | Enforce server-side contextual authorization: check `jwt.sub == request.resource.owner_id` on every query. |
