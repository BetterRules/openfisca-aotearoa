## Setup Aotearoa OpenFisca in pew

Follow this installation if you wish to:
  - run calculations on a large population;
  - run your own instance of openfisca-aotearoa, but not modify the rules

## Step 1: Install Python 3

This package requires [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) .

Supported platforms:
- GNU/Linux distributions (in particular Debian and Ubuntu);
- Mac OS X;
- Microsoft Windows (we recommend using [ConEmu](https://conemu.github.io/) instead of the default console).

Other OS should work if they can execute Python and NumPy.

## Step 2: Setup Pew

### Setting-up a Virtual Environment with Pew

Create a [virtual environment](https://virtualenv.pypa.io/en/stable/) (abbreviated as "virtualenv") with a using [pew](https://github.com/berdario/pew).

- A [virtualenv](https://virtualenv.pypa.io/en/stable/) is a project specific environment >created to suit the needs of the project you are working on.
- A virtualenv manager, such as [pew](https://github.com/berdario/pew), lets you easily create, remove and toggle between several virtualenvs.

To install pew, launch a terminal on your computer and follow these instructions:

```sh
 python --version # You should have python 3.7 or better installed on your computer.
 # If not, visit http://www.python.org to install it and install pip as well.
```

```sh
pip install --upgrade pip
pip install pew  # if asked, answer "Y" to the question about modifying your shell config file.
```

To set-up and create a new a virtualenv named **openfisca** running python3.7:

```sh
pew new openfisca --python=python3.7
```

The virtualenv you just created will be automatically activated. This means you will operate in the virtualenv immediately. You should see a prompt resembling this:

```sh
Installing setuptools, pip, wheel...done.
Launching subshell in virtual environment. Type 'exit' or 'Ctrl+D' to return.
```

Additional information:
- Exit the virtualenv with `exit` (or Ctrl-D).
- Re-enter with `pew workon openfisca`.

:tada: You are now ready to install this OpenFisca Country Package!

#### Step 3: Install this Country Package with Pip Install

Inside your virtualenv, check the prerequisites:

```sh
python --version  # should print "Python 3.xx".
#if not, make sure you pass the python version as an argument when creating your virtualenv
```

```sh
pip --version  # should print at least 9.0.
#if not, run "pip install --upgrade pip"
```

Install the Country Package:


```sh
pip install openfisca_aotearoa
```

:tada: This OpenFisca Country Package is now installed and ready!

