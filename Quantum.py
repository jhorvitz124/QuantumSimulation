from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Function to create a Bell state
def create_bell_pair(qc, a, b):
    qc.h(a)
    qc.cx(a, b)

# Function to measure qubits
def measure_pair(qc, a, b):
    qc.cx(a, b)
    qc.h(a)
    qc.measure(a, 0)
    qc.measure(b, 1)

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2, 2)

# Create a Bell state
create_bell_pair(qc, 0, 1)

# Measure qubits
measure_pair(qc, 0, 1)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, simulator)
qobj = assemble(transpiled_qc)
result = simulator.run(qobj).result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
plt.show()
