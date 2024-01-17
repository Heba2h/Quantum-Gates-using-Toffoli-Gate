import tkinter as tk
from tkinter import ttk
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer, plot_bloch_multivector
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class ORGateSimulator:
    def __init__(self, a, b, draw=True):
        self.a = a
        self.b = b
        self.draw = draw

    def simulate(self):
        print("OR Gate Simulation:")
        print(f"Input State:|{self.a}111{self.b}>")

        A = QuantumRegister(1, f"A ")
        B = QuantumRegister(1, f"B ")
        C = QuantumRegister(1, "C = |1>")
        D = QuantumRegister(1, "D = |1>")
        E = QuantumRegister(1, "E = |1>")
        qc = QuantumCircuit(B, C, D, E, A)
        qc.reverse_bits()

        if self.a:
            qc.x(4)
        if self.b:
            qc.x(0)
        qc.x(1)
        qc.x(2)
        qc.x(3)
        qc.ccx(4, 2, 3)
        qc.ccx(0, 2, 1)
        qc.ccx(1, 3, 2)
        qc.measure_all()

        simulator = Aer.get_backend("aer_simulator")
        result = execute(qc, simulator, shots=1).result()
        counts = result.get_counts(qc)
        print(f" Output |{list(counts.keys())[0]}>")
        print(f"|A NOT(A) OR(A,B) NOT(B) B>")

        truth_table_data = {
                    "A": [0, 0, 1, 1],
                    "B": [0, 1, 0, 1],
                    "C": [1, 1, 1, 1],
                    "D": [1, 1, 1, 1],
                    "E": [1, 1, 1, 1],
                    "A'": [0, 0, 1, 1],
                    "NOT(A)": [1, 1, 0, 0],
                    "OR(A,B)": [0, 1, 1, 1],
                    "NOT(B)": [1, 0, 1, 0],
                    "B'": [0, 1, 0, 1],
                }

        truth_table = pd.DataFrame(truth_table_data)

        print("\nTruth Table:")
        print(truth_table.to_string(index=False))

        if self.draw:
            qc_draw = QuantumCircuit(B, C, D, E, A)
            qc_draw.ccx(4, 2, 3)
            qc_draw.ccx(0, 2, 1)
            qc_draw.ccx(1, 3, 2)
            qc_draw.measure_all()
            # display(qc_draw.draw(output="mpl", reverse_bits=True, style="iqp"))

        return list(counts.keys())[0]
    
    def get_quantum_circuit(self):
        A = QuantumRegister(1, f"A ")
        B = QuantumRegister(1, f"B ")
        C = QuantumRegister(1, "C = |1>")
        D = QuantumRegister(1, "D = |1>")
        E = QuantumRegister(1, "E = |1>")
        qc = QuantumCircuit(B, C, D, E, A)
        qc.reverse_bits()

        if self.a:
            qc.x(4)
        if self.b:
            qc.x(0)

        qc.x(1)
        qc.x(2)
        qc.x(3)
        qc.ccx(4, 2, 3)
        qc.ccx(0, 2, 1)
        qc.ccx(1, 3, 2)
        qc.measure_all()

        return qc
# Example usage:
# or_gate_simulator = ORGateSimulator(1, 1)
# or_gate_simulator.simulate()
