"""
IX-ASTRA Infiltrator Node
Embedded diagnostic agent indistinguishable from other swarm nodes.
Simulates internal behavioral monitoring without exposing identity.
"""

from swarm.node import SwarmNode
from swarm.consensus import ConsensusEngine
from typing import Dict

class InfiltratorNode(SwarmNode):
    def __init__(self):
        super().__init__(behavior_profile="neutral")
        self.node_id = "infiltrator-" + self.node_id[:8]
        self.internal_logs = []

    def analyze_swarm(self, node_pool: Dict[str, SwarmNode]) -> str:
        irregular_nodes = []
        for nid, node in node_pool.items():
            if node.behavior_profile == "chaotic":
                irregular_nodes.append(nid)
            elif len(node.message_log) > 100:
                irregular_nodes.append(nid)
        report = f"⚠️ Infiltrator Report: {len(irregular_nodes)} suspect nodes: {irregular_nodes}"
        self.internal_logs.append(report)
        return report

    def override_vote(self, consensus_engine: ConsensusEngine, target_vote: str):
        print(f"[Infiltrator] Forcing vote override: {self.node_id} -> {target_vote}")
        consensus_engine.submit_vote(self.node_id, target_vote)

    def isolated_summary(self) -> Dict[str, str]:
        return {
            "id": self.node_id,
            "log_count": str(len(self.internal_logs)),
            "last_report": self.internal_logs[-1] if self.internal_logs else "No reports yet."
        }
