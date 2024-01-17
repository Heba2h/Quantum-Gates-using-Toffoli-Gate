from matplotlib import pyplot as plt
import pandas as pd
from qiskit import Aer, QuantumCircuit, QuantumRegister, execute
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NANDSimulator:
    def __init__(self, a, b, draw=True):
        self.a = a
        self.b = b
        self.draw = draw

    def simulate(self):
        print("NAND Gate Simulation:")
        print(f"Input State: |{self.a}{self.b}1>")

        A = QuantumRegister(1, f"A")
        B = QuantumRegister(1, f"B")
        C = QuantumRegister(1, "C = |1>")
        qc = QuantumCircuit(A, B, C)

        if self.a:
            qc.x(0)
        if self.b:
            qc.x(1)

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
            "A": [0, 0, 1, 1],
            "B": [0, 1, 0, 1],
            "C": [1, 1, 1, 1],
            "A'": [1, 1, 0, 0],
            "B'": [1, 0, 1, 0],
            "C'": [0, 0, 0, 1],
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
        
        return output[::-1]
    
    def get_quantum_circuit(self):
        A = QuantumRegister(1, f"A")
        B = QuantumRegister(1, f"B")
        C = QuantumRegister(1, "C = |1>")
        qc = QuantumCircuit(A, B, C)

        if self.a:
            qc.x(0)
        if self.b:
            qc.x(1)

        qc.x(2)
        qc.ccx(0, 1, 2)
        qc.measure_all()

        return qc