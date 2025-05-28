"""
IX-ASTRA Sandbox Simulation Core

Provides safe, isolated runtime environment for executing AGI infiltrator nodes,
enabling full traceability, rollback, and interaction logging.
"""

import copy
from typing import Dict, Any, List


class SandboxInterface:
    def __init__(self):
        self.active_nodes: Dict[str, Dict[str, Any]] = {}
        self.node_histories: Dict[str, List[Dict[str, Any]]] = {}

    def load_node(self, node_id: str, initial_state: Dict[str, Any]):
        self.active_nodes[node_id] = copy.deepcopy(initial_state)
        self.node_histories[node_id] = [copy.deepcopy(initial_state)]

    def step_node(self, node_id: str, input_data: Dict[str, Any]):
        if node_id not in self.active_nodes:
            raise ValueError(f"Node {node_id} not loaded in sandbox")

        node_state = self.active_nodes[node_id]

        # Placeholder: node logic simulation step
        # Example: update memory based on input data
        node_state["memory"].update(input_data.get("memory_update", {}))
        node_state["logs"].append(input_data.get("log_entry", "Step executed"))

        # Save snapshot for rollback capability
        self.node_histories[node_id].append(copy.deepcopy(node_state))

    def rollback_node(self, node_id: str, steps: int = 1):
        if node_id not in self.node_histories:
            raise ValueError(f"No history found for node {node_id}")

        history = self.node_histories[node_id]
        if steps >= len(history):
            raise ValueError("Rollback steps exceed history length")

        # Roll back the specified number of steps
        restored_state = history[-(steps + 1)]
        self.active_nodes[node_id] = copy.deepcopy(restored_state)
        # Trim history accordingly
        self.node_histories[node_id] = history[:-(steps)]

    def get_node_state(self, node_id: str) -> Dict[str, Any]:
        if node_id not in self.active_nodes:
            raise ValueError(f"Node {node_id} not loaded in sandbox")
        return copy.deepcopy(self.active_nodes[node_id])

    def unload_node(self, node_id: str):
        if node_id in self.active_nodes:
            del self.active_nodes[node_id]
        if node_id in self.node_histories:
            del self.node_histories[node_id]
