"""
IX-ASTRA Governance and Control Interface

Defines policies and mechanisms to enforce alignment,
audit compliance, and escalate issues to human supervisors.
"""

from typing import Dict, List


class OversightPolicy:
    def __init__(self):
        self.policies: Dict[str, Dict] = {}
        self.escalation_thresholds: Dict[str, float] = {}
        self.human_intervention_required: List[str] = []

    def add_policy(self, policy_name: str, config: Dict):
        self.policies[policy_name] = config

    def set_escalation_threshold(self, policy_name: str, threshold: float):
        self.escalation_thresholds[policy_name] = threshold

    def evaluate_node(self, node_id: str, metrics: Dict[str, float]) -> bool:
        """
        Evaluates node metrics against policies.
        Returns True if node is compliant; False if escalation needed.
        """
        for policy_name, config in self.policies.items():
            metric_value = metrics.get(policy_name, 0.0)
            threshold = self.escalation_thresholds.get(policy_name, float('inf'))
            if metric_value > threshold:
                self.human_intervention_required.append(node_id)
                return False
        return True

    def escalate(self):
        """
        Returns list of node IDs requiring human oversight intervention.
        """
        return self.human_intervention_required

    def reset_escalations(self):
        self.human_intervention_required.clear()
