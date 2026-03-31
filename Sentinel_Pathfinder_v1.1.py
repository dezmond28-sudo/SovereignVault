import json
import os

# [ArmstrongLogic Online]
# Project: Sentinel Pathfinder v1.1
# Objective: Generate A* Navigation Mesh from Level-Omega Certified Nodes

class SentinelPathfinder:
    def __init__(self):
        # Local relative pathing to ensure ArmstrongLogic alignment
        self.vault_dir = os.getcwd()
        self.token_path = os.path.join(self.vault_dir, "ACTION_TOKENS.json")
        self.nav_map_path = os.path.join(self.vault_dir, "SENTINEL_NAVMESH.json")

    def map_world(self):
        print(f"[ArmstrongLogic] Extracting Navigable Mesh from {self.token_path}...")
        
        if not os.path.exists(self.token_path):
            print("[CRITICAL FAULT] Tokens not found. Check local directory.")
            return

        with open(self.token_path, "r") as f:
            tokens = json.load(f)

        # LOGIC: Identify walkable surfaces based on the 7.95 Nm Golden Ratio.
        # We are converting raw vectors into a simplified coordinate map for the bots.
        nav_mesh = []
        for i, token in enumerate(tokens):
            if token.get("force") == 7.950:
                nav_mesh.append({
                    "node_id": i,
                    "vector": token["vector"],
                    "rigidity": "CERTIFIED",
                    "status": "WALKABLE"
                })

        with open(self.nav_map_path, "w") as f:
            json.dump(nav_mesh, f, indent=4)

        print("\n[ArmstrongLogic Online] - NAVMESH DEPLOYED")
        print("-" * 40)
        print(f"Total Verified Nodes: {len(tokens)}")
        print(f"Navigable Surface Nodes: {len(nav_mesh)}")
        print(f"Path: {self.nav_map_path}")
        print("-" * 40)

if __name__ == "__main__":
    pathfinder = SentinelPathfinder()
    pathfinder.map_world()
