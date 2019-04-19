---
author: Stephen Hudson
layout: single
permalink: /tutorials/python-doc-sphinx/
title: "Documentation with Sphinx"
author_profile: true
sidebar:
  nav: "content"
---

<!-- ## Documentation with Sphinx -->

<!-- ### Contributed by [Steve Hudson](https://github.com/shuds13) -->


1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Autodoc](#autodoc)
4. [Themes](#themes)
5. [Using NumPy or Google style docstrings](#using-numpy-or-google-style-docstrings)
6. [Upload to ReadtheDocs](#upload-to-readthedocs)
7. [Breathe: Combining with Doxygen](#breathe-combining-with-doxygen)
8. [Links](#links)
9. [Feedback](#feedback)


## Introduction

This article introduces documentation with Sphinx for Python projects and is intended as a quick getting started document.

Sphinx is a documentation generator based on interpretation of reStructuredText (abbr. rst or reST). It is used extensively for Python projects.

## Setup

The following gives a very basic setup to get started as quick as possible.

First Install and set up Sphinx: 
    
     pip install Sphinx
     
Now in your python project create a docs/ directory at the top level of your package. Inside the docs/ directory run:

     sphinx-quickstart

For basic setup, most questions can take defaults (shown in square brackets) - just press enter. 

Below is an example set of answers for project `myproj`. 

Note: The first question takes default as we're running in docs/ directory:
Note: Make sure to say yes to the autodoc question if you want to auto-generate an API from docstrings. Highly recommended!

> Root path for the documentation [.]:  
> Separate source and build directories (y/n) [n]:  
> Name prefix for templates and static dir [_]:  
> Project name: `myproj`  
> Author name(s): `Steve Hudson`  
> Project version []: `0.1.0`  
> Project release [0.1.0]:  
> Project language [en]:  
> Source file suffix [.rst]:  
> Name of your master document (without suffix) [index]:  
> Do you want to use the epub builder (y/n) [n]:  
> autodoc: automatically insert docstrings from modules (y/n) [n]: `y`  
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:  
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:  
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:  
> coverage: checks for documentation coverage (y/n) [n]:  
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:  
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:  
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:  
> viewcode: include links to the source code of documented Python objects (y/n) [n]:  
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:  
> Create Makefile? (y/n) [y]:  
> Create Windows command file? (y/n) [y]: `n`  

In this case only project name, author name, version, autodoc and Windows command file are non-default.

For following files are created:

```bash
_templates/
_static/
_build/
index.rst
conf.py
Makefile
```

index.rst is the base file containing your toctree (table of contents tree).

conf.py is the configuration file for your project.

You now have a template for your documentation. To build:

    make html
    
And then open in a browser. E.g:

    firefox _build/html/index.html

    
Create a file called readme.rst in the docs directory. This will simply contain a pointer to your project readme file eg:

    .. include:: ../README.rst
    
In index.html list this file without the extension. The toctree in index.rst looks like this:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
```

Note that indentation is important in rst.

Now your readme should appear in the documentation.

Note: Before you rebuild always make clean.

    make clean; make html
    firefox _build/html/index.html    

Further Instructions at [First Steps with Sphinx](http://www.sphinx-doc.org/en/stable/tutorial.html)

Alternative [installation instructions](http://www.sphinx-doc.org/en/stable/install.html)


## Autodoc

The pyexample project can be found on github [here](https://github.com/shuds13/pyexample)

Say you have the following directory structure.

<pre>
pyexample
├── docs
│   ├── _build
│   ├── conf.py
│   ├── index.rst
│   ├── Makefile
│   ├── readme.rst
│   ├── _static
│   └── _templates
├── LICENSE
├── pyexample
│   ├── __init__.py
│   ├── module_mpi4py_1.py
│   ├── module_numpy_1.py
│   └── module_numpy_2.py
├── README.rst
└── setup.py
</pre>

To use autodoc to extract the docstrings from module_mpi4py_1.py you can do the following.

In docs directory create a file mpi4py_module.rst that contains:

```rst
mpi4py Test Module
==================
.. automodule:: module_mpi4py_1
  :members:
```

Now add this file (without extension) to the index.rst

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   mpi4py_module
```

One more requirement is that autddoc can import the module. This can be achieved by giving the relative path in conf.py by adding these lines. Note the first three may already be there commented out.

```rst
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append('../pyexample')
```

Now rebuild, and the documentation should contain a link to the autogenerated documentation from doc strings.

Note: If you want to show the function signature lines for functions without docstring add `:undoc-members:` E.g: In mpi4py_module.rst add:

```rst
mpi4py Test Module
==================
.. automodule:: module_mpi4py_1
  :members:
  :undoc-members:  
```

This can now be repeated for other modules.

To nest sets of modules under the index title see the [libEnsemble example](https://github.com/Libensemble/libensemble/blob/master/docs/examples_modules.rst). And see the front end on [ReadtheDocs](https://libensemble.readthedocs.io)

## Themes

At time of writing the most popular theme is the Readthedocs theme. To change the theme, find the `html_theme` line in conf.py and change. E.g.

    html_theme = 'sphinx_rtd_theme'

<!-- Did I have to download something to get this??? -->
You may need to install:

    pip install sphinx_rtd_theme


## Using NumPy or Google style docstrings

To use the NumPy or Google stype docstrings add the napolean extension to the extension list E.g:

    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

For mmore info see [Support for NumPy and Google style docstrings](http://www.sphinx-doc.org/en/stable/ext/napoleon.html)


## Upload to ReadTheDocs

<!-- review from here -->>
Upload your docs directory to your online repository (e.g. github). Then create an account, if necessary, on ReadtheDocs and import the repo.

See instructions on [ReadTheDocs](http://docs.readthedocs.io/en/latest/getting_started.html)

Note: If you are using autodoc, ReadtheDocs will need to be able to import your code. This may not be possible if you are using C extensions, and this requires you mock these extensions in your conf.py. This will manifest as import errors in the readthedocs build log.

Example of mocking functions in conf.py:

```rst
from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()

MOCK_MODULES = ['argparse', 'numpy', 'mpi4py' , 'scipy',  'petsc4py', 'PETSc']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
```
    
More info at [ReadtheDocs FAQ](http://docs.readthedocs.io/en/latest/faq.html) 

## Breathe: Combining with Doxygen    
    
If you have Doxygen instrumented code which you wish to incorporate into a Sphinx document, you can use the [Breathe package](https://breathe.readthedocs.io). 

    pip install breathe

Breathe must be able locate the Doxygen produced XML.

<!-- double check -->

E.g: In conf.py modify/add lines of the format:

    extensions = ['sphinx.ext.autodoc', 'breathe']
    breathe_projects = { "myproject": "../code/src/xml/" }

where ../code/src/xml contains the doxygen XML output.

Create a file in docs/ E.g. `doxygen_files.rst` containing:

```rst
Doxygen Files
=============
.. autodoxygenindex::

```
Then add doxygen_files to your toctree in index.


## Links

More info at official [webpage](http://www.sphinx-doc.org)


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

