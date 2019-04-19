---
layout: single
permalink: /python-for-hpc/
title: "Python for HPC: ECP Community Materials"
author_profile: false
sidebar:
  nav: "content"
---


<!-- # Python for HPC: ECP Community Materials -->

## Getting Started

This site provides a combination of original resources and recommended links for Python users in
the ECP and broader scientific community. It is part of the [Better Scientific Software](https://bssw.io/) initiative.

Discuss this page on [slack](https://join.slack.com/t/bssw-python/shared_invite/enQtNDcxNDA3OTg0OTYwLTAyOGY0YjdhNDUzOTE1NGUwNGM4MDI1ZDQwY2U3OGY2NzQxZWE4ZDZiZjM2OTEzNDRkNDBkZTEyMDVlMDM2NTE)

### Quick-Start Guides
 - [Python for HPC]({{site.baseurl}}/tutorials/python-whatis/)
 - [Creating a PYPI package]({{site.baseurl}}/tutorials/python-pypi-packaging/)
 - [Using Conda / Anaconda]({{site.baseurl}}/tutorials/python-conda/)
 - [Documenting with Sphinx]({{site.baseurl}}/tutorials/python-doc-sphinx/)
 
 - [Python 102](https://python-102.readthedocs.io/en/latest/index.html) Covers topics that are essential for scientific computing and data analysis in Python, but typically not covered in an introductory course or workshop.

### Presentations and Webinars
 - [Python for High Performance Computing](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/ECP_Python_Tutorial_2018.pdf) ECP Annual Meeting 2018. William Scullin (ALCF), Matt Belhorn (OLCF) and Rollin Thomas (NERSC)
 - [HPC Python Testing and Debugging Tutorial 2018](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/debugging_slides.pdf) ECP Annual Meeting 2018. Matt Belhorn (OLCF), William Scullin (ALCF), Rollin Thomas (NERSC) 
 - [Analyzing Python Performance with Intel VTune](https://www.alcf.anl.gov/files/Tullos-Analyzing_Python_Performance.pdf) 2017 Intel presentation.
 - [Using and Scaling Python](https://www.alcf.anl.gov/files/Scullin-Pavlyk%20_SDL2018_Python.pdf) ALCF Simulation, Data, and Learning Workshop 2018. William Scullin (ALCF) and Oleksandr Pavlyk (Intel)
 - [Python in HPC Webinar 2017](https://www.exascaleproject.org/event/python-in-hpc-2) 
 - [Python on Summit](https://www.olcf.ornl.gov/wp-content/uploads/2019/02/STW_Feb_20190211_summit_workshop_python.pdf) OLCF Feb 2019 [Note on mpi4py]({{site.baseurl}}/tutorials/summit-mpi4py-note.md)

### Python Resources for Scientists
 - [XSD Python lecture/video series for Scientists](https://confluence.aps.anl.gov/display/XSDPT/XSD+Python+Training+Home) (From Argonne APS) Recommended as an introductory course for scientists.
 - [SciPy Lectures](http://www.scipy-lectures.org/) A community-based series of tutorials.
 - On-demand learning for Python - using a Transmedia Learning Framework [Webinar](https://ideas-productivity.org/events/hpc-best-practices-webinars/#webinar018) [Python TLF](https://bssw.io/resources/transmedia-learning-frameworks-tlf)
 - [MolSSI institue Best Practices](https://molssi.org/education/best-practices) A concise set of best practices that apply to all scientfic software. [Webinar](https://www.youtube.com/watch?v=44ryG3PHIew)
 
 
## Best Practices in Python

### Testing

 - [pytest](https://pytest.org) - Recommended testing framework. Easy-to-use, auto-discovery of tests, fixtures, many useful plugins (eg. pytest-cov, pytest-timeout).
 - [HPC Python Testing and Debugging Tutorial 2018](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/debugging_slides.pdf) ECP Annual Meeting 2018. Matt Belhorn (OLCF), William Scullin (ALCF), Rollin Thomas (NERSC) 
 
### Coding Standards and Style
 - [YAPF](https://github.com/google/yapf) "Yet Another Python Formatter" Auto-formats Python to style-guides (select from built-in styles PEP8(default), Google, Chromium, Facebook). Also customisable.
 [Try online](https://yapf.now.sh/)
 
### Design Patterns
"Design Patterns are general, repeatable solutions to common recurring problems in software development." [From Wikipedia, the free encyclopedia, "Design pattern (computer science)"].
 - [python-patterns](https://github.com/faif/python-patterns) A collection of design patterns and idioms in Python with coded examples.

### Tips on Python for Scientific Computing
 - [Interrogating NumPy Configuration/Compiler Options]({{site.baseurl}}/tutorials/interrogating-numpy/)
 - [Links for moving from Matlab to NumPy]({{site.baseurl}}/tutorials/matlab-numpy-conversion/)
 
 
## Scientific Notebooks

### Jupyter Notebooks

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text

 - [Jupyter Notebooks](http://jupyter.org/) Official Documentation
 - [Beginners Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
 - [Beginner's Video](https://www.youtube.com/watch?v=HW29067qVWk&t=1009s)

### Example: Python at Speed
 - [Electrostatics loop example]({{site.baseurl}}/notebooks/Compiled_Examples.ipynb) A simple electrostatics loop implemented using pure Python, NumPy, Cython, Numba (inc GPU version) with timings. Contributed by Daniel Smith (MolSSI). [Notes on running]({{site.baseurl}}/notebooks/running-compiled-examples/)
 
### Jupyter on Supercomputers
 
Some HPC centres now support running Jupyter notebooks on supercomputers. Accounts on these
systems is required to access the Jupyterhub servers.

### Jupyter at NERSC

 - [Jupyter and HPC Webinar](https://www.exascaleproject.org/event/jupyter) Current State and Future Roadmap 2018. Includes information on NERSC's support for running notebooks on Cori.

 - [Example Notebook with Slurm](https://github.com/NERSC/example-jupyter-notebooks) A NERSC example using SLURM magic (provided by Rollin Thomas).
 - [More NERSC Examples](https://github.com/NERSC?language=jupyter+notebook)

 
### Jupyter at Argonne

The ALCF (Argonne Leadship Computing Facility) now supports Notebooks on Theta and Cooley. An ALCF account is required.
 - [Theta](https://jupyter.alcf.anl.gov/theta/hub/login) Jupyterhub for Theta
 - [Cooley](https://jupyter.alcf.anl.gov/hub/login) Jupyterhub for Cooley
 - [Using Jupyter on Theta]({{site.baseurl}}/notebooks/explore_theta_jupyterhub.ipynb) A notebook for getting started with Jupyter on Theta


## Scientific Programming in Python

### Scientific Computing Packages:
 - [NumPy](http://www.numpy.org/) NumPy is the fundamental package for scientific computing with Python.
 - [SciPy](https://www.scipy.org/) A Python-based ecosystem of open-source software for mathematics, science, and engineering. Now incorporates: Numpy, the SciPy library, Matplotlib, IPython, SymPy and Pandas.
 
### Speeding up Python

These packages all involve creating compiled code from Python. This can be done using packages such as [NumPy and SciPy](#scientific-programming-in-python). Alternatively, you can use tools to compile Python code. Some popular ones are given below.

 - [Cython](http://cython.org/) Create C code from modified Python. Enables performance and threading [Beginners video](https://www.youtube.com/watch?v=NfnMJMkhDoQ&list=PLhsR3m5MO5X6T4Bs_9h1azJoQ9srQmQAC)
 - [PyPy](https://pypy.org/) Implementation of the Python language that JIT compiles for performance. No code changes required.
 - [Numba](https://numba.pydata.org/) Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code. Numba supports Intel and AMD x86, POWER8/9, and ARM CPUs, NVIDIA and AMD GPUs. Relies on decorators to identify code sections to accelerate. Requires LLVM for compiler, but works with the standard CPython.  [Accelerating Python with Numba (Video)](https://www.youtube.com/watch?v=eYIPEDnp5C4) 
 - Note: A growing alternative to speeding up Python is the compiled language [Julia](https://julialang.org/)

### Create Python Bindings to Code:
 - [SWIG](http://www.swig.org/) – Generate bindings to C/C++. Works with Python and other high level languages.
 - [F2PY](https://docs.scipy.org/doc/numpy-1.15.0/f2py/index.html) – Create Python interfaces to Fortran (part of NumPy).
 - [PyBind11](https://pybind11.readthedocs.io/en/master/) – “seamless operability between C++11 and Python”
 - [Boost.Python](https://www.boost.org/doc/libs/1_68_0/libs/python/doc/html/index.html) – “seamless operability between C++ and Python”
 - [ctypes](https://docs.python.org/3/library/ctypes.html) – built-in Python FFI for interfacing C
 
 - Recommended reading: [Python modules in C](http://dan.iel.fm/posts/python-c-extensions)

### Python on Accelerators
 - [Numba](https://numba.pydata.org/) supports GPUS (see description above). 
 - [PyCUDA](https://documen.tician.de/pycuda/tutorial.html)
   PyCUDA lets you access Nvidia's CUDA parallel computation API from Python.
 - [PyOpenCL](https://documen.tician.de/pyopencl/index.html)
   PyOpenCL lets you access the OpenCL parallel computation API from Python
 - [CuPy](https://cupy.chainer.org/) NumPy-like API accelerated with CUDA) [github](https://github.com/cupy/cupy)


 
## Parallel and Distributed Programming:

### Shared Memory Parallelism
 
 Note: Python provides an in-built [threading](https://docs.python.org/3/library/threading.html) module. However, this is not really suitable for parallel computation due to the [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) (Global Interpreter Lock)
 
 - [Multiprocessing module](https://docs.python.org/3/library/multiprocessing.html) Basic multiple process parallelism through forked interpreters (with threading like interface). Be aware of issues mixing with OpenMP, MPI, or shared memory tools.
 

### Distributed Memory Parallelism

 - [mpi4py](https://mpi4py.readthedocs.io/en/stable/) Python wrapper for MPI
 - [PyCOMPSs](https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/) PyCOMPSs is a programming model that enables the parallelization of sequential Python codes following a task-based approach. PyCOMPSs enables the execution in distributed infrastructures, such as Clusters, Grids, Clouds, and containers.


## Scientific Libraries for HPC

### Python Bindings to HPC Libraries:
 - [petsc4py](https://bitbucket.org/petsc/petsc4py) Python bindings for PETSc/Tao, the scalable Library for partial differential equations, and numerical optimization.
 - [slepc4py](https://bitbucket.org/slepc/slepc4py) Python bindings for SLEPc, the Scalable Library for Eigenvalue Problem Computations
 - [PyTrilinos](https://trilinos.org/packages/pytrilinos/) A set of python wrappers for selected Trilinos packages

### I/O Libraries:
 - [h5py](https://www.h5py.org/) The h5py package is a Pythonic interface to the HDF5 binary data format.

### Ensemble and Workflow Tools
 - [Parsl](http://parsl-project.org) Use Parsl with Jupyter notebooks to scale interactive analyses from laptops to supercomputers. [video](https://www.youtube.com/watch?v=tHTt0Pyb4_M)
 - [Balsam](https://www.alcf.anl.gov/balsam) Workflow system for managing large campaigns of interdependent jobs (unlimited queue depth). Balsam manages a database of jobs, with specified dependences. Jobs can be added to the database from anywhere on the system, for dynamic workflows.
 - [libEnsemble](https://libensemble.readthedocs.io) Library for dynamic ensembles using generator and simulator functions (e.g. using numerical optimization).

 
## Other
 
### Conferences and Events

**Upcoming:**
 - [SciPy 2019 Austin, Texas, July 8-14th](https://www.scipy2019.scipy.org/)


**Previous Events:**

 - [SciPy 2018 Videos](https://www.youtube.com/playlist?list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR)
 - [ALCF Simulation, Data and Learning Workshop 2018](https://www.alcf.anl.gov/workshops/sdl-workshop-oct2018) Includes slides for many relevant presentations.
 - PyHPC Workshop 2018 (In conjunction with SC18) [Twitter page](https://twitter.com/pythonhpc?lang=en)
 
Find more software engineering materials for computational scientists at the [Better Scientific Software](https://bssw.io/) website.


### Alternatives to Python
 - [Julia](https://julialang.org/) A scripting like language that compiles to efficient native code for multiple platforms via LLVM.


### Feedback

Any feedback, corrections, and suggested additions are welcome: shudson@anl.gov
Or raise a github [issue](https://github.com/betterscientificsoftware/python-for-hpc/issues) in this repository (esp. broken links etc).

<iframe src="https://ghbtns.com/github-btn.html?user=betterscientificsoftware&repo=python-for-hpc&type=star&count=false&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe>
