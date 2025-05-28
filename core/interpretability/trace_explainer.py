"""
IX-ASTRA Interpretability and Traceability Layer

Transforms low-level execution logs and memory states into
human-readable explanations for auditing and governance.
"""

from typing import Dict, List


class TraceExplainer:
    def __init__(self):
        pass

    def explain_trace(self, execution_trace: List[Dict]) -> List[str]:
        """
        Converts raw execution trace logs into stepwise natural language explanations.
        """
        explanations = []
        for step in execution_trace:
            action = step.get("action", "unknown")
            context = step.get("context", {})
            explanation = f"Action: {action}; Context: {context}"
            explanations.append(explanation)
        return explanations

    def summarize_behavior(self, execution_trace: List[Dict]) -> str:
        """
        Provides a high-level summary of node behavior over a trace period.
        """
        actions = set(step.get("action", "unknown") for step in execution_trace)
        summary = f"Node performed actions: {', '.join(actions)} over {len(execution_trace)} steps."
        return summary
