# uv

<https://github.com/astral-sh/uv>

## installation

```shell
# with pip
pip install uv
```

## Python versions

<https://docs.astral.sh/uv/concepts/python-versions>

```shell
# Install the latest Python version
uv python install

# Install a specific version
uv python install 3.12

# Install multiple versions
uv python install 3.10 3.11 3.12

# Install an alternative Python implementation, e.g. PyPy
uv python install pypy@3.10

# Uninstalling a version
uv python uninstall 3.12
```

```shell
# List installed and available Python versions
uv python list
# By default, downloads for other platforms and old patch versions are hidden.

# To exclude downloads and only show installed Python versions
uv python list --only-installed

# Use a specific Python version in the current directory
uv python pin 3.11
```

## The pip interface

⚠️**Ideally, don't use this**⚠️

see `uv - pip interface.md`

## Scripts

Executing standalone Python scripts, e.g., example.py.

* `uv run`: Run a script.
* `uv add --script`: Add a dependency to a script
* `uv remove --script`: Remove a dependency from a script

A Python script is a file intended for standalone execution, e.g., with `python <script>.py`. Using uv to execute scripts ensures that script dependencies are managed without manually managing environments.

<https://docs.astral.sh/uv/guides/scripts/>

## Projects

Creating and working on Python projects, i.e., with a pyproject.toml.

* `uv init`: Create a new Python project.
* `uv add`: Add a dependency to the project.
* `uv remove`: Remove a dependency from the project.
* `uv sync`: Sync the project's dependencies with the environment.
* `uv lock`: Create a lockfile for the project's dependencies.
* `uv run`: Run a command in the project environment.
* `uv tree`: View the dependency tree for the project.
* `uv build`: Build the project into distribution archives.
* `uv publish`: Publish the project to a package index.

<https://docs.astral.sh/uv/guides/projects/>

## Tools

Running and installing tools published to Python package indexes, e.g., ruff or black.

* `uvx / uv tool run`: Run a tool in a temporary environment.
* `uv tool install`: Install a tool user-wide.
* `uv tool uninstall`: Uninstall a tool.
* `uv tool list`: List installed tools.
* `uv tool update-shell`: Update the shell to include tool executables.

<https://docs.astral.sh/uv/guides/tools/>

## resources

* [Matt Palmer - uv for everything](https://www.youtube.com/watch?v=zgSQr0d5EVg)
* [Timnology - UV](https://www.youtube.com/watch?v=ap2sWj5yDIY)
