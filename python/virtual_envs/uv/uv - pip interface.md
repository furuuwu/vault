# uv - The pip interface

## The pip interface

Manually managing environments and packages — intended to be used in legacy workflows or cases where the high-level commands do not provide enough control.

<https://docs.astral.sh/uv/pip/>

* Creating virtual environments (replacing venv and virtualenv):

```shell
# create a virtual environment in a directory called .venv
uv venv

# create a virtual environment in a directory called my_venv
uv venv my_venv

# create a virtual environment with a specific Python version
uv venv --python 3.12.0
```

* Managing packages in an environment (replacing pip and pipdeptree):

```shell
# Install packages into the current environment
uv pip install flask

# Install a package with optional dependencies enabled, e.g., Flask with the "dotenv" extra
uv pip install "flask[dotenv]"

# Install a package with a constraint, e.g., Ruff v0.2.0 or newer
uv pip install 'ruff>=0.2.0'
uv pip install 'ruff==0.3.0'

# Install a package from GitHub
uv pip install "git+https://github.com/astral-sh/ruff"

# Install a package from the disk
uv pip install "ruff @ ./projects/ruff"

# Installing packages from files
uv pip install -r requirements.txt
uv pip install -r pyproject.toml
uv pip install -r pyproject.toml --extra foo

# Uninstall packages
uv pip uninstall matplotlib

"""
uv pip tree: View the dependency tree for the environment.
"""
```

* Inspecting environments

```shell
# To list all of the packages in the environment
uv pip list

# To list all of the packages in the environment in a requirements.txt format
uv pip freeze

# Inspecting an installed package
uv pip show matplotlib

# To check for conflicts or missing dependencies in the environment
uv pip check
```

* Declaring dependencies

<https://docs.astral.sh/uv/pip/dependencies/>

It is best practice to declare dependencies in a static file instead of modifying environments with ad-hoc installations. Once dependencies are defined, they can be locked to create a consistent, reproducible environment.

Using `pyproject.toml` - The pyproject.toml file is the Python standard for defining configuration for a project.

To define project dependencies in a pyproject.toml file:

```toml
[project]
dependencies = [
  "httpx",
  "ruff>=0.3.0"
]
```

To define optional dependencies in a pyproject.toml file:

```toml
[project.optional-dependencies]
cli = [
  "rich",
  "click",
]
```

Each of the keys defines an "extra", which can be installed using the `--extra` and `--all-extras` flags or `package[<extra>]` syntax. See the documentation on installing packages for more details.

<https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>

Using `requirements.in` - It is also common to use a lightweight requirements.txt format to declare the dependencies for the project. Each requirement is defined on its own line. Commonly, this file is called requirements.in to distinguish it from requirements.txt which is used for the locked dependencies.

To define dependencies in a requirements.in file

```text
# requirements.in
httpx
ruff>=0.3.0
```

Optional dependencies groups are not supported in this format.

* Locking packages in an environment (replacing pip-tools):

<https://docs.astral.sh/uv/pip/compile/>

Locking is to take a dependency, e.g., ruff, and write an exact version to use to a file. When working with many dependencies, it is useful to lock the exact versions so the environment can be reproduced. Without locking, the versions of dependencies could change over time, when using a different tool, or across platforms.

```shell
"""
uv pip compile: Compile requirements into a lockfile.
uv pip sync: Sync an environment with a lockfile.
"""

# To lock dependencies declared in a pyproject.toml
uv pip compile pyproject.toml -o requirements.txt

# To lock dependencies declared in a requirements.in
uv pip compile requirements.in -o requirements.txt

# uv also supports legacy setup.py and setup.cfg formats. To lock dependencies declared in a setup.py
uv pip compile setup.py -o requirements.txt

# To sync an environment with a lockfile
uv pip sync requirements.txt
uv pip sync pyproject.toml
```
