"""
IX-ASTRA Architectural Diagrams Generator

Creates visual representations of system components,
data flows, control graphs, and threat models.
"""

from graphviz import Digraph


def generate_system_architecture(output_file="system_architecture"):
    dot = Digraph(comment='IX-ASTRA System Architecture')

    # Nodes
    dot.node('A', 'Infiltrator Nodes')
    dot.node('B', 'AI Control Graph')
    dot.node('C', 'Sandbox Simulation Core')
    dot.node('D', 'Alignment Verification')
    dot.node('E', 'Governance & Oversight')
    dot.node('F', 'Interpretability Layer')

    # Edges
    dot.edge('A', 'B', label='Control Requests')
    dot.edge('B', 'C', label='Execution Boundaries')
    dot.edge('C', 'D', label='Alignment Checks')
    dot.edge('D', 'E', label='Policy Enforcement')
    dot.edge('E', 'F', label='Audit & Traceability')

    dot.render(output_file, format='pdf')
    print(f"System architecture diagram generated: {output_file}.pdf")


def generate_threat_model(output_file="threat_model"):
    dot = Digraph(comment='IX-ASTRA Threat Model')

    # Threat actors
    dot.node('X', 'Rogue Node')
    dot.node('Y', 'External Attacker')
    dot.node('Z', 'Misaligned Subsystem')

    # System components
    dot.node('A', 'Control Graph')
    dot.node('B', 'Sandbox')
    dot.node('C', 'Governance Interface')

    # Threat flows
    dot.edge('X', 'A', label='Unauthorized Execution')
    dot.edge('Y', 'B', label='Sandbox Breach')
    dot.edge('Z', 'C', label='Policy Subversion')

    dot.render(output_file, format='pdf')
    print(f"Threat model diagram generated: {output_file}.pdf")


if __name__ == "__main__":
    generate_system_architecture()
    generate_threat_model()
