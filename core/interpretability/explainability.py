"""
IX-ASTRA Interpretability Explainability Module

Provides detailed, context-aware explanations of infiltrator node
decisions to enhance auditability and trustworthiness.
"""

from typing import List, Dict


class ExplainabilityModule:
    def __init__(self):
        pass

    def explain_decision(self, node_id: str, decision_trace: List[Dict[str, str]]) -> str:
        """
        Creates a detailed explanation summary based on node's decision trace.
        """
        explanation = [f"Decision Explanation for Node {node_id}:\n"]
        for step, entry in enumerate(decision_trace, 1):
            action = entry.get("action", "unknown action")
            context = entry.get("context", {})
            explanation.append(f"Step {step}: Executed '{action}' with context {context}")
        return "\n".join(explanation)
