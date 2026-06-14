from app.ai.gemini_client import model
from app.ai.prompts import SYSTEM_PROMPT


def analyze_security(findings, drifts):

    prompt = f"""
{SYSTEM_PROMPT}

Findings:

{findings}

Drifts:

{drifts}
"""

    response = model.generate_content(prompt)

    return response.text