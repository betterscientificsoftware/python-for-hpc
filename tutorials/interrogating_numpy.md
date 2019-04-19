---
author: Stephen Hudson
layout: single
permalink: /tutorials/interrogating-numpy/
title: "Obtaining Numpy Configuration"
author_profile: true
sidebar:
  nav: "content"
---

<!-- # Obtaining NumPy build configuration. -->

<!-- ### Contributed by [Steve Hudson](https://github.com/shuds13) -->

NumPy is based on compiled C extensions and in turn is built upon BLAS/LAPACK libraries. The following gives some information on how to interrogate the build configuration and dependent libraries upon which NumPy is built.

Get basic configuration including BLAS/LAPACK libraries:

    import numpy
    numpy.__config__.show()
  
Note that configuration information may not be reliable in all circumstances. Dependencies of built libraries can also be checked by using the ldd command on NumPy shared libraries. E.g.

    ldd /<path_to_site-packages>/numpy/core/multiarray.so

Libraries may have variations in name based on platform (e.g. multiarray.cpython-36m-x86_64-linux-gnu.so). To check the site packages directory location you can do:

    $ python
    Python 3.6.3 |Intel Corporation| (default, Oct 16 2017, 15:28:36) ....
    >>> import numpy
    >>> numpy.__path__
    ['/home/shudson/miniconda3/lib/python3.6/site-packages/numpy']
    
    
To get full NumPy configuration details including compiler options/environment:

    import numpy.distutils
    np_config_vars = numpy.distutils.unixccompiler.sysconfig.get_config_vars()
    
    import pprint
    pprint.pprint(np_config_vars)

Or to write output to a file

    f = open('np_config_pprint.log','w')
    pprint.pprint(np_config_vars,f)
    
    
To get specific variables you can specify them as arguments E.g:
    
    import numpy.distutils
    c_cpp_compiler = numpy.distutils.unixccompiler.sysconfig.get_config_vars('CC', 'CXX')
    compile_vars = numpy.distutils.unixccompiler.sysconfig.get_config_vars('CFLAGS', 'LDSHARED')
    print(c_cpp_compiler)   
    print(compile_vars)
    
If NumPy has been installed without modification it will likely inherit the configuration from Python. You can check that with distutils.

    from distutils import sysconfig
    sysconfig.get_config_vars()

## References

Python for High Performance Computing (Exascale Computing Project 2nd Annual Meeting) [Slides](https://github.com/wscullin/ecp_python_tutorial/blob/master/slides/ECP_Python_Tutorial_2018.pdf)
William Scullin (ALCF), Matt Belhorn (OLCF), Rollin Thomas (NERSC)

stackoverflow: [find-out-if-which-blas-library-is-used-by-numpy](https://stackoverflow.com/questions/37184618/find-out-if-which-blas-library-is-used-by-numpy)

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
