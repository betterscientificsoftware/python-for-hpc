## Python for HPC: ECP Community Materials

This site provides a combination of original resources and recommended links for Python users in
the ECP and broader scientific community. It is part of the [IDEAS-ECP](https://ideas-productivity.org/ideas-ecp) project.

### Quick-start Guides
 - [Python for HPC](tutorials/python.whatis.md)
 - [Creating a PYPI package](tutorials/python.pypi-packaging.md)
 - [Using Conda / Anaconda](tutorials/python.conda.md)
 - [Documenting with Sphinx](tutorials/python.doc-sphinx.md)

### Presentations and Webinars
 - [Python for High Performance Computing](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/ECP_Python_Tutorial_2018.pdf) ECP Annual Meeting 2018. William Scullin (ALCF), Matt Belhorn (OLCF) and Rollin Thomas (NERSC)
 - [HPC Python Testing and Debugging Tutorial 2018](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/debugging_slides.pdf) ECP Annual Meeting 2018. Matt Belhorn (OLCF), William Scullin (ALCF), Rollin Thomas (NERSC) 
 - [Analyzing Python Performance with Intel VTune](https://www.alcf.anl.gov/files/Tullos-Analyzing_Python_Performance.pdf) 2017 Intel presentation.
 - [Using and Scaling Python](https://www.alcf.anl.gov/files/Scullin-Pavlyk%20_SDL2018_Python.pdf) ALCF Simulation, Data, and Learning Workshop 2018. William Scullin (ALCF) and Oleksandr Pavlyk (Intel)
 - [Python in HPC Webinar 2017](https://www.exascaleproject.org/event/python-in-hpc-2) 

 
### Testing

 - [pytest](https://pytest.org) - Recommended testing framework. Easy-to-use, auto-discovery of tests, fixtures, many useful plugins (eg. pytest-cov, pytest-timeout).
 - [HPC Python Testing and Debugging Tutorial 2018](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/debugging_slides.pdf) ECP Annual Meeting 2018. Matt Belhorn (OLCF), William Scullin (ALCF), Rollin Thomas (NERSC) 
 
### Coding Standards and style
 - [YAPF](https://github.com/google/yapf) "Yet Another Python Formatter" Auto-formats Python to style-guides (select from built-in styles PEP8(default), Google, Chromium, Facebook). Also customisable.
 [Try online](https://yapf.now.sh/)
 
### Design Patterns
"Design Patterns are general, repeatable solutions to common recurring problems in software development." [From Wikipedia, the free encyclopedia, "Design pattern (computer science)"].
 - [python-patterns](https://github.com/faif/python-patterns) A collection of design patterns and idioms in Python with coded examples.

### Tips on Python for Scientific Computing
 - [Interrogating NumPy Configuration/Compiler Options](tutorials/interrogating_numpy.md)
 - [Links for moving from Matlab to NumPy](tutorials/matlab-numpy-conversion.md)
 
### Python resources for computational scientists
 - [XSD Python lecture/video series for Scientists](https://confluence.aps.anl.gov/display/XSDPT/XSD+Python+Training+Home) (From Argonne APS) Recommended as an introductory course for scientists.
 - [SciPy Lectures](http://www.scipy-lectures.org/) A community-based series of tutorials.
 - On-demand learning for Python - using a Transmedia Learning Framework [Webinar](https://ideas-productivity.org/events/hpc-best-practices-webinars/#webinar018) [Python TLF](https://bssw.io/resources/transmedia-learning-frameworks-tlf)
 - [MolSSI institue Best Practices](https://molssi.org/education/best-practices) A concise set of best practices that apply to all scientfic software. [Webinar](https://www.youtube.com/watch?v=44ryG3PHIew)

### Scientific Notebooks
 - [Jupyter Notebooks](http://jupyter.org/) The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. [Beginner's Video](https://www.youtube.com/watch?v=HW29067qVWk&t=1009s)
 - [Jupyter and HPC Webinar](https://www.exascaleproject.org/event/jupyter) Current State and Future Roadmap 2018
 
#### Examples:
 - [Electrostatics loop example](notebooks/Compiled_Examples.ipynb) A simple electrostatics loop implemented using pure Python, NumPy, Cython, Numba (inc GPU version) with timings. Contributed by Daniel Smith (MolSSI). [Notes on running](notebooks/running_compiled_examples.md)

### Scientific Libraries

#### Scientific computing packages in Python (running C extensions):
 - [NumPy](http://www.numpy.org/) NumPy is the fundamental package for scientific computing with Python.
 - [SciPy](https://www.scipy.org/) A Python-based ecosystem of open-source software for mathematics, science, and engineering. Now incorporates: Numpy, the SciPy library, Matplotlib, IPython, SymPy and Pandas.
 
#### Parallel and Distributed Programming Options:
 
 Note: Python provides an in-built [threading](https://docs.python.org/3/library/threading.html) module. However, this is not really suitable for parallel computation due to the [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) (Global Interpreter Lock)
 
 - [mpi4py](https://mpi4py.readthedocs.io/en/stable/) Python wrapper for MPI
 - [Multiprocessing module](https://docs.python.org/3/library/multiprocessing.html) Basic multiple process parallelism through forked interpreters (with threading like interface). Be aware of issues mixing with OpenMP, MPI, or shared memory tools.


#### Python bindings to scientific libraries in HPC:
 - [petsc4py](https://bitbucket.org/petsc/petsc4py) Python bindings for PETSc
 - [slepc4py](https://bitbucket.org/slepc/slepc4py) Python bindings for SLEPc, the Scalable Library for Eigenvalue Problem Computations
 - [PyTrilinos](https://trilinos.org/packages/pytrilinos/) A set of python wrappers for selected Trilinos packages

#### I/O:
 - [h5py](https://www.h5py.org/) The h5py package is a Pythonic interface to the HDF5 binary data format.


### Speeding up Python
 - [Cython](http://cython.org/) Create C code from modified Python. Enables performance and threading [Beginners video](https://www.youtube.com/watch?v=NfnMJMkhDoQ&list=PLhsR3m5MO5X6T4Bs_9h1azJoQ9srQmQAC)
 - [PyPy](https://pypy.org/) Implementation of the Python language that JIT compiles for performance. No code changes required.
 - [Numba](https://numba.pydata.org/) Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code. Numba supports Intel and AMD x86, POWER8/9, and ARM CPUs, NVIDIA and AMD GPUs. Relies on decorators to identify code sections to accelerate. Requires LLVM for compiler, but works with the standard CPython.  [Accelerating Python with Numba (Video)](https://www.youtube.com/watch?v=eYIPEDnp5C4) 
 - Note: A growing alternative to speeding up Python is the compiled language [Julia](https://julialang.org/)

#### Or to create your own Python bindings to compiled code:
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


### Ensemble and Workflow tools
 - [Parsl](http://parsl-project.org) Use Parsl with Jupyter notebooks to scale interactive analyses from laptops to supercomputers. [video](https://www.youtube.com/watch?v=tHTt0Pyb4_M)
 - [Balsam](https://www.alcf.anl.gov/balsam) Workflow system for managing large campaigns of interdependent jobs (unlimited queue depth). Balsam manages a database of jobs, with specified dependences. Jobs can be added to the database from anywhere on the system, for dynamic workflows.
 - [libEnsemble](https://libensemble.readthedocs.io) Library for dynamic ensembles using generator and simulator functions (e.g. using numerical optimization).


### Conferences and Events
 - [SciPy 2018 Videos](https://www.youtube.com/playlist?list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR)
 - [ALCF Simulation, Data and Learning Workshop 2018](https://www.alcf.anl.gov/workshops/sdl-workshop-oct2018) Includes slides for many relevant presentations.
 - PyHPC Workshop 2018 (In conjunction with SC18) [Announcements](https://twitter.com/pythonhpc?lang=en) [Register](https://www.dlr.de/sc/desktopdefault.aspx/tabid-12954/22625_read-52397/)
 
Find more software engineering materials for computational scientists at the [Better Scientific Software](https://bssw.io/) website.


### Alternatives to Python
 - [Julia](https://julialang.org/) A scripting like language that compiles to efficient native code for multiple platforms via LLVM.

### Feedback

Any feedback, corrections, and suggested additions are welcome: shudson@anl.gov
Or raise a github [issue](https://github.com/betterscientificsoftware/python-for-hpc/issues) in this repository (esp. broken links etc).

<iframe src="https://ghbtns.com/github-btn.html?user=betterscientificsoftware&repo=python-for-hpc&type=star&count=false&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe>
