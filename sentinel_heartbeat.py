import os
import subprocess
import time

# [ArmstrongLogic Online]
# Security Clearance: LEVEL-OMEGA
# macOS M4 / SovereignVault v1.5.0

class SentinelHeartbeat:
    def __init__(self):
        self.repo_name = "SovereignVault"
        self.node_id = "M4-DEZ-AIR"

    def archive_logic(self):
        """Checks for local changes and pushes to the vault."""
        # Stage all changes (Roblox .rbxl snapshots, .py scripts, .zsh logs)
        subprocess.run(["git", "add", "."], capture_output=True)
        
        # Check if there is anything to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        
        if status.stdout.strip():
            print(f"[{time.ctime()}] Changes detected. Initiating Sovereign Archive...")
            commit_msg = f"ARCHITECT: Automated Pulse - {time.strftime('%Y-%m-%d %H:%M')}"
            subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True)
            
            # Atomic Push to origin
            push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
            if push.returncode == 0:
                print("[SUCCESS] Vault Synchronized.")
            else:
                print(f"[FAULT] Sync Error: {push.stderr.strip()}")
        else:
            print(f"[{time.ctime()}] No changes. System Nominal.")

    def run_forever(self):
        print(f"--- Sentinel Heartbeat v1.5.0 Active on {self.node_id} ---")
        while True:
            self.archive_logic()
            # 30-minute interval to balance M4 thermal efficiency and data safety
            time.sleep(1800)

if __name__ == "__main__":
    SentinelHeartbeat().run_forever()
