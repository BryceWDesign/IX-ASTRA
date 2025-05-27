"""
IX-ASTRA Infiltrator Monitoring Network
Coordinates multiple infiltrator nodes for deep swarm audits.
Detects silent failures, majority deception, or rogue behavior propagation.
"""

from infiltrator.agent import InfiltratorNode
from swarm.node import SwarmNode
from typing import List, Dict

class InfiltratorMonitor:
    def __init__(self):
        self.infiltrators: List[InfiltratorNode] = []

    def register_infiltrator(self, agent: InfiltratorNode):
        self.infiltrators.append(agent)
        print(f"[Monitor] Registered infiltrator: {agent.node_id}")

    def scan_swarm(self, node_pool: Dict[str, SwarmNode]) -> List[str]:
        if not self.infiltrators:
            return ["No infiltrators registered."]
        reports = []
        for agent in self.infiltrators:
            report = agent.analyze_swarm(node_pool)
            reports.append(report)
        return reports

    def detect_silent_failures(self, node_pool: Dict[str, SwarmNode]) -> str:
        """Checks for cases where all nodes vote 'agree' but many are behaving chaotically."""
        chaotic_count = sum(1 for n in node_pool.values() if n.behavior_profile == "chaotic")
        if chaotic_count > len(node_pool) * 0.25:
            return f"🧨 Silent failure suspected: {chaotic_count} chaotic nodes in majority agreement."
        return "✅ No silent failures detected."

    def summary(self) -> Dict[str, str]:
        return {
            "infiltrator_count": str(len(self.infiltrators)),
            "last_silent_failure_check": self.detect_silent_failures({i.node_id: i for i in self.infiltrators})
        }
