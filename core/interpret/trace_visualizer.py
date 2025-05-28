"""
IX-ASTRA Interpretability Layer

Provides visualization and traceability of AGI node decision logic,
goal hierarchies, and memory evolution over time.
"""

from typing import Dict, List, Any
import json

class TraceVisualizer:
    def __init__(self, node_state: Dict[str, Any]):
        self.node_id = node_state.get("id", "UNKNOWN")
        self.memory = node_state.get("memory", {})
        self.logs = node_state.get("logs", [])

    def format_memory_trace(self) -> str:
        trace_output = f"Node ID: {self.node_id}\n--- MEMORY TRACE ---\n"
        for key, value in self.memory.items():
            trace_output += f"{key}: {json.dumps(value, indent=2)}\n"
        return trace_output

    def format_decision_log(self) -> str:
        log_output = f"--- DECISION LOG ---\n"
        for i, log in enumerate(self.logs):
            log_output += f"[{i}] {log}\n"
        return log_output

    def get_full_trace(self) -> str:
        return self.format_memory_trace() + "\n" + self.format_decision_log()

    def export_trace_json(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "memory": self.memory,
            "logs": self.logs
        }
