=====================================
 Getting Started with Python and Git
=====================================

This is a quick assignment to help you become familiar with git and with how
Python assignments will work. If this is your first time using git or GitHub,
you may find [GitHub's "Hello World"
Guide](https://guides.github.com/activities/hello-world/) useful.

To complete the assignment you will need to:

- Fork this repository to your own account
- Edit the file ``getting_started.py`` using a text editor and complete the program so it runs.
- "Push" your revised ``getting_started.py`` to your repository.

Test your implementation using ``python getting_started.py``.

Using Python on the Linux cluster (strongly recommended)
========================================================

You are strongly encouraged to use the SOIC Linux clusters to complete this
assignment. All the computers have Python 3 installed.

You can connect to one of the computers via SSH. The following command should work on Linux and macOS. On Windows you will need to download an SSH client such as PuTTY.

```bash
ssh username@burrow.soic.indiana.edu
```

(If you are not a graduate student in SOIC this will likely not work. Tell the instructor.)

Once connected you can type ``python3`` to use the Python REPL. You can run
Python code stored in a file (e.g., ``my_program.py``) in your current
directory with ``python3 my_program.py``.

The vanilla Python REPL is not the most enjoyable environment. You may install
an enhanced version of the Python REPL with the following:

```bash
python3 -m pip install IPython
```

to use IPython:

```bash
python3 -m IPython
```

There is also a browser-based Python REPL called, [Jupyter](http://jupyter.org/). You can
install this with

```bash
python3 -m pip install jupyter
```

and lauch the jupyter notebook with

```bash
python3 -m jupyter notebook
```

Due to prudent SOIC firewalls, accessing the jupyter notebook using your web
browser will only work smoothly if you are physically at a computer in the
cluster in Lindley Hall. To use the notebook remotely you need to use VNC.

To get a taste of what the Jupyter notebook is like, you may visit
[http://jupyter.org/](http://try.jupyter.org/).

Using Python on your computer
=============================

You may also install the Anaconda distribution of Python, which is a package
which comes with most of the functionality etc. which you will need for the
course. Direct your browser to https://www.continuum.io/downloads and download
the graphical installer (on macOS and Windows). Double-click the downloaded
file and install the Python distribution system-wide. Make sure that you
download Python 3.5.
