---
author: Stephen Hudson
author_profile: true
title: "Static analysis and style checking in Python packages"
date: 2019-04-18
tags: [linting, static analysis, PEP 8, style, errors]
excerpt: "Flake8 for static analysis and style checking in Python"
sidebar:
  nav: "content"
---


This blog is based on our development experience with an ECP software technology code written in Python. It includes the authors opinions and should not be taken as dictum. Please provide counter opinions in the comments.

After reviewing several options for linting Python code, we converged on [Flake8](http://flake8.pycqa.org/en/latest){:target="_blank"} as an easy-to-use syntax and style checker. Flake8 is the merger of two static analysis tools: [pycodestyle](https://github.com/PyCQA/pycodestyle){:target="_blank"} (formerly called pep8) which checks code for PEP 8 style compliance and [pyflakes](https://github.com/PyCQA/pyflakes){:target="_blank"} which checks for syntactical errors.

**Note:** PEP 8 (Python Enhancement Proposal 8) provides the official coding conventions (also known as a "style guide") for Python.
{: .notice--warning}

Once imported (`pip install flake8`), the tester can simply type `flake8` in the top-level directory and Flake8 checks through the entire package. A Flake8 check can be added to test scripts and run with all tested versions of Python. A `.flake8` configuration file can be added to the top directory, which decides which rules to ignore, which files to exclude, and also allows the user to specify rules to ignore in specific files.

[Using flake8 in our .travis.yml](https://github.com/Libensemble/libensemble/blob/master/.travis.yml){:target="_blank"}

[Our .flake8 configuration file](https://github.com/Libensemble/libensemble/blob/master/.flake8){:target="_blank"}

Note that Flake8 is also provided as a `pytest` plugin (`pytest-flake8`).


Example of syntax and style analysis
------------------------------------

Taking the following Python code in the file `badcode.py`. It can be seen that `flake8` combines the style analysis of `pycodestyle` with the syntax analysis of `pyflakes`.

```python
import time
logger=logging.getLogger(__name__)

try:
    print('hi')
except:
    print('oh no')
```

    $ pycodestyle badcode.py 
    badcode.py:2:7: E225 missing whitespace around operator
    badcode.py:6:1: E722 do not use bare 'except'
    
    $ pyflakes badcode.py 
    badcode.py:1: 'time' imported but unused
    badcode.py:2: undefined name 'logging'
    
    $ flake8 badcode.py
    badcode.py:1:1: F401 'time' imported but unused
    badcode.py:2:7: E225 missing whitespace around operator
    badcode.py:2:8: F821 undefined name 'logging'
    badcode.py:6:1: E722 do not use bare 'except'


Motivation
----------

Why do we use static syntax checking:

 - It is important to check the whole source for errors that may not be caught in tests. This is especially important as Python is not pre-compiled. Flake8 examines the syntax of each file separately, making it fast, but possibly not as thorough as linting tools that perform inter-file analysis (such as [Pylint](https://www.pylint.org/){:target="_blank"})

 - It is a quick way to catch unnecessary imports, unused variables, and other inefficiencies that do not make code fail. 
 
 - It is good for portability. Some Python implementations may allow errors others do not. 


Why do we use style checking:

 - Firstly style standards are intended to improve readability of code. Code is read more often than it is written, and it is often noted that reading code is harder than writing it. If all developers follow the same conventions this maximizes clarity, and ultimately reduces the time making style decisions.

 - To aid provenance of code. If everyone submits PEP 8 compliant code, then many lines will not be misattributed due to a style clean-up, including white space removal. Such clean-up efforts also often touch the same lines of code other developers are working on creating unnecessary conflicts when merging.
 
 - It is better to have compliance with agreed exceptions than not at all. On our project, we allow exceptions to a few of the PEP 8 rules, including line length and space between operators, as there are occasions where we do not want to enforce these.
 
 - In some cases, this style enforcement may help to find bugs in code. For example, not allowing *bare exceptions* (when an except clause does not include an Exception type) is not a syntactical error, but is a common semantic mistake that can result in the code continuing past errors that should have raised an exception. [Some more examples](https://www.python.org/dev/peps/pep-0008/#programming-recommendations){:target="_blank"}.
 
 
Automatic formatters
--------------------

Formatters can be used to save the burden of manually correcting format issues. Some of these may make style choices that go beyond the requirements in order to produce consistent code style. We tried the popular open-source Python formatter [YAPF](https://github.com/google/yapf){:target="_blank"} (Yet Another Python Formatter) and mostly liked the result. However, we found some cases where this resulted in unfavorable style decisions such as peculiar line-splitting. A style file can be used to control such decision making, but controlling it with the finesse you desire can be time-consuming and we have not yet adopted this approach.

It is also worth noting that auto-formatters have to be cautious, so as not to change the semantics of the code, and so may not guarantee PEP 8 compliant code without some manual intervention. 

Popular Python formatters:

* [YAPF](https://github.com/google/yapf){:target="_blank"} (Yet Another Python Formatter) [Try online](https://yapf.now.sh/){:target="_blank"}
* [Black](https://black.readthedocs.io){:target="_blank"} Uncompromising formatter than forgoes configurability for optimal code consistency (Any color you like as long as it's Black!).


Example of YAPF
---------------

What happens if we run our `badcode.py` example, from above, through YAPF (with no configuration).

    $ yapf badcode.py > goodcode.py

The following code is produced.

```python
import time
logger = logging.getLogger(__name__)

try:
    print('hi')
except:
    print('oh no')
```

    $ flake8 goodcode.py
    goodcode.py:1:1: F401 'time' imported but unused
    goodcode.py:2:10: F821 undefined name 'logging'
    goodcode.py:6:1: E722 do not use bare 'except'
    
The whitespace issues have been fixed. The syntax problems remain (unused imports). Also note that the bare
exception remains. Although counted as a style issue, the formatter lacks the information to fix it.


Summary
-------

Linting code is a simple and worthwhile addition to testing that helps achieve consistency across code-bases and can reduce errors. Automatic formatters may be used to achieve yet more consistency and time-saving, though possibly with an initial out-lay of effort on configuration or ceding complete control of decision making to the formatter.
