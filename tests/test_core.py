from pii_redaction_toolkit import redact_pii


def test_redacts_supported_identifiers():
    result = redact_pii("Email me@site.com or call +91 85258 83729 from 10.0.0.1")
    assert "me@site.com" not in result.text
    assert "+91 85258 83729" not in result.text
    assert "10.0.0.1" not in result.text
    assert result.counts == {"EMAIL": 1, "IP_ADDRESS": 1, "PHONE": 1}


def test_leaves_safe_text_unchanged():
    result = redact_pii("No identifiers here")
    assert result.text == "No identifiers here"
    assert result.counts == {}
