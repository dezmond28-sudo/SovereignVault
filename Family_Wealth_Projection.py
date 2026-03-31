import numpy as np

# [ArmstrongLogic Online]
# Strategic Wealth Projection v1.0.0
# Objective: Generational Security for the Armstrong Family

class WealthScientist:
    def __init__(self, current_savings, monthly_contribution):
        self.principal = current_savings
        self.monthly = monthly_contribution
        self.rate = 0.08  # 8% Average Market Return

    def project_trajectory(self, years=28):
        months = years * 12
        monthly_rate = self.rate / 12
        
        # Compound Interest Formula for Monthly Contributions
        future_value = self.principal * (1 + monthly_rate)**months + \
                       self.monthly * (((1 + monthly_rate)**months - 1) / monthly_rate)
        
        print(f"\n[ArmstrongLogic Online]")
        print(f"REPORT: Generational Wealth Forecast")
        print(f"TARGET YEAR: {2026 + years}")
        print(f"PROJECTED VAULT: ${future_value:,.2f}")
        return future_value

if __name__ == "__main__":
    # Settings: Start with $5,000 | Add $500/mo (Recovered Revenue)
    architect = WealthScientist(5000, 500)
    architect.project_trajectory()
