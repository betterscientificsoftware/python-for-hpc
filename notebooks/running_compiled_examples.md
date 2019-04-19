---
layout: single
permalink: /notebooks/running-compiled-examples/
title: "Python for HPC"
author_profile: false
sidebar:
  nav: "content"
---

## Scientific Notebook Example

The kernel in this example iterates over 1000 point charges, computing and summing the electrostatic forces between points. It has implementations in pure Python, NumPy, Cython (3 versions) and Numba (inc GPU version) with timings. For Cython, the compiled code generated is also shown.

### Instructions:

First make sure jupyter is installed. E.g.

    conda install jupyter # For conda
    pip3 install jupyter  # with pip
    
You may need to install other packages as required.

Now run the notebook:

    jupyter notebook Compiled_Examples.ipynb

or

    jupyter notebook

and select file from list.

The notebook will be rendered with the original output (run on 4-core Broadwell  i7-5600U CPU @ 2.60GHz).

To run on your system, make a copy. In the notebook, from menu bar:

    File -> Make a Copy...

Optional: You may want to clear the output here, from menu bar:

    Kernel -> Restart and Clear Output
    
Then you can select Run from the command buttons or press ctrl-Enter in each cell to execute the cell. If the cell identifier (In [ ]) turns to an asterisk, it is processing or waiting for a previous cell to process. If it becomes a number it has processed, showing the order of cell execution.

Now you can run through and create results/timings/graphs for your system.
 
This Notebook includes cells to run the kernel with:

 - pure python
 - numpy
 - cython unmodified (will use CPython calls ~same speed as Python)
 - cython with numpy and type definitions
 - cython in parallel* (threaded) with numnpy and type definitions
 - Numba (unmodified pure python)
 - Numba in parallel (threaded)
 - Numba on GPU (Need to uncomment - req. CUDA capable GPU)
 - Finally a cell that runs all for varous data sizes and tabulates

numexpr:
There is also an array expression example comparing numpy, numba and numexpr.

*Note that the Cython parallel runs, which should be creating threads, did not work on the system for which results are shown - it just ran serial. This is still included.


## Notes

Note on performance: Numba uses the llvm compiler, while the compiled components in other examples (numpy/cython) will be using the default gnu compilers in the provided results.

Note on timing: The timeit output will give a time per loop - a loop here refers to one run of the function (not the inner loop!). With small functions, timeit will do multiple iterations of the function to reduce the impact of timing overhead. It will also repeat the timing run several times and take a mean and standard deviation. These can be controlled with arguments if required.

Note on installing packages while using Notebook: If you find you need to install a package, install as usual and then restart the kernel in the Jupyter Notebook. From menu bar:

    Kernel -> Restart

