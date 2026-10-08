# PII Redaction Toolkit

A lightweight preprocessing utility that masks common email, phone, and IP-address patterns before text reaches logs or AI services.

## Highlights

- Deterministic labeled replacements
- Per-category redaction counts
- Case-insensitive email matching
- No runtime dependencies

```python
from pii_redaction_toolkit import redact_pii

safe = redact_pii(raw_text)
print(safe.text, safe.counts)
```

Pattern matching cannot identify every form of sensitive data; production systems should combine it with policy, access controls, and specialized detectors.

No license has been selected; all rights are reserved.
