import re
from dataclasses import dataclass

PATTERNS = {
    "EMAIL": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "IP_ADDRESS": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "PHONE": re.compile(r"(?<!\w)(?:\+?\d[\d ()-]{7,}\d)(?!\w)"),
}


@dataclass(frozen=True)
class RedactionResult:
    text: str
    counts: dict[str, int]


def redact_pii(text: str) -> RedactionResult:
    redacted = text
    counts: dict[str, int] = {}
    for label, pattern in PATTERNS.items():
        redacted, count = pattern.subn(f"[{label}]", redacted)
        if count:
            counts[label] = count
    return RedactionResult(text=redacted, counts=counts)
