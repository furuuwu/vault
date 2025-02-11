# pyenv (GPT)

## ERROR - trouble installing pyenv on WSL

i'm trying to install pyenv in wsl (a ubuntu 22.04 lts i got from the windows store)

```shell
curl https://pyenv.run | bash
```

```text
output:
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   270  100   270    0     0    413      0 --:--:-- --:--:-- --:--:--   413

WARNING: Can not proceed with installation. Kindly remove the '/home/devcontainers/.pyenv' directory first.
```

The error indicates that the directory `/home/devcontainers/.pyenv` already exists, and the installation script won't proceed unless it is removed. Here's how you can resolve this issue:

### Steps to Fix

1. **Check if `.pyenv` already exists**:
   Run the following command to confirm:

   ```bash
   ls -la /home/devcontainers/.pyenv
   ```

   If it exists, it means a previous or incomplete installation of Pyenv is causing the conflict.

2. **Remove the existing `.pyenv` directory**:
   If you don’t need the existing installation or its data, you can remove the directory:

   ```bash
   rm -rf /home/devcontainers/.pyenv
   ```

3. **Retry the Pyenv installation**:
   After removing the directory, rerun the installation command:

   ```bash
   curl https://pyenv.run | bash
   ```

---

### If You Want to Preserve the Existing `.pyenv` Directory

If you want to keep the current installation (e.g., it has configurations or installed versions you need):

1. **Backup the directory**:

   ```bash
   mv /home/devcontainers/.pyenv /home/devcontainers/.pyenv_backup
   ```

2. Proceed with the installation.

---

### Ensure Proper Permissions

The `devcontainers` user may not have the correct permissions. To ensure proper permissions:

1. Run the installation as the `devcontainers` user:

   ```bash
   sudo -u devcontainers bash -c "curl https://pyenv.run | bash"
   ```

2. If you intend to install Pyenv system-wide or for another user, switch to the relevant user (e.g., `root` or your primary user) before running the command.

---

### Verify the Installation

After the installation completes, add the following to your shell's configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

Reload your shell:

```bash
source ~/.bashrc
```

Verify Pyenv is installed correctly:

```bash
pyenv --version
```

## ERROR - using pyenv install on WSL

```text
pyenv install 3.10.0
Downloading Python-3.10.0.tar.xz...
-> https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
Installing Python-3.10.0...
patching file aclocal.m4
patching file configure
Hunk #5 succeeded at 10537 (offset -15 lines).
patching file Misc/NEWS.d/next/Build/2021-10-11-16-27-38.bpo-45405.iSfdW5.rst
patching file configure
patching file configure.ac

BUILD FAILED (Ubuntu 22.04 using python-build 20180424)

Inspect or clean up the working tree at /tmp/python-build.20241216110805.25461
Results logged to /tmp/python-build.20241216110805.25461.log

Last 10 log lines:
checking for python3.10... python3.10
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... "linux"
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: in /tmp/python-build.20241216110805.25461/Python-3.10.0':
configure: error: no acceptable C compiler found in $PATH
See config.log' for more details
```

---

The error indicates that a C compiler is missing from your system, which is required to build Python from source. Here’s how you can resolve this issue on Ubuntu 22.04 in WSL:

### Step-by-Step Fix

1. **Install Required Build Tools**:
   You need to install a C compiler and other dependencies to build Python:

   ```bash
   sudo apt update
   sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
   xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
   ```

2. **Verify GCC Installation**:
   After installing the tools, check if GCC is available:

   ```bash
   gcc --version
   ```

   If GCC is installed, you’ll see its version. For example:

   ```shell
   gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
   ```

3. **Retry the Pyenv Installation**:

   Run the command again to install Python 3.10.0:

   ```bash
   pyenv install 3.10.0
   ```

4. **Troubleshooting Additional Errors**:
   If you encounter any further issues, ensure that:
   - **Temporary directories are clean**: Delete any leftover build artifacts:

     ```bash
     rm -rf /tmp/python-build.*
     ```

   - **Pyenv is using the correct environment**: Ensure Pyenv paths are set up properly:

     ```bash
     export PATH="$PYENV_ROOT/bin:$PATH"
     eval "$(pyenv init --path)"
     ```

---

Once the installation completes:

1. Set the installed version as the global default:

   ```bash
   pyenv global 3.10.0
   ```

2. Check the Python version:

   ```bash
   python --version
   ```

You should now have Python 3.10.0 installed and working in your WSL environment!
