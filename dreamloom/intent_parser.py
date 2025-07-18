# dreamloom/intent_parser.py
# Parses user text or voice input into structured system blueprint

import json

class IntentParser:
    def __init__(self):
        self.templates = {
            "dashboard": ["analytics panel", "mood tracker", "quantum ripple map"],
            "marketplace": ["listing grid", "emotion filter", "neural exchange bar"]
        }

    def parse(self, prompt: str) -> dict:
        system = {
            "name": "SynthRealm",
            "features": [],
            "tone": "Inspirational",
            "layout": "Modular mesh"
        }
        for keyword, modules in self.templates.items():
            if keyword in prompt.lower():
                system["features"].extend(modules)
        return system

# Example usage:
if __name__ == "__main__":
    parser = IntentParser()
    blueprint = parser.parse("Create a mood-reactive marketplace")
    print(json.dumps(blueprint, indent=2))
