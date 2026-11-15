# CLAUDE.md — Agent Interface for Cybersecurity LLM Wiki

> This vault operates under the LLM Wiki Architecture.

Please read and strictly follow the master configuration and schema documented in **[[AGENTS.md]]**:
- **Domain:** Cybersecurity (Offensive Tradecraft, Defensive Engineering, Threat Intelligence, Detection Engineering, Vulnerability Research, Incident Response).
- **Core Rules:**
  1. Never modify or delete files in `raw/` (immutable source of truth).
  2. Maintain and compound knowledge inside `wiki/`.
  3. Every ingest, query, or operation must update `wiki/index.md` and `wiki/log.md`.
  4. Cross-link entities liberally with wikilinks (`[[page-name]]`).
  5. Check `COMMANDS.md` for slash commands workflows (`/ingest`, `/query`, `/lint`, `/threat-model`, `/cve`, `/lab-debrief`, `/detection-rule`).
