# pyenv

You can use this to manage multiple python versions

<https://github.com/pyenv/pyenv>

## Installation on Windows

The official pyenv does not support Windows

![a](img/2024-12-15-17-11-24.png)

So, use `pyenv for Windows`

<https://github.com/pyenv-win/pyenv-win>

Steps:

* Install pyenv-win in PowerShell

  ```powershell
  Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
  ```

* Reopen PowerShell
* Run `pyenv --version` to check if the installation was successful.

  ![a](img/2024-12-15-17-13-48.png)

The installation created a `~/.pyenv/` directory

![a](img/2024-12-15-17-17-35.png)

## Installation on Ubuntu

```bash
# remove the existing .pyenv directory
rm -rf /home/devcontainers/.pyenv

# run the automatic installer in Linux
curl https://pyenv.run | bash

# edit the shell's configuration file (~/.bashrc in this case)
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
# reload your shell
source ~/.bashrc

# verify it is working
pyenv --version
```

here's the prints and some trouble i run into (looking back, i could have used the existing pyenv)

![a](img/2024-12-16-10-59-25.png)

![a](img/2024-12-16-11-00-23.png)

![a](img/2024-12-16-11-01-41.png)

![a](img/2024-12-16-11-02-37.png)

## Updating and Uninstalling

To uninstall, remove that folder

```bash
rm -rf ~/.pyenv
```

To update (since we installed via the installer), run in a Powershell terminal

```powershell
&"${env:PYENV_HOME}\install-pyenv-win.ps1"
```

## Usage

* you use pyenv to manage (install and select) multiple Python versions

![a](img/2024-12-15-17-31-23.png)

* get a specific version of Python

  `pyenv install 3.10.0`

  it must be one of the versions listed in the command below

  `pyenv install --list`

  ![a](img/2024-12-15-17-34-07.png)

  ![a](img/2024-12-15-17-35-06.png)

  ![a](img/2024-12-15-17-38-57.png)

* list the versions that are installed and which one is active

  `pyenv versions`

  in the image below, i have two versions installed but none of them is active
  ![a](img/2024-12-15-17-41-14.png)

* you can set a python version in different ways: local, global and shell installations

  * globally means the entire system uses it unless there's a more specific (shell > local > global)

  eg.
  
  `pyenv shell 3.10.0` sets that version for current shell (resets after you kill it)

  `pyenv local 3.10.0` sets a version for the directory the command is run on

  `pyenv global 3.10.0` sets a global version

  in the image below, i set a local version for that folder

  ![a](img/2024-12-15-17-44-48.png)

on WSL, i got some trouble with using it (after the installation). I followed these steps

```bash
# install a C compiler and other dependencies to build Python
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# verify gcc installation
gcc --version

# and then it worked
pyenv install 3.10.0
pyenv global 3.10.0
python --version
```
