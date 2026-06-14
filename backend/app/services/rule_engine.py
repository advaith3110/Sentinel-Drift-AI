def analyze_security(config):

    findings = []

    # Rule 1
    if config.get("public") is True:
        findings.append({
            "severity": "Critical",
            "issue": "Resource is publicly accessible"
        })

    # Rule 2
    if config.get("encrypted") is False:
        findings.append({
            "severity": "High",
            "issue": "Encryption is disabled"
        })

    # Rule 3
    if config.get("root_access") is True:
        findings.append({
            "severity": "Critical",
            "issue": "Root access is enabled"
        })

    return findings