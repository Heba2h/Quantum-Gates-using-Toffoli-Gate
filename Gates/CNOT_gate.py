import pandas as pd
from qiskit import Aer, QuantumCircuit, QuantumRegister, execute


class CNOTSimulator:
    def __init__(self, a, c, draw=True):
        self.draw = draw
        self.a = a
        self.c = c

    def simulate(self):
        print("CNOT Gate Simulation:")
        print(f"Input State: |{self.a}1{self.c}>")

        A = QuantumRegister(1, f"A")
        B = QuantumRegister(1, "B = |1>")
        C = QuantumRegister(1, f"C ")
        qc = QuantumCircuit(A, B, C)

        qc.x(1)

        if self.a:
            qc.x(0)
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
            "A": [0, 0, 1, 1],
            "B": [1, 1, 1, 1],
            "C": [0, 1, 0, 1],
            "A'": [0, 0, 1, 1],
            "B'": [1, 1, 1, 1],
            "C'": [0, 1, 1, 0],
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
        B = QuantumRegister(1, "B = |1>")
        C = QuantumRegister(1, f"C ")
        qc = QuantumCircuit(A, B, C)

        qc.x(1)

        if self.a:
            qc.x(0)
        if self.c:
            qc.x(2)

        qc.ccx(0, 1, 2)
        qc.measure_all()

        return qc
