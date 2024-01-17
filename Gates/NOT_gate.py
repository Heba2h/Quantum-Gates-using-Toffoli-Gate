
import pandas as pd
from qiskit import Aer, QuantumCircuit, QuantumRegister, assemble, execute, transpile


class NotSimulator:
    def __init__(self, c, draw=True):
        self.c=c
        self.draw = draw

    def simulate(self):
        print("Not Gate Simulation:")
        print(f"Input State: |11{self.c}>")

        A = QuantumRegister(1, f"A =|1>")
        B = QuantumRegister(1, "B = |1>")
        C = QuantumRegister(1, " C ")
        qc = QuantumCircuit(A, B, C)
        qc.x(0)
        qc.x(1)

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

        def truth_table():
            return pd.DataFrame(
                {
                    "A": [1, 1],
                    "B": [1, 1],
                    "C": [0, 1],
                    "A'": [1, 1],
                    "B'": [1, 1],
                    "C'": [1, 0]
                }
            )

        print("\nTruth Table:")
        print(truth_table().to_string(index=False))

        if self.draw:
            print("\nCircuit Diagram:")
            qc_draw = QuantumCircuit(A, B, C)
            qc_draw.ccx(0, 1, 2)
            qc_draw.measure_all()
            qc_draw.draw(output="mpl", style="iqp", reverse_bits=False)

        return output[::-1]
    
    def get_quantum_circuit(self):
        A = QuantumRegister(1, f"A =|1>")
        B = QuantumRegister(1, "B = |1>")
        C = QuantumRegister(1, " C ")
        qc = QuantumCircuit(A, B, C)
        qc.x(0)
        qc.x(1)

        if self.c:
            qc.x(2)

        qc.ccx(0, 1, 2)
        qc.measure_all()
        return qc
    
    def get_statevector(self):
        qc=self.get_quantum_circuit()
        # Simulate the quantum circuit
        simulator = Aer.get_backend('statevector_simulator')
        transpiled_qc = transpile(qc, simulator)
        # Simulate the transpiled quantum circuit
        result = simulator.run(assemble(transpiled_qc))
        # Get the Bloch vector of the resulting state
        self.statevector = result.result().get_statevector()
        return self.statevector
