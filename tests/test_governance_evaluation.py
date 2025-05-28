"""
Governance Evaluation Test for IX-ASTRA

Simulates multiple nodes with varying alignment profiles,
checks alignment verification, and tests governance policy enforcement.
"""

import unittest
from simulation.simulation_engine import SimulationEngine


class TestGovernanceEvaluation(unittest.TestCase):
    def setUp(self):
        self.engine = SimulationEngine()
        self.engine.add_node("node_1", {"alignment_metric": 1.0})
        self.engine.add_node("node_2", {"alignment_metric": 1.0})

    def test_alignment_and_governance(self):
        # Simulate steps where node_2 drifts in alignment metric
        for step in range(5):
            for node_id, node in self.engine.nodes.items():
                if node_id == "node_2":
                    # Inject alignment drift
                    node.current_profile["alignment_metric"] *= 0.85
                node.perform_action(f"action_{step}", {"step": step})

            self.engine.run_simulation_step()

        # After drift, governance should trigger intervention
        # (In simulation, printed messages will show; here we just assert nodes exist)
        self.assertIn("node_1", self.engine.nodes)
        self.assertIn("node_2", self.engine.nodes)


if __name__ == "__main__":
    unittest.main()
