import level3
import jax.numpy as np
from jax import grad, jit
import matplotlib.pyplot as plt
import time

def optimise_JPw_2(data, step_size_effect, n_subsamples, N_E, N_I, contrasts, orientations, J_init, P_init, w_init, T_inv, tau, tau_ref, pref_E, pref_I, g, w_ff, sig_ext):
    params = np.array(J_init[0,0])
    rand_mat = level3.random_matrix(N_E + N_I)  # Put inside gradient descent loop

    def optimising_func(J1):

        J = np.array([[J1, J_init[0,1]], [J_init[1,0], J_init[1,1]]])
        return level3.loss_from_parameters(data, step_size_effect, n_subsamples, rand_mat, N_E, N_I, contrasts, orientations, J, P_init, w_init, T_inv, tau, tau_ref, pref_E, pref_I, g, w_ff, sig_ext)

    gradient_func = jit(grad(optimising_func))
    jit_func = jit(optimising_func)

    for i in range(3):
        print("params: " + str(params))
        t0 = time.process_time()

        loss = jit_func(params)

        t1 = time.process_time()
        print("loss: " + str(loss))
        print("cpu time: " + str(t1 - t0))
        
        gradient = gradient_func(params)
        
        t2 = time.process_time()
        print("gradient: " + str(gradient))
        print("cpu time: " + str(t2 - t1))

    print(loss)


def optimise_JPw(data, step_size_effect, n_subsamples, N_E, N_I, contrasts, orientations, J_init, P_init, w_init, T_inv, tau, tau_ref, pref_E, pref_I, g, w_ff, sig_ext):
    params = np.array([J_init, P_init, w_init])
    rand_mat = level3.random_matrix(N_E + N_I)

    def optimising_func(params):
        return level3.loss_from_parameters(data, step_size_effect, n_subsamples, rand_mat, N_E, N_I, contrasts, orientations, *params, T_inv, tau, tau_ref, pref_E, pref_I, g, w_ff, sig_ext)

    gradient_func = grad(optimising_func)

    for i in range(3):
        print("params: " + str(params))
        t0 = time.process_time()

        loss = optimising_func(params)
        t1 = time.process_time()
        print("loss: " + str(loss))
        print("cpu time: " + str(t1 - t0))
        
        gradient = gradient_func(params)
        
        t2 = time.process_time()
        print("gradient: " + str(gradient))
        print("cpu time: " + str(t2 - t1))

    print(loss)