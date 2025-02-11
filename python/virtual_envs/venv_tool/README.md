# venv

This is used to create virtual environments

<https://docs.python.org/3/library/venv.html>

## Create a new virtual environment

```bash
python -m venv venv
# or if you prefer (the name doesn't matter)
python -m venv .venv
```

## Activate an existing virtual environment

this depends on the OS and shell you are using

On Windows

- on Git Bash,

```bash
source venv/Scripts/activate
```

On Linux

- on bash,

```bash
source venv/bin/activate
```

## resources

- <https://fastapi.tiangolo.com/virtual-environments/>
