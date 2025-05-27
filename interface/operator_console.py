"""
IX-ASTRA Operator Console
Mock CLI interface for interacting with swarm infiltrators.
Proof-of-concept only. No real execution or control takes place.
"""

from infiltrator.monitor import InfiltratorMonitor
from infiltrator.agent import InfiltratorNode
from swarm.node import SwarmNode

class OperatorConsole:
    def __init__(self):
        self.monitor = InfiltratorMonitor()
        self.mock_node_pool = self._generate_mock_swarm()

        # Register mock infiltrators
        for _ in range(4):
            infiltrator = InfiltratorNode()
            self.monitor.register_infiltrator(infiltrator)

    def _generate_mock_swarm(self):
        pool = {}
        for i in range(20):
            node = SwarmNode()
            node.behavior_profile = "neutral" if i % 4 != 0 else "chaotic"
            pool[node.node_id] = node
        return pool

    def run_scan(self):
        print("\n🔍 Running swarm analysis via all infiltrators...")
        reports = self.monitor.scan_swarm(self.mock_node_pool)
        for report in reports:
            print(report)

    def check_for_silent_failures(self):
        print("\n🧨 Silent Failure Detection:")
        result = self.monitor.detect_silent_failures(self.mock_node_pool)
        print(result)

    def summary(self):
        print("\n📋 Infiltrator Monitor Summary:")
        info = self.monitor.summary()
        for k, v in info.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    console = OperatorConsole()
    console.run_scan()
    console.check_for_silent_failures()
    console.summary()
