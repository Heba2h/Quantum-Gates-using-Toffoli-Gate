import tkinter as tk
from tkinter import ttk
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer, plot_bloch_multivector
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from qiskit import QuantumCircuit, Aer, transpile, assemble, QuantumRegister
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

from qiskit import QuantumCircuit, QuantumRegister, Aer, execute
from qiskit.quantum_info import Statevector, Operator
import pandas as pd

class FANOUTSimulator:
    def __init__(self, c, draw=True):
        self.c = c
        self.draw = draw

    def simulate(self):
        print("FANOUT Gate Simulation:")
        print(f"Input State: |00{self.c}>")

        A = QuantumRegister(1, "A= |0>")
        B = QuantumRegister(1, "B = |0>")
        C = QuantumRegister(1, f"C ")
        qc = QuantumCircuit(A, B, C)

        if self.c:
            qc.x(2)

        qc.ccx(0, 1, 2)
        qc.measure_all()

        simulator = Aer.get_backend("aer_simulator")
        result = execute(qc, simulator, shots=1).result()
        counts = result.get_counts(qc)
        output = list(counts.keys())[0]

        print("Output State:")
        print(f"|{output[::-1]}>")  # Reverse the order to match the standard convention

        truth_table_data = {
            "A": [0, 0],
            "B": [0, 0],
            "C": [0, 1],
            "A'": [0, 0],
            "B'": [0, 0],
            "C'": [0, 1],
         }

        truth_table = pd.DataFrame(truth_table_data)

        print("\nTruth Table:")
        print(truth_table.to_string(index=False))

        if self.draw:
            print("\nCircuit Diagram:")
            qc_draw = QuantumCircuit(A, B, C)
            qc_draw.ccx(0, 1, 2)
            qc_draw.measure_all()
            qc_draw.draw(output="mpl", style="iqp", reverse_bits=False)
            # Use the following line if you want to display the circuit
            # display(qc_draw.draw(output="mpl", style="iqp", reverse_bits=False))

        return output[::-1]
    
    def get_quantum_circuit(self):
        A = QuantumRegister(1, "A= |0>")
        B = QuantumRegister(1, "B = |0>")
        C = QuantumRegister(1, f"C ")
        qc = QuantumCircuit(A, B, C)

        if self.c:
            qc.x(2)

        qc.ccx(0, 1, 2)
        qc.measure_all()

        return qc

# Example usage:
# fanout_simulator = FANOUTSimulator(0)
# fanout_simulator.simulate()
