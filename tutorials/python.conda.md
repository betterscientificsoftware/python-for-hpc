---
author: Stephen Hudson
layout: single
permalink: /tutorials/python-conda/
title: "Conda and Anaconda"
author_profile: true
sidebar:
  nav: "content"
---

<!-- # Conda and Anaconda -->

<!-- ### Contributed by [Steve Hudson](https://github.com/shuds13) -->

## What is Conda/Anaconda/Miniconda

The Conda products form a free cross-platform package management system created by Continuum Analytics, and consists of the following components.

 - Conda is an open-source package manager and virtual environment manager for installing packages from Conda compatible distributions.

 - Anaconda is a Conda package distribution that includes many python packages and extensions. It ships with Conda.

 - Miniconda includes a much smaller set of core packages along with Conda. 


Miniconda still has access to the Anaconda repository on-line, and other repositories of Conda packages including the community driven conda-forge, and these can easily be installed at the command line. Intel also provides high performance variants of many packages accessible through Conda. This includes the NumPy and SciPy packages built upon MKL.

While Conda packages are a binary distribution allowing very fast installation, other forms of installation are supported inside Conda environments, including pip. Any source installation can also be performed inside the Conda virtual environment. Each package installs along with a list of dependent packages by default.

Conda environments are an alternative to other python virtual environment managers such as virtualenv. Virtual environments are extremely useful in python for enabling reproducibility and maintaining multiple sets of packages/dependencies. Unlike other virtual environments, Conda installs Python itself inside the environment, by default.

Ananconda is provided on many major computing platforms, generally requiring loading of an environment module or equivalent.

Miniconda is ideal for personal use on standalone systems and for using with on-line CI tools such as Travis. It's fast due to binary installation and usually quite simple (unless you have dependency issues – see below). The libEnsemble package has an [example of using Conda with Travis](https://github.com/Libensemble/libensemble/blob/master/.travis.yml)

Further resources:

Download [Anaconda](www.anaconda.com/download)

Download [Miniconda](https://conda.io/miniconda.html)

Conda has a [getting started tutorial](https://conda.io/docs/user-guide/getting-started.html)

A good discussion on the thinking behind Conda and some common misconceptions can be found [here](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions).



## Issues and Limitations

A downside of using a binary distribution is that it can be inflexible. The binaries are only built and configured for selected platforms and configurations. Furthermore, packages may come with incompatible dependencies (due to version locked packages or alternative API implementations). This may result in a dependency for one package being upgraded/downgraded when installing a later package. To some extent this can be managed by use of the `--no-deps` or `--no-update-deps` option on the Conda install command. Conda does not support virtual dependencies and packages may, for example, come with a given MPI implementation as a dependency. 

Lets say that you wish to install OpenMPI via:

    conda install openmpi

and you then try installing another MPI based package - you may find that package comes with MPICH as a dependency.

    conda install petsc
    
or

    conda install mpi4py

One answer to this is to try to install packages in one line as follows:

    conda install petsc mpi4py openmpi

If this does not work, then sometimes combining source distributions with Conda can be used to create customized builds, along with `--no-deps` flags.

When installing on a system with an existing MPI, such as a cluster, then it is highly recommended that mpi4py is installed on top of the system MPI. This can be done in the Conda environment using pip install as follows:

    env MPICC=$(which cc) pip install mpi4py

If working in a cross-compilation environment, ensure the correct compiler and MPI libraries are loaded.
    
## Combining with external dependencies

Python will locate installed packages according to sys.path which can be checked by:


    $ python
    Python 3.6.3 |Intel Corporation| (default, Oct 16 2017, 15:28:36) ....
    >>> import sys
    >>> sys.path
 
To ensure isolation from external packages on your system set the environment variable `export PYTHONNOUSERSITE=1` before activating the environment (similar to `--no-site-packages` in virtualenv). This should prevent paths for external python paths being included in the sys.path inside the Conda environment. Selected directories can also be added using the  PYTHONPATH environment variable as usual.


<!-- Cross compilation issues *** -->

## Cross compilation

Conda version 5 has added some features for compiler specification/cross-compilation. A good overview is given in the Conda documentation under [Compiler Tools](https://conda.io/docs/user-guide/tasks/build-packages/compiler-tools.html). Note that as the Conda distributions themselves are binary, the builds are still limited to those available. 

<!-- Add example of this -->


## Examples

The Intel Python libraries are popular for use in high performance environments. 

Using Intel python libraries:

    conda config --add channels intel

You can now access Python packages (Note: channels can also be added to a .condarc file)

To add the set of Intel core packages for latest version of python3 when creating a new environment myenv:

    conda create --name myenv intelpython3_core python=3

or to add Intel's full distribution (takes a while):

    conda create --name myenv intelpython3_full python=3

Intel Conda packages include NumPy and SciPy based on MKL. 

Note that the Intel compiler is not included in the Intel Conda packages. These packages will generally work with gcc and this may be worthwhile for picking up, for example, the MKL library. If an Intel compiler is not available on the system, the default gcc compiler will be used.


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
