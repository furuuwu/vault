# pipenv

## installing pipenv

* <https://pipenv.pypa.io/>

![a](img/2025-02-04-11-34-21.png)

```shell
pip install --user pipenv
```

This command instructs pip to install Pipenv in your user space. The `--user` option ensures that Pipenv is installed in the user install directory for your platform.

![a](img/2025-02-04-11-58-32.png)

![a](img/2025-02-04-15-46-31.png)

Add it to the PATH environment variable (of the User or of the System)

```shell
pipenv
# if you get `pipenv: command not found`...
# find pipenv's installation path
pip show pipenv
# look for the Location field—it shows where Pipenv is installed
```

## creating a virtual environment

```shell
pipenv shell
```

![a](img/2025-02-04-15-53-21.png)

## installing dependencies

Use `pipenv install <package>` and `pipenv uninstall <package>`

```shell
# eg.
pipenv install matplotlib
```

the generated `Pipfile` will look something like this:

```none
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
notebook = "*"
ipykernel = "*"
dask = {extras = ["complete"], version = "*"}

[dev-packages]

[requires]
python_version = "3.10"
```
