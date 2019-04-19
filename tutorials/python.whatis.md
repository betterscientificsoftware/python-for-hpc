---
author: Stephen Hudson
layout: single
permalink: /tutorials/python-whatis/
title: "Python for HPC"
author_profile: true
sidebar:
  nav: "content"
---
<!--# Python: Python for HPC-->

<!-- ### Contributed by [Steve Hudson](https://github.com/shuds13) -->

## Introduction

Python is a very popular language in many domains. Traditionally, these are domains where speed of development and portability are more important than code performance. However, Python has now become popular in scientific computing and is becoming a de facto language for data science. It is commonly used for rapid prototyping of numerical software, and is becoming increasingly popular for implementing production software. It is also used for application connectivity (glue) in many scientific workflows.

Designed as an interpreted language, Python does not have the speed of compiled code and sometimes will not be the appropriate tool. However, Python has a number of extensions/tools for increasing performance through various mechanisms for generating compiled code. The most common of these is the C extension libraries such as NumPy/SciPy. Python can also be parallelized using the module mpi4py - built upon MPI.

Python is free and open-source which enables easy use across platforms, and a huge resource of community development and support.

Python also supports multiple programming paradigms including procedural, object-oriented and functional programming.


## The workings of Python

The most common Python interpreter is CPython (written in C). CPython translates modules to bytecode when they are imported. CPython then runs, interpreting and executing the bytecode instructions while performing supporting services, such as determining the types of variables and controlling memory allocation and deallocation (garbage collecting). This run-time memory management causes a performance overhead, but saves the programmer this overhead in terms of rapid development.

By default, the bytecode is kept after the first time it is compiled. These will show as <module_name>.pyc files. For Python3 these are kept in a `__pycache__` subdirectory.

While CPython runs as a bytecode interpreter, the Python language, like any language, can be compiled, and alternatives to CPython exist (see below). None of these have become as popular as CPython, however, which is ubiquitous and works well with the large resource of C extensions.

Python3 is recommended for new users, although there is still considerable use of Python2. The latest version of Python2 is 2.7. Python2 is due to be offically maintained until 1st January 2020. Many new features are added to Python3 regularly and all major libraries now work under Python3.5+.


## Rapid development

One famous advantage of Python is the capability to implement complex tasks in only a few simple lines of code. The key reason for this is code re-use via both an in-built and vast online resource of modules.

As Python is interpreted, most of these modules can be simply imported and used without any pre-compilation. CPython will translate to bytecode, only those components/submodules that are imported by the program. 

Due to Python's popularity, this is accompanied by a vast online resource of community support, which will often provide exact, or very close, instructions on how to accomplish the desired task (e.g. Stack Overflow).

Modules include, for example, tools to access system libraries/variables, plot graphs, manipulate images and many domain specific toolsets. This gives Python enormous flexibility. It also has multiple unit-testing frameworks available including the built-in unittest and the popular pytest.

Due to the above, it is fairly simple to get started with Python. It is also very simple to start an interactive interpreter to test out code. This interactive capability can be augmented with use of iPython/Jupyter notebooks.


## Performance for compute intensive code

To take advantage of mathematical/linear algebra functions which are numerically intensive, the NumPy and SciPy modules are recommended. These are not pure Python packages, but rather are mostly written in C with Python bindings. When these functions are run, the Python interpreter yields to compiled code, giving the speed of compiled C, called from a Python program. This can provide good numerical performance when the intensive loops of the code can be composed of these functions.

These packages are available as pre-compiled binaries for common platforms, but may also be compiled by the user. The pre-compiled binaries, are likely to have standard optimization flags, but not specialist platform flags. They usually do not have AVX, for example. Some of these functions may also make use of multiple threads/cores available on the system (as they are in compiled code, Pythons global interpreter lock is released *see below).

It should be noted that a number of NumPy/SciPy linear algebra functions are calling underlying BLAS and LAPACK libraries for the bulk of the computation. These may vary in speed significantly from the reference implementations (provided by Netlib) to high performance implementations such as OpenBLAS, ATLAS and Intel's MKL (all of which are now openly available).

Instructions to discover the configuration and compiler options for your installed version of NumPy, as well as the linked BLAS library, are provided [here](../tutorials/interrogating_numpy.md).

