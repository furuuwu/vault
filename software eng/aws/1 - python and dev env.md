# 1 - A Primer on Python and the Development Environment

it also included an introduction to python, see `1 - python.ipynb`

## Git

* a distributed version control system (VCS) designed to track changes in source code and manage a code base
* any changes you make can be tracked, committed, and pushed up
to your online storage location (eg. GitHub)
* your GitHub repositories serve as a portfolio to showcase your code projects publicly (or keep them private, if you prefer)
* GitHub also allows others to contribute to your code base. Git version control enables collaboration without the fear of losing or overwriting changes since multiple developers can work on different branches, and changes can be reviewed and merged through pull requests.
* GitHub can be integrated with various services, such as project management tools and various CI/CD tools, and allows automated testing and deployment of your code.

## Jupyter Notebook

* <https://jupyter.org/install>

As it says there, you can install just some of the components

* JupyterLab

```shell
# Install JupyterLab with pip
pip install jupyterlab

# Once installed, launch JupyterLab with
jupyter lab
```

* Jupyter Notebook

```shell
# Install the classic Jupyter Notebook with
pip install notebook

# To run the notebook
jupyter notebook
```

Another option is to install the [Jupyter metapackage](https://pypi.org/project/jupyter/)

```shell
pip install jupyter 
```

this bundles in a single package:

* `notebook` - Jupyter Notebook
* `jupyterlab` - JupyterLab (added to metapackage v1.1)
* `ipython` - IPython (terminal)
* `ipykernel` - IPython Kernel for Jupyter
* `jupyter-console` - terminal Jupyter client
* `nbconvert` - convert notebooks between formats
* `ipywidgets` - interactive widgets package for IPython

## Documenting environment dependencies with `requirements.txt`

By freezing the application to specific versions of dependencies, it
ensures that, given the correct requirements, your project will maintain its original state.

```none
# ex: requirements.txt
pip==3.9
python==3.9.4
pandas==1.4.2
requests==2.28.0
```

```shell
# install dependencies using the requirements.txt file
pip install -r requirements.txt
```

you can update and store the new package imports and versions to keep the requirements.txt file up to date

```shell
# collect dependencies in the requirements.txt file
pip freeze >> requirements.txt
```

## (optional) Utilizing module management systems

MMSs are like special folders that only work in certain environments. They do this by changing `sys.prefix` and `sys.exec_prefix` so that they point to the base directory of the virtual environment.
This is helpful because it lets developers create "clean" applications and also makes sure that all the different parts of the project work well together.

There are many different module management systems to choose from, but `Anaconda` is the most popular. However, it doesn't always have the most up-to-date packages for data engineers, and `pip`, the regular package manager for Python, doesn’t work well with Anaconda. That’s why we’re using `pipenv` in this book. It's a virtual environment and package management system that uses `Pipfile` and `Pipfile.lock`, similar to a requirements.txt file.

```shell
# create the environment and activate it
pipenv shell

# install dependencies
pipenv install <package>
pipenv install # what's already there
```

⚠️**See the pipenv folder for more instructions (or don't use it)**⚠️
