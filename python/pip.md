# pip

## Install packages listed on requirements.txt

```bash
pip install -r requirements.txt
```

## Uninstall all packages

```bash
pip freeze | xargs pip uninstall -y
```

or, step by step

```bash
# Generate a list of installed packages
pip freeze > requirements.txt
# Uninstall all packages
pip uninstall -r requirements.txt -y
```

or, if they are in a virtualenv, just delete the virtualenv (it's usually much faster)
