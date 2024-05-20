import numpy as np


# Data for Fig.7a

thetas_fig8a = np.load('Fig8a_theta.npy') # Array with shape (100,N). They are the N angles of each circuit. Here, N = 16.
qubits_fig8a = np.load('Fig8a_qubits.npy') # Array with shape (100,N). They are the N indeces of the physical qubits used for each circuit. Here, N = 16.
mz_fig8a = np.load('Fig8a_mz_exact.npy') # Array with shape (100,). They are the exact average magnetization per qubit for each circuit.
mz_noisy_fig8a = np.load('Fig8a_z_noisy.npy') # Array with shape (100,N). They are the noisy single qubit expectation values of the observable Z for each qubit of each circuit. Here, N = 16.
mz_zne_fig8a = np.load('Fig8a_mz_zne.npy') # Array with shape (100,). They are the noisy average magnetization per qubit for each circuit after zero noise extrapolation.
mz_cnn_fig8a = np.load('Fig8a_mz_predicted.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the convolutional neural network.
mz_linear_fig8a = np.load('Fig8a_mz_linear.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the linear regression model.


# Data for Fig.7b

thetas_fig8b = np.load('Fig8b_theta.npy') # Array with shape (100,P). They are the N angles of each circuit. Here, P = 20.
qubits_fig8b = np.load('Fig8b_qubits.npy') # Array with shape (100,N). They are the N indeces of the physical qubits used for each circuit. Here, N = 16.
mz_fig8b = np.load('Fig8b_mz_exact.npy') # Array with shape (100,). They are the exact average magnetization per qubit for each circuit.
mz_noisy_fig8b = np.load('Fig8b_z_noisy.npy') # Array with shape (100,N). They are the noisy single qubit expectation values of the observable Z for each qubit of each circuit. Here, N = 16.
mz_zne_fig8b = np.load('Fig8b_mz_zne.npy') # Array with shape (100,). They are the noisy average magnetization per qubit for each circuit after zero noise extrapolation.
mz_cnn_fig8b = np.load('Fig8b_mz_predicted.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the convolutional neural network.
mz_linear_fig8b = np.load('Fig8b_mz_linear.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the linear regression model.


# Data for Fig.7c

thetas_fig8c = np.load('Fig8c_theta.npy') # Array with shape (100,P). They are the N angles of each circuit. Here, P = 20.
qubits_fig8c = np.load('Fig8c_qubits.npy') # Array with shape (100,N). They are the N indeces of the physical qubits used for each circuit. Here, N = 16.
mz_fig8c = np.load('Fig8c_mz_exact.npy') # Array with shape (100,). They are the exact average magnetization per qubit for each circuit.
mz_noisy_fig8c = np.load('Fig8c_z_noisy.npy') # Array with shape (100,N). They are the noisy single qubit expectation values of the observable Z for each qubit of each circuit. Here, N = 16.
mz_zne_fig8c = np.load('Fig8c_mz_zne.npy') # Array with shape (100,). They are the noisy average magnetization per qubit for each circuit after zero noise extrapolation.
mz_cnn_fig8c = np.load('Fig8c_mz_predicted.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the convolutional neural network.
mz_linear_fig8c = np.load('Fig8c_mz_linear.npy') # Array with shape (100,). They are the average magnetization per qubit for each circuit predicted by the linear regression model.
