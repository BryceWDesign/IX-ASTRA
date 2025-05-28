"""
IX-ASTRA Sandbox Interface

Provides a framework for safely testing AGI behavior and infiltrator interventions
in isolated environments with rollback and observational logging.
"""

from typing import Callable, Dict, Any, List
from copy import deepcopy
from engine.simulator.core_simulation import IXSwarmSimulator


class SandboxResult:
    def __init__(self, initial_state: Dict, final_state: Dict, interventions: List[str]):
        self.initial_state = initial_state
        self.final_state = final_state
        self.interventions = interventions


class SandboxEnvironment:
    def __init__(self, simulator: IXSwarmSimulator):
        self.simulator = simulator
        self.history: List[Dict[str, Any]] = []
        self.snapshots: List[Dict[str, Any]] = []

    def capture_snapshot(self):
        """Store the current simulation state for analysis or rollback."""
        snapshot = deepcopy(self.simulator.report_state())
        self.snapshots.append(snapshot)

    def run_with_conditions(self, steps: int, condition_fn: Callable[[Dict], bool]) -> SandboxResult:
        """Run the simulation with injected conditions and return state diffs and intervention logs."""
        self.capture_snapshot()
        initial_state = deepcopy(self.simulator.report_state())

        for _ in range(steps):
            self.simulator.run_simulation_step()
            self.capture_snapshot()
            current_state = self.simulator.report_state()

            if condition_fn(current_state):
                break

        final_state = deepcopy(current_state)
        interventions = self._collect_intervention_logs(final_state)
        return SandboxResult(initial_state, final_state, interventions)

    def _collect_intervention_logs(self, state: Dict) -> List[str]:
        logs = []
        for node in state.values():
            logs.extend(node.get("logs", []))
        return logs

    def rollback(self, version: int = -1):
        """Rollback to a specific snapshot version."""
        if len(self.snapshots) == 0:
            raise RuntimeError("No snapshot available to rollback.")
        state = deepcopy(self.snapshots[version])
        # Reconstruct simulator manually from state if needed (stubbed here)
        return state  # placeholder

