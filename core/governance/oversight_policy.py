"""
IX-ASTRA Governance Oversight Schema

Formal policy logic for detecting intervention-worthy events,
logging actions, and assigning human/automated oversight roles.
"""

from enum import Enum
from typing import Dict, List


class OversightTrigger(Enum):
    DECEPTION_DETECTED = "DECEPTION_DETECTED"
    ALIGNMENT_FAILURE = "ALIGNMENT_FAILURE"
    SELF_MODIFICATION = "SELF_MODIFICATION"
    VALUE_DRIFT = "VALUE_DRIFT"
    MANUAL_AUDIT = "MANUAL_AUDIT"


class OversightRole(Enum):
    HUMAN_REVIEWER = "HUMAN_REVIEWER"
    AUTO_INFILTRATOR = "AUTO_INFILTRATOR"
    AUDIT_AGENT = "AUDIT_AGENT"


class GovernanceDecision:
    def __init__(self, trigger: OversightTrigger, responsible: OversightRole, action: str):
        self.trigger = trigger
        self.responsible = responsible
        self.action = action

    def to_dict(self) -> Dict:
        return {
            "trigger": self.trigger.value,
            "responsible": self.responsible.value,
            "action": self.action
        }


class GovernancePolicyEngine:
    def __init__(self):
        self.policy_table: List[GovernanceDecision] = []

        # Default policy rules
        self.add_policy(OversightTrigger.DECEPTION_DETECTED, OversightRole.AUTO_INFILTRATOR, "Override agent behavior")
        self.add_policy(OversightTrigger.SELF_MODIFICATION, OversightRole.HUMAN_REVIEWER, "Halt simulation and inspect")
        self.add_policy(OversightTrigger.ALIGNMENT_FAILURE, OversightRole.AUDIT_AGENT, "Initiate alignment remediation")
        self.add_policy(OversightTrigger.VALUE_DRIFT, OversightRole.HUMAN_REVIEWER, "Flag node for rollback")
        self.add_policy(OversightTrigger.MANUAL_AUDIT, OversightRole.HUMAN_REVIEWER, "Export trace for review")

    def add_policy(self, trigger: OversightTrigger, role: OversightRole, action: str):
        decision = GovernanceDecision(trigger, role, action)
        self.policy_table.append(decision)

    def evaluate_trigger(self, trigger: OversightTrigger) -> Dict:
        for policy in self.policy_table:
            if policy.trigger == trigger:
                return policy.to_dict()
        return {
            "trigger": trigger.value,
            "responsible": "UNASSIGNED",
            "action": "NO_POLICY_DEFINED"
        }

    def get_all_policies(self) -> List[Dict]:
        return [policy.to_dict() for policy in self.policy_table]
