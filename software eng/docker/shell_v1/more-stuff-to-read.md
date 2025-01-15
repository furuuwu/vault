A error i got:

The error you're encountering, where Docker is trying to execute C:/sdks/Git/usr/bin/sh instead of running /bin/sh inside the container, suggests that your Windows terminal (likely Git Bash or a similar shell) is incorrectly handling the Docker command and looking for the wrong path.

This is likely due to the shell environment you're using on Windows. Docker on Windows has some peculiarities when using Git Bash or other shell environments, and the docker run command may be misinterpreting the shell path due to Windows path conventions.

Solution: use PowerShell or Command Prompt or WSL


You can override the CMD in your docker run command to launch an interactive shell instead of running the Python script. This way, the container will remain running, and you can interact with it.

`docker run -it --name <some-ctn> <some-image> /bin/bash`

To attach a shell (eg. bash or sh) to an **running** Docker container , you can use the docker exec command, which allows you to run commands inside a running container.

`docker exec -it <ctn-name> /bin/bash`

/bin/bash starts a Bash shell inside the container. If Bash is not installed in the container (it may not be in lightweight images like python:slim), you can use /bin/sh instead: