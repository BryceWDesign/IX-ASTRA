"""
IX-ASTRA Swarm Consensus Engine
Provides a deterministic voting and quorum protocol for simulated swarm decisions.
No real-time execution — all logic is static and intended for proof-of-concept only.
"""

from typing import Dict, Any
from collections import Counter

class ConsensusEngine:
    def __init__(self, quorum_ratio: float = 0.66):
        self.quorum_ratio = quorum_ratio
        self.vote_records: Dict[str, str] = {}

    def submit_vote(self, node_id: str, vote: str):
        self.vote_records[node_id] = vote
        print(f"[Consensus] Vote submitted: {node_id} -> {vote}")

    def get_majority_vote(self) -> str:
        if not self.vote_records:
            return "No votes submitted."
        vote_count = Counter(self.vote_records.values())
        majority_vote, count = vote_count.most_common(1)[0]
        total_votes = len(self.vote_records)
        if count / total_votes >= self.quorum_ratio:
            return f"Consensus reached: {majority_vote}"
        else:
            return "No consensus: Quorum not met."

    def reset_votes(self):
        print("[Consensus] Resetting vote records.")
        self.vote_records.clear()

    def get_vote_summary(self) -> Dict[str, Any]:
        return {
            "total_votes": len(self.vote_records),
            "votes": dict(Counter(self.vote_records.values()))
        }
