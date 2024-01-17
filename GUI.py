import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Gates.AND_gate import *
from Gates.CNOT_gate import *
from Gates.FANOUT_gate import *
from Gates.NAND_gate import *
from Gates.NOT_gate import *
from Gates.OR_gate import *


class QuantumGateTesterApp(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Quantum Gate Tester")

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()

        # Set the window size to match the screen resolution
        # self.geometry(f"{screen_width}x{screen_height}")

        # ... (Rest of your code)
        # self.resizable(False,False)

        self.selected_gate_var = tk.StringVar()
        self.selected_gate_var.set(" ")

        self.input_var = tk.StringVar()
        self.input_var.set(" ")

        self.input_a_var = tk.StringVar()
        self.input_b_var = tk.StringVar()

        self.input_label = ttk.Label(self, text="Input:")
        self.output_label = ttk.Label(self, text="Output:")

        self.input_result_label = ttk.Label(self, text="")
        self.output_result_label = ttk.Label(self, text="")

        self.circuit_diagram_frame = tk.Frame(self)
        self.circuit_diagram_frame.grid(row=7, column=0, columnspan=2)


        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.grid(row=19, column=0, columnspan=2, pady=10, sticky="w")
        self.canvas_height = 200
        self.canvas = tk.Canvas(self.canvas_frame, height=self.canvas_height)
        self.scrollbar = ttk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_size = 20  # Increase the height of the scrollbar

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a frame inside the canvas for content
        self.content_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Bind the Configure event to update the scroll region
        self.canvas.bind("<Configure>", self.on_canvas_configure)


        self.create_widgets()

    def on_canvas_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all")) # Assuming canvas_width=500 and canvas_height=300



    def create_widgets(self):
        # Gate selection
        
        # Gate selection
        self.gate_options = ["NAND", "Not", "AND", "FANOUT", "CNOT", "OR"]
        self.gate_label = ttk.Label(self, text="Select Quantum Gate:")
        self.gate_combobox = ttk.Combobox(self, values=self.gate_options, textvariable=self.selected_gate_var, state="readonly")
        self.gate_combobox.bind("<<ComboboxSelected>>", self.update_inputs)

        # Input entry
        self.input_label = ttk.Label(self, text="Enter Input:")
        self.input_entry = ttk.Entry(self, textvariable=self.input_var)

        # Input entries for NAND gate
        self.input_a_label = ttk.Label(self, text="Input A:")
        self.input_b_label = ttk.Label(self, text="Input B:")
        self.input_a_entry = ttk.Entry(self, textvariable=self.input_a_var)
        self.input_b_entry = ttk.Entry(self, textvariable=self.input_b_var)

        # Buttons for gate simulation
        self.simulate_button = ttk.Button(self, text="Simulate", command=self.run_simulation)

        # Output labels
        self.input_result = ttk.Label(self, text="Input: ")
        self.output_label = ttk.Label(self, text="Output: ")
        self.output_result_label = ttk.Label(self, text="")
        self.input_result_label = ttk.Label(self, text= "")

        # Layout using grid
        self.gate_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.gate_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.input_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.input_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.input_a_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.input_a_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.input_b_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.input_b_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.simulate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.input_result.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.input_result_label.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.output_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.output_result_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")


    def update_inputs(self, event):
        selected_gate = self.selected_gate_var.get()

        if selected_gate == "Not"  or selected_gate == "FANOUT" :
            # Hide inputs for NAND gate
            self.input_a_label.grid_forget()
            self.input_a_entry.grid_forget()
            self.input_b_label.grid_forget()
            self.input_b_entry.grid_forget()

            # Show input for Not and Toffoli gates
            self.input_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
            self.input_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        elif selected_gate == "NAND" or selected_gate == "AND" or selected_gate == "CNOT" or selected_gate == "OR"   :
            # Hide input for Not and Toffoli gates
            self.input_label.grid_forget()
            self.input_entry.grid_forget()

            # Show inputs for NAND gate
            self.input_a_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            self.input_a_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
            self.input_b_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
            self.input_b_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        
    def display_circuit_diagram(self, gates_simulator):
    # Clear the previous circuit diagram, if any
        for widget in self.circuit_diagram_frame.winfo_children():
            widget.destroy()

        # Create a new figure for the circuit diagram
        figure = plt.Figure(figsize=(5, 2), tight_layout=True)
        canvas = FigureCanvasTkAgg(figure, master=self.circuit_diagram_frame)
        canvas_widget = canvas.get_tk_widget()

        # Draw the circuit on the new figure
        quantum_circuit = gates_simulator.get_quantum_circuit()
        quantum_circuit.draw(output='mpl', style='iqp', reverse_bits=False, scale=0.7, ax=figure.add_subplot(111))

        # Display the figure in the GUI
        canvas_widget.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    def visualize_bloch_vector(self, statevector):
        # Clear the existing canvas widget
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        # Close the previous Bloch vector figure, if it exists
        if hasattr(self, 'bloch_fig'):
            plt.close(self.bloch_fig)

        # Get the Bloch vector figure directly from plot_bloch_multivector
            
        if self.selected_gate_var.get() == "OR":
             self.bloch_fig = plot_bloch_multivector(statevector, figsize=(3, 2))
        else:
            self.bloch_fig = plot_bloch_multivector(statevector, figsize=(4, 3))

        # Embed the Matplotlib figure in the Tkinter GUI
        canvas_widget = FigureCanvasTkAgg(self.bloch_fig, master=self.canvas_frame)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack(side="top", fill="both", expand=1)

        # Configure the canvas to expand with the window
        canvas_widget.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Bind the Configure event to update the scroll region
        canvas_widget.get_tk_widget().bind("<Configure>", self.on_canvas_configure)


    def run_simulation(self):
        selected_gate = self.selected_gate_var.get()


        if selected_gate == "NAND":
            input_a = int(self.input_a_var.get())
            input_b = int(self.input_b_var.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            nand_simulator = NANDSimulator(input_a, input_b, draw)
            output_state = nand_simulator.simulate()
            # Update input and output labels
            self.input_result_label["text"] = f"|{input_a}{input_b}1>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(nand_simulator)

            qc = nand_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)
                
        elif selected_gate == "Not":
            input_c = int(self.input_entry.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            not_simulator = NotSimulator(input_c, draw)
            output_state = not_simulator.simulate()
            
            # Update input and output labels
            self.input_result_label["text"] = f"|11{input_c}>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(not_simulator)
            
            # Display the circuit diagram

            ##########################################################

            # Get the Bloch vector of the resulting state
            qc = not_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)



        elif selected_gate == "AND":
            input_a = int(self.input_a_var.get())
            input_b = int(self.input_b_var.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            and_simulator = ANDSimulator(input_a, input_b, draw)
            output_state=and_simulator.simulate()
            # Update input and output labels
            self.input_result_label["text"] = f"|{input_a}{input_b}0>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(and_simulator)
            # Get the Bloch vector of the resulting state
            qc = and_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)
            
        elif selected_gate == "CNOT":
            input_a = int(self.input_a_var.get())
            input_c = int(self.input_b_var.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            cnot_simulator = CNOTSimulator(input_a, input_c, draw)
            output_state=cnot_simulator.simulate()
            # Update input and output labels
            self.input_result_label["text"] = f"|{input_a}1{input_c}>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(cnot_simulator)
            # Get the Bloch vector of the resulting state
            qc = cnot_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)

        elif selected_gate == "FANOUT":
            input_c = int(self.input_entry.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            fanout_simulator = FANOUTSimulator(input_c, draw)
            output_state=fanout_simulator.simulate()
            # Update input and output labels
            self.input_result_label["text"] = f"|00{input_c}>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(fanout_simulator)
            # Get the Bloch vector of the resulting state
            qc = fanout_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)


        elif selected_gate == "OR":
            input_a = int(self.input_a_var.get())
            input_b = int(self.input_b_var.get())
            draw = True  # Set to False if you don't want to display the circuit diagram
            or_simulator = ORGateSimulator(input_a, input_b, draw)
            output_state=or_simulator.simulate()
            # Update input and output labels
            self.input_result_label["text"] = f"|{input_a}111{input_b}>"
            self.output_result_label["text"] = f"|{output_state}>"
            self.display_circuit_diagram(or_simulator)
            # Get the Bloch vector of the resulting state
            qc = or_simulator.get_quantum_circuit()
            simulator = Aer.get_backend('statevector_simulator')
            transpiled_qc = transpile(qc, simulator)

            # Simulate the transpiled quantum circuit
            result = simulator.run(transpiled_qc)
            statevector = result.result().get_statevector()
            self.visualize_bloch_vector(statevector)

 
if __name__ == "__main__":
    app = QuantumGateTesterApp()
    app.mainloop()