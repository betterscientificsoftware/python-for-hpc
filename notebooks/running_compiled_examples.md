---
layout: single
permalink: /notebooks/running-compiled-examples/
title: "Scientific Notebook Example"
author_profile: false
comments: true
sidebar:
  nav: "content"
---

<!-- ## Scientific Notebook Example -->

The kernel in this example iterates over 1000 point charges, computing and summing the electrostatic forces between points. It has implementations in pure Python, NumPy, Cython (3 versions) and Numba (inc GPU version) with timings. For Cython, the compiled code generated is also shown.

### Get the Notebook:

Click on the Notebook link and select `Save File` to save to your system.

The file will be called `Compiled_Examples.ipynb`


### Instructions for Running:

First make sure jupyter is installed. E.g.

    conda install jupyter # For conda
    pip3 install jupyter  # with pip
    
You may need to install other packages as required when you run, including:

* numpy
* cython
* numba
* matplotlib
* pandas
* seaborn

Now run the notebook:

    jupyter notebook Compiled_Examples.ipynb

Optional: To clear any existing output, from menu bar:

    Kernel -> Restart and Clear Output
    
Then you can select `Run` from the command buttons or press `ctrl-Enter` in each cell to execute the cell. If the cell identifier (In [ ]) turns to an asterisk, it is processing or waiting for a previous cell to process. If it becomes a number it has processed, showing the order of cell execution.

<details>
  <summary>Having trouble with missing modules?</summary>

    Note on installing packages while using Notebook: If you find you need to install a package, install as usual and then restart the kernel in the Jupyter Notebook. From menu bar:

        Kernel -> Restart
        
</details>

<br>

Now you can run through and create results/timings/graphs for your system.
 
This Notebook includes cells to run the kernel with:

 - pure python
 - numpy
 - cython unmodified (will use CPython calls ~same speed as Python)
 - cython with numpy and type definitions
 - cython in parallel (threaded) with numnpy and type definitions
 - Numba (unmodified pure python)
 - Numba in parallel (threaded)
 - Numba on GPU (Need to uncomment - req. CUDA capable GPU)
 - Finally a cell that runs all for varous data sizes and tabulates


### Notes:

Note on performance: Numba uses the llvm compiler, while the compiled components in other examples (numpy/cython) will be using the default compilers for your system (GNU compilers in the provided results).

Note on timing: The `timeit` output will give a time per loop - a loop here refers to one run of the function (not the inner loop!). With small functions, timeit will do multiple iterations of the function to reduce the impact of timing overhead. It will also repeat the timing run several times and take a mean and standard deviation. These can be controlled with arguments if required.
