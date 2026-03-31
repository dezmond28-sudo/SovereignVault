import pandas as pd
import os

# [ArmstrongLogic Online]
# Sentinel Module: Ticket Generator v1.0.2
# Security Clearance: LEVEL-OMEGA

class TicketGenerator:
    def __init__(self):
        self.vault = os.path.expanduser("~/SovereignVault")
        self.targets_path = os.path.join(self.vault, "RECOVERY_TARGETS.csv")
        self.output_path = os.path.join(self.vault, "TICKET_DRAFT.txt")

    def generate(self):
        if not os.path.exists(self.targets_path):
            print("[CRITICAL] No targets found. Run Prophet first.")
            return

        df = pd.read_csv(self.targets_path)
        total_leak = df['leak_amount'].sum()
        
        ticket_body = f"""
SUBJECT: Formal Inquiry - Commission Settlement Discrepancy
TOTAL DISCREPANCY: ${total_leak:,.2f}

To the Support Team,

My automated audit system (Prophet v2.1) has identified a settlement delta across {len(df)} transactions. 
The expected commission totals do not match the settled payouts.

Discrepancy Details:
{df[['order_id', 'leak_amount']].to_string(index=False)}

Please review these Order IDs and adjust the settlement to achieve parity.
Reference: ArmstrongLogic SovereignVault Audit {os.urandom(4).hex().upper()}
        """
        
        with open(self.output_path, "w") as f:
            f.write(ticket_body)
        
        print(f"\n[SENTINEL] Ticket Draft Generated: {self.output_path}")
        print("-" * 30)
        print(ticket_body)

if __name__ == "__main__":
    gen = TicketGenerator()
    gen.generate()