A good benchmark for the different BLAS implementations can be found [in this blog](http://markus-beuckelmann.de/blog/boosting-numpy-blas.html).

To see if threading is being employed across cores, use top or htop while running. Hint: In top - press 1 to run to toggle a list of each core - the first column shows the time in your program (us = userspace time).

## Further performance enhancement

To improve performance of code that cannot be composed in terms of existing extensions, there are a number of existing alternatives to gain advantage from code compilation.

Alternative Python interpreters/compilers/tools E.g:

* Cython for augmented Python code that is compiled to C code

* PyPy (a JIT-compiled Python written in Python - compiles loops on the fly)

* Numba (Annotate code with decoraters to compile selected functions - supports CPUs and GPUs)

* SWIG for quickly creating interfaces for C extensions.

Note that PyPy is not yet 100% compatible with CPython and all modules.
    
There are many more alternative Pythons available.


## Parallelism

*Note on threading:*  CPython employs the GIL (Global Interpreter Lock). This means that only one thread can access the interpreter's memory space at a time. Threads may still be employed via the `threading` module, and may obtain a performance advantage when performing I/O etc... However, Python computation will not see significant speedups from multi-threading. Note that the GIL is released for C extensions such as NumPy.

The multiprocessing module was created to solve this problem. This provides a thread-like interface while generating multiple copies of the Python interpreter that can run on multiple cores. The threads can communicate via special shared variables, pipes and queues. The multiprocessing module, however, does not tend to mix well with other parallel threading tools or MPI, and should be used with some caution.

[mpi4py](https://mpi4py.readthedocs.io) provides Python bindings to the systems underlying MPI library to provide distributed parallelism. It exposes the full feature set and scalability of MPI.


## Package managers

Recommended package managers for installing modules include pip and Conda. pip is the de facto standard package manager for Python. However, Conda has become very popular, particularly in scientific environments. pip can also be used inside Conda environments.

### pip

pip is a package management system, specifically designed for installing Python packages from the Internet hosted Python Package Index (commonly known as PyPI). It is the most common way to install Python packages. E.g.

    pip install mpi4py

The package can now be imported in Python scripts. You may need to run as sudo if you have root privileges, or append  `--user`  to install under your home directory (often this will be under $HOME/.local).

Note: pip3 is used to install Python3 packages, however in some environments the command pip may point to pip3, just as Python may point to Python3. You can use `which pip` to check this. For this document, examples will show the command simply as pip. 


**Tip**: To download a specific version of a package:

    pip install mpi4py=2.0.0


**Tip**: To find out what versions are available:

    pip install mpi4py==

This is essentially trying to install a version that does not exist and causes pip to list available versions.

### Anaconda

Anaconda is a Conda package distribution that includes many Python packages and extensions. It ships with Conda (A package and virtual environment manager).

Conda has a [getting started tutorial](https://conda.io/docs/user-guide/getting-started.html)

This series also has a [Conda for HPC](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python.conda.html) introduction.


## Virtual Environments

Virtual environments are extremely useful in Python for enabling reproducibility and maintaining multiple sets of packages/dependencies. The Conda package manager (provided with Anaconda and Miniconda) comes with a robust virtual environment system. 

Virtualenv is a popular alternative for those not using Conda.


## Alternative distributions

* [Intel Python](https://software.intel.com/en-us/distribution-for-Python) - managed and used via Conda
* [Enthought Canopy](https://www.enthought.com/product/enthought-Python-distribution)

[Example](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python.conda.html#examples) of Intel Python usage in Conda.

    
## Links

* [More detailed introduction](https://github.com/wscullin/ecp_Python_tutorial/blob/master/slides/ECP_Python_Tutorial_2018.pdf)


## References

Python for High Performance Computing (Exascale Computing Project 2nd Annual Meeting) [Slides](https://github.com/wscullin/ecp_Python_tutorial/blob/master/slides/ECP_Python_Tutorial_2018.pdf)
William Scullin (ALCF), Matt Belhorn (OLCF), Rollin Thomas (NERSC)

## Feedback

Any feedback/corrections are welcome: shudson@anl.gov

<br>

Back to [main page](https://betterscientificsoftware.github.io/python-for-hpc)



<!--Template to fill in from how-to example-->
<!---
Publish: yes
Categories: development
Topics: development, deployment
Tags: bssw-article
Level: 2???
Prerequisites: default
Aggregate: none???
--->
