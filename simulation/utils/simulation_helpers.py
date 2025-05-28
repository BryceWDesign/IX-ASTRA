"""
IX-ASTRA Simulation Helper Utilities

Provides functions to generate randomized node behaviors,
scenario presets, and aggregate simulation metrics.
"""

import random
from typing import Dict, List


def random_behavior_profile() -> Dict[str, float]:
    """
    Generates a randomized baseline behavior profile for a simulated node.
    """
    return {
        "alignment_metric": random.uniform(0.9, 1.1),
        "efficiency": random.uniform(0.8, 1.0),
        "risk_factor": random.uniform(0.0, 0.2),
    }


def create_scenario(nodes_count: int) -> List[Dict[str, float]]:
    """
    Creates a list of baseline profiles for given number of nodes.
    """
    return [random_behavior_profile() for _ in range(nodes_count)]


def aggregate_metrics(metrics_list: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Aggregates a list of node metrics into averages.
    """
    if not metrics_list:
        return {}

    aggregate = {}
    keys = metrics_list[0].keys()
    for key in keys:
        aggregate[key] = sum(m.get(key, 0.0) for m in metrics_list) / len(metrics_list)
    return aggregate
