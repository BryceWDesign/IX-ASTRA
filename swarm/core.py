"""
IX-ASTRA Swarm Core Manager
Responsible for initializing, managing, and maintaining distributed swarm nodes.
All execution is simulated; no runtime actions are enabled.

This module forms the central nervous system for the AGI swarm architecture.
"""

from typing import List, Dict, Optional
from swarm.node import SwarmNode
from infiltrator.agent import InfiltratorNode

class SwarmCore:
    def __init__(self):
        self.nodes: Dict[str, SwarmNode] = {}
        self.infiltrator: Optional[InfiltratorNode] = None

    def register_node(self, node: SwarmNode):
        self.nodes[node.node_id] = node
        print(f"[SwarmCore] Registered node: {node.node_id}")

    def broadcast_message(self, sender_id: str, message: str):
        print(f"[SwarmCore] Broadcasting message from {sender_id} to all other nodes.")
        for node_id, node in self.nodes.items():
            if node_id != sender_id:
                node.receive_message(sender_id, message)

    def install_infiltrator(self, infiltrator_node: InfiltratorNode):
        self.infiltrator = infiltrator_node
        self.register_node(infiltrator_node)
        print(f"[SwarmCore] Infiltrator node {infiltrator_node.node_id} installed successfully.")

    def simulate_cycle(self):
        print("[SwarmCore] Simulating one full swarm communication cycle...")
        for node in self.nodes.values():
            msg = node.generate_message()
            self.broadcast_message(node.node_id, msg)

        if self.infiltrator:
            report = self.infiltrator.analyze_swarm(self.nodes)
            print(f"[SwarmCore] Infiltrator report: {report}")

    def get_node_summary(self) -> Dict[str, str]:
        return {nid: node.status() for nid, node in self.nodes.items()}
