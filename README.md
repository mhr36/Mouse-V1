# Mouse-V1
Alternative approach to the problem of modelling mouse primary visual cortex as a recurrent neural network.
The class structure of the previous attempt (Neural-Data-Analysis) has been replaced by a procedural structure.
This structure better lends itself to the use of JAX since TracerArrays can be passed between functions and multiple
threads can run at the same time.