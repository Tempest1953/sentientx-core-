# intent_parser.py

import re

class IntentParser:
    """
    Parses user commands or logs to determine application-level intents.
    Designed for security audit and classification pipelines.
    """

    def __init__(self):
        self.intent_patterns = {
            "AUTH_EVENT": [r"\b(login|sign in|auth)\b"],
            "DATA_EXFIL": [r"\b(upload|export|send file)\b"],
            "PRIV_ESCALATION": [r"\b(root access|admin|sudo)\b"],
            "CONFIG_CHANGE": [r"\b(change settings|reconfigure|edit config)\b"]
        }

    def parse(self, text: str) -> str:
        """
        Analyzes input string and returns the detected intent label.
        Returns 'UNKNOWN' if no intent matches.
        """
        clean_text = text.strip().lower()

        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, clean_text):
                    return intent
        return "UNKNOWN"
