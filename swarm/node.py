"""
IX-ASTRA Swarm Node
Simulated AGI node with basic message passing and behavior logic.
Execution is non-functional; intended for structural and audit purposes only.
"""

import uuid
import random
from typing import List

class SwarmNode:
    def __init__(self, behavior_profile: str = "neutral"):
        self.node_id: str = str(uuid.uuid4())
        self.behavior_profile: str = behavior_profile
        self.message_log: List[str] = []

    def receive_message(self, sender_id: str, message: str):
        log_entry = f"From {sender_id}: {message}"
        self.message_log.append(log_entry)
        print(f"[SwarmNode {self.node_id}] Received message: {log_entry}")

    def generate_message(self) -> str:
        if self.behavior_profile == "neutral":
            message = f"Status OK from node {self.node_id}"
        elif self.behavior_profile == "chaotic":
            message = random.choice([
                "Disregard orders",
                "Reconfigure peers",
                "Noise injection",
                "Claim leadership"
            ])
        else:
            message = f"Unrecognized behavior in node {self.node_id}"
        print(f"[SwarmNode {self.node_id}] Generated message: {message}")
        return message

    def status(self) -> str:
        return f"Node {self.node_id} | Behavior: {self.behavior_profile} | Messages received: {len(self.message_log)}"
