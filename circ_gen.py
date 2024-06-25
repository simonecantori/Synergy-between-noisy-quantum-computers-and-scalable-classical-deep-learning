'''

The following code is compatible with Qiskit version >= 1.0.
While the results presented in the paper were obtained using an older version of Qiskit, we have tried to update
the code to ensure it runs with the latest versions of Qiskit.
'''

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime.fake_provider import FakeGuadalupe
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.primitives import StatevectorEstimator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

def OrigCircSim(h, N, P): 
    qc = QuantumCircuit(N)
    valcount_output = np.zeros((N))
    valcount_output_ideal = np.zeros((N))
    for j in range(P):
        for i in range(N):
            qc.rx(h[j],i) 
        for i in range(N-1):
            if qubits_used[i]==8 or qubits_used[i]==12 or qubits_used[i]==7:
                qc.rzz(-np.pi/2,i,i+1)
                if i+2<N:
                    qc.rzz(-np.pi/2,i,i+2)
            elif qubits_used[i]!=9 and qubits_used[i]!=15 and qubits_used[i]!=6:
                qc.rzz(-np.pi/2,i,i+1)  
    pm = generate_preset_pass_manager(backend=sim,optimization_level=0,initial_layout=list(qubits_used))
    transpiled_circuit = pm.run(qc)

    observables_layout = []
    for i in observables:
        observables_layout.append(i.apply_layout(layout=transpiled_circuit.layout))
    pub = (transpiled_circuit, observables_layout)
    # In the original code we used a fixed number of shots (10^4). In Qiskit 1.0, one can use an arbitrary precision 
    result = estimator_noisy.run(pubs=[pub],precision=np.sqrt(1/shot)).result()
    valcount_output = np.flip(result[0].data.evs)

    pub = (qc, observables)
    result = estimator.run(pubs=[pub]).result()
    valcount_output_ideal = np.flip(result[0].data.evs)

    return valcount_output, valcount_output_ideal

    
if __name__ == '__main__':
    shot = 10000
    mit0 = 100 
    mit = mit0/100 #p_noise
    nm = NoiseModel.from_backend(FakeGuadalupe())
    qc = QuantumCircuit(2)
    qc.id(0)
    qc.id(1) 
    if mit0 != 100:
        for i in nm._local_quantum_errors['cx'].keys():
            prob_count = 0
            (nm._local_quantum_errors['cx'][i].circuits).append(qc)
            (nm._local_quantum_errors['cx'][i].probabilities).append(0)
            for j in range(len(nm._local_quantum_errors['cx'][i].probabilities)):
                nm._local_quantum_errors['cx'][i].probabilities[j] *= mit
                prob_count += nm._local_quantum_errors['cx'][i].probabilities[j]
            nm._local_quantum_errors['cx'][i].probabilities[-1] = 1 - prob_count
    sim = AerSimulator(noise_model = nm)
    estimator_noisy = Estimator(backend=sim)
    estimator = StatevectorEstimator()
    
    P = 20
    N = 10
    association_list = [0,1,2,3,5,8,9,11,14,13,12,15,10,7,6,4]
    observables = []
    for i in range(N):
        s = "I" * N
        s = s[:i] + 'Z' + s[i+1:]
        observables.append(SparsePauliOp.from_list([(s,1)]))
    num_samples = 1

    J_npy = []
    h_npy = []
    output_npy = []
    output_ideal_npy = []
    qubits_used_npy = []
    for s in range(num_samples):
        h = np.random.uniform(0,np.pi/2,size=P)
        while True:
            start = np.random.randint(0,17-N)
            if association_list[start]!=9 and association_list[start]!=15 and association_list[start]!=6:
                break
        qubits_used= np.copy(association_list[start:start+N])
        output, output_ideal = OrigCircSim(h, N, P)

        h_npy.append(h)
        output_npy.append(output)
        output_ideal_npy.append(output_ideal)
        qubits_used_npy.append(qubits_used)


