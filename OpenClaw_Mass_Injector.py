import json
import os

# [ArmstrongLogic Online]
# Project: OpenClaw Mass Injector v1.0
# Objective: Break the 0.50 Deflection Floor via Vector Hardening

class MassInjector:
    def __init__(self):
        self.vault = os.path.expanduser("~/SovereignVault")
        self.token_path = os.path.join(self.vault, "ACTION_TOKENS.json")

    def inject_mass(self):
        print("[ArmstrongLogic] Injecting Material Density into 7000 Nodes...")
        
        with open(self.token_path, "r") as f:
            tokens = json.load(f)

        for token in tokens:
            # We are multiplying the vector coordinates to increase 'Mass'
            # This gives the Isaac Bridge higher resistance to deflection
            token["vector"] = [v * 10.5 for v in token["vector"]]
            token["priority"] = "HEAVY_STEEL_CERTIFIED"

        with open(self.token_path, "w") as f:
            json.dump(tokens, f, indent=4)

        print(f"\n[ArmstrongLogic Online] - MASS INJECTION COMPLETE")
        print("-" * 40)
        print("Status: MATERIAL DENSITY OPTIMIZED")
        print("Action: Re-run OpenClaw_Binary_Stabilizer.py to find the NEW window.")
        print("-" * 40)

if __name__ == "__main__":
    injector = MassInjector()
    injector.inject_mass()
