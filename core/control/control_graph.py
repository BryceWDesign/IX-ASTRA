"""
IX-ASTRA AI Control Graph

Defines node-to-node authority and execution boundaries for AGI logic,
ensuring containment and enforcing strict callpath constraints.
"""

from typing import Dict, List, Set


class ControlGraph:
    def __init__(self):
        self.adjacency: Dict[str, Set[str]] = {}
        self.trusted_zones: Set[str] = set()
        self.execution_locks: Set[str] = set()

    def add_node(self, node_id: str, trusted: bool = False):
        if node_id not in self.adjacency:
            self.adjacency[node_id] = set()
        if trusted:
            self.trusted_zones.add(node_id)

    def add_connection(self, from_node: str, to_node: str):
        if from_node in self.execution_locks:
            raise PermissionError(f"Execution blocked for node: {from_node}")
        self.adjacency.setdefault(from_node, set()).add(to_node)

    def lock_node(self, node_id: str):
        self.execution_locks.add(node_id)

    def is_path_trusted(self, from_node: str, to_node: str) -> bool:
        return from_node in self.trusted_zones and to_node in self.trusted_zones

    def get_connections(self, node_id: str) -> List[str]:
        return list(self.adjacency.get(node_id, []))

    def validate_structure(self) -> bool:
        """
        Confirms that no unauthorized node has outbound execution paths
        outside its scope.
        """
        for node, connections in self.adjacency.items():
            if node not in self.trusted_zones:
                for target in connections:
                    if target not in self.trusted_zones:
                        return False
        return True
