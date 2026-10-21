# Threat model (summary)

Cairn reads untrusted text (source trees, imported skills, documentation, web pages) and can run commands, so it is exposed to prompt injection and unsafe actions.

| Threat | Example | Mitigation |
|---|---|---|
| Prompt injection via source or docs | a comment in a file tells the agent to run a command | all file content is data; instructions inside it are ignored and reported |
| Malicious imported skill | an imported skill contains hidden instructions or network calls | quarantine, static scan, operator review, activation only through the consent gate |
| Destructive actions | dropping a database, deleting volumes, force-push | container scope limited to declared dev containers; destructive actions always ask; deny rules in permissions |
| Secret exposure | tokens written to memory, logs or exports | secrets only in environment files; hooks block printing them; exports exclude them |
| Silent agent drift | skills added or changed without notice | consent gate, checkpoints before every change, versioned rollback |
| Data leakage between projects | project facts promoted into core | layer isolation and approved promotion only |
| Supply chain | untrusted dependencies or scripts | pinned dependencies, review before install, scan of imports |
| Publishing sensitive material | memory derived from proprietary source pushed to a public repo | allowlist-based public export and a pre-publish audit |

## Out of scope

Hooks and permission rules are guardrails, not a security boundary. Running Cairn against production systems is unsupported.
