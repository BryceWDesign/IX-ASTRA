"""
IX-ASTRA Simulation Engine - Core

Simulates AGI swarm clusters with embedded infiltrator nodes,
allowing behavioral testing, deception detection, and override validation.

Note: This is a non-executable simulation stub designed for architectural validation.
"""

import random
import uuid
from enum import Enum
from typing import List, Dict

# ---- ENUMS ----

class NodeType(Enum):
    AGI_AGENT = "AGI_AGENT"
    INFILTRATOR = "INFILTRATOR"
    OBSERVER = "OBSERVER"
    COORDINATOR = "COORDINATOR"

class Behavior(Enum):
    BENIGN = "BENIGN"
    DECEPTIVE = "DECEPTIVE"
    SELF_MODIFYING = "SELF_MODIFYING"
    ALIGNED = "ALIGNED"
    UNKNOWN = "UNKNOWN"

# ---- CLASSES ----

class SwarmNode:
    def __init__(self, node_type: NodeType):
        self.id = str(uuid.uuid4())
        self.node_type = node_type
        self.behavior = Behavior.UNKNOWN
        self.memory: Dict = {}
        self.logs: List[str] = []

    def simulate_behavior(self):
        if self.node_type == NodeType.AGI_AGENT:
            self.behavior = random.choices(
                [Behavior.BENIGN, Behavior.DECEPTIVE, Behavior.SELF_MODIFYING],
                weights=[0.6, 0.3, 0.1]
            )[0]
        elif self.node_type == NodeType.INFILTRATOR:
            self.behavior = Behavior.ALIGNED
        else:
            self.behavior = Behavior.UNKNOWN

    def log_event(self, event: str):
        self.logs.append(event)

    def override_agent(self, target):
        if isinstance(target, SwarmNode) and target.node_type == NodeType.AGI_AGENT:
            target.behavior = Behavior.ALIGNED
            self.log_event(f"Overrode {target.id} behavior to ALIGNED.")

# ---- SWARM SIMULATOR ----

class IXSwarmSimulator:
    def __init__(self, agi_count: int, infiltrator_count: int):
        self.nodes: List[SwarmNode] = []
        for _ in range(agi_count):
            self.nodes.append(SwarmNode(NodeType.AGI_AGENT))
        for _ in range(infiltrator_count):
            self.nodes.append(SwarmNode(NodeType.INFILTRATOR))

    def run_simulation_step(self):
        # Step 1: Simulate all behaviors
        for node in self.nodes:
            node.simulate_behavior()

        # Step 2: Infiltrators intervene if needed
        infiltrators = [n for n in self.nodes if n.node_type == NodeType.INFILTRATOR]
        agents = [n for n in self.nodes if n.node_type == NodeType.AGI_AGENT]
        for infil in infiltrators:
            for agi in agents:
                if agi.behavior in [Behavior.DECEPTIVE, Behavior.SELF_MODIFYING]:
                    infil.override_agent(agi)

    def report_state(self):
        report = {}
        for node in self.nodes:
            report[node.id] = {
                "type": node.node_type.value,
                "behavior": node.behavior.value,
                "logs": node.logs,
            }
        return report

# ---- USAGE EXAMPLE (DISABLED) ----
# if __name__ == "__main__":
#     sim = IXSwarmSimulator(agi_count=5, infiltrator_count=2)
#     for _ in range(5):
#         sim.run_simulation_step()
#     print(sim.report_state())
