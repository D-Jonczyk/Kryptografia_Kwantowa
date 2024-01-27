from qiskit import QuantumCircuit, Aer, execute


def create_xor_circuit(input1, input2):
    qc = QuantumCircuit(2, 1)

    # Ustawianie stanów wejściowych
    if input1:
        qc.x(0)
    if input2:
        qc.x(1)

    # Implementacja bramki XOR
    qc.cx(0, 1)
    qc.measure(1, 0)

    return qc


def run_xor_simulation(input1, input2):
    qc = create_xor_circuit(input1, input2)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    measurements = result.get_counts(qc)

    # Generowanie wizualizacji obwodu
    circuit_image = qc.draw(output='mpl')

    return next(iter(measurements)), circuit_image
