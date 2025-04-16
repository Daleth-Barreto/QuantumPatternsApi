import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

simulator = AerSimulator()
num_qubits = 3

qr = QuantumRegister(num_qubits, 'q')
cr = ClassicalRegister(num_qubits, 'c')

def create_simple_pattern_circuit(qubits, x, y):
    qc = QuantumCircuit(qubits)
    for i in range(num_qubits):
        qc.h(i)
        qc.ry(np.sin(x * i) + np.cos(y * i), i)
    qc.measure_all(qr, cr)
    return qc

def create_pattern_circuit(qubits, x, y, pattern_type):
    qc = QuantumCircuit(qubits)
    for i in range(num_qubits):
        qc.h(i)
        if pattern_type == "circular":
            qc.ry(np.sin(np.sqrt(x**2 + y**2)) * i, i)
        elif pattern_type == "waves":
            qc.ry(np.sin(x + y) * i, i)
        elif pattern_type == "checkerboard":
            qc.ry((x + y) % 2 * np.pi/2, i)
        else:
            qc.ry(np.random.uniform(0, 2 * np.pi), i)
    qc.measure_all(qr, cr)
    return qc

def quantum_pattern_word(qubits, x, y, word):
    qc = QuantumCircuit(qubits)
    for i, char in enumerate(word):
        angle = ord(char) * np.pi / 180
        qc.ry(angle, i % num_qubits)
    for i in range(num_qubits):
        qc.cry(x * i + y * (num_qubits - i), i, (i + 1) % num_qubits)
    qc.measure_all(qr, cr)
    return qc

def simulate_circuit(qc):
    job = simulator.run(qc, shots=1)
    counts = job.result().get_counts()
    pixel_value = list(counts.keys())[0][::-1]
    r = int(pixel_value[0]) * 255
    g = int(pixel_value[1]) * 255
    b = int(pixel_value[2]) * 255
    return (r, g, b)

def generate_image(qubits, width, height, circuit_function, pattern_type=None, word=None):
    pixel_data = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for y in range(height):
            for x in range(width):
                if word:
                    qc = circuit_function(qubits, x, y, word)
                elif pattern_type:
                    qc = circuit_function(qubits, x, y, pattern_type)
                else:
                    qc = circuit_function(qubits, x, y)
                futures.append(executor.submit(simulate_circuit, qc))
        
        # Recolectar los resultados de las simulaciones en paralelo
        for future in futures:
            pixel_data.append(future.result())

    image = np.array(pixel_data).reshape((height, width, 3))
    return image

def generate_pattern_image(data):
    if data.pattern_type == "simple":
        image = generate_image(qr, data.width, data.height, create_simple_pattern_circuit)
    elif data.pattern_type == "word" and data.word:
        image = generate_image(qr, data.width, data.height, quantum_pattern_word, word=data.word)
    else:
        image = generate_image(qr, data.width, data.height, create_pattern_circuit, pattern_type=data.pattern_type)

    # ✅ Asegurarse de que el tipo de dato sea uint8
    image = np.array(image)
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)

    # Convertir a PNG
    buf = BytesIO()
    plt.imsave(buf, image, format='png')
    buf.seek(0)
    return buf.read()
