mpi4py on Summit
================

### Contributed by [Steve Hudson](https://github.com/shuds13)

At time of writing (Feb 2019) I've found the following works for mpi4py on Python.

The gcc/4.8.5 must be loaded (replacing xl compilers).

Then use:

    CC=mpicc MPICC=mpicc pip install mpi4py --no-binary mpi4py
    
Note both CC and MPICC are set to mpicc

Full example from login (Create Conda environment and install mpi4py):

    module load python # Loads Anaconda
    module load gcc/4.8.5
    conda create --name myenv # First time
    . activate myenv
    conda install pip # So pip installs stuff in the right place
    CC=mpicc MPICC=mpicc pip install mpi4py --no-binary mpi4py # Install from source
