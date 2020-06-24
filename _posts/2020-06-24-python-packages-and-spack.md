---
author: Stephen Hudson
author_profile: true
title: "Installing Python packages with Spack"
date: 2020-06-24
tags: [spack, python, conda]
excerpt: "Working with Python packages with Spack and Conda on HPC systems."
sidebar:
  nav: "content"
---


## Obtaining Spack

To obtain the Spack distribution and start installing packages, see the [Spack getting started guide](https://spack.readthedocs.io/en/latest/getting_started.html)

An example of how to get spack and maintain a forked repository is [here](https://libensemble.readthedocs.io/en/master/dev_guide/release_management/release_platforms/rel_spack.html).


## Installing Python packages in Spack

All Python packages in Spack have the `py-` prefix. E.g. to install *py-libensemble*:

    spack install py-libensemble

While most packages in Spack locate dependencies using `RPATHS` embedded in the binaries, Python packages must be loaded into the `PYTHONPATH`. The complication is that every Python package in Spack has it's own Python *site-packages* sub-directory, instead of a combined *site-packages*.

When the `spack install` command is executed, modules are created for each package. To see your package directories do:

    spack find --paths

Having installed your package, you can recursively load your modules with one command. But first you must have Spack's shell commands enabled:

    . $SPACK_ROOT/share/spack/setup-env.sh

Now load the package modules:

    spack load -r py-libensemble

This will bring py-libensemble and all Python package dependencies into your `PYTHONPATH`. If you have more than one variant of the package, specify the abbreviated hash with a forward slash. E.g:

    spack load -r py-libensemble /j4zmggq

Any Python packages will be added to the PYTHONPATH, when the modules are loaded.

If you do not have an environment module system installed, you may need to install [lmod](https://lmod.readthedocs.io) (also available in Spack):

    spack install lmod
    . $(spack location -i lmod)/lmod/lmod/init/bash
    spack load lmod


**Note** An alternative to the recursive module load is to use [Spack views](https://spack.readthedocs.io/en/latest/workflows.html#filesystem-views).


## Using system installed Python

Many systems will have a Python module, which will supply a Python distribution, perhaps through a Conda environment.

I recommend specifying the module supplied Python within your `~/.spack/packages.yaml` file. Packages included with this Python distribution (e.g. Numpy) can also be supplied. This file is used to specify dependencies that Spack must obtain from the given system (rather than building from scratch).  E.g. to use the modules on [Theta](https://www.alcf.anl.gov/support-center/theta) the `packages.yaml` may include:

```yaml
packages:
  python:
    modules:
      python@3.6%intel@18.0.0.128 arch=cray-cnl6-mic_knl: intelpython36/2019.3.075
      buildable: False
  py-numpy:
    modules:
      py-numpy@1.16.1%intel@18.0.0.128 arch=cray-cnl6-mic_knl: intelpython36/2019.3.075
      buildable: False
```

**Hint**: Alternatively, you can access your Conda Python and built-in packages in your
`~/.spack/packages.yaml` while your Conda environment is activated, using ``CONDA_PREFIX``
For example, if you have an activated Conda environment with Python 3.7 and SciPy installed:

```yaml
packages:
    packages:
      python:
        paths:
          python: $CONDA_PREFIX
        buildable: False
      py-numpy:
        paths:
          py-numpy: $CONDA_PREFIX/lib/python3.7/site-packages/numpy
        buildable: False
      py-scipy:
        paths:
          py-scipy: $CONDA_PREFIX/lib/python3.7/site-packages/scipy
        buildable: False
```

It is also recommended to use `packages.yaml` to specify the MPI libraries for your system.
To see the concretized specification (and which packages are already installed):

    spack spec --install-status py-libensemble

Spack packages come with variants. Note that some packages have an MPI. In some cases, the serial version may require turning off sub-variants. For example to build a simple serial version of PETSc with petsc4py:

    spack install py-petsc4py~mpi ^petsc~mpi~hdf5~hypre~superlu-dist



