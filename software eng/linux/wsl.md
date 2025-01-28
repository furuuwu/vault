# WSL

## documentation

<https://learn.microsoft.com/en-gb/windows/wsl/>

## installations

```shell
# list distributions
wsl --list --verbose
```

set a distribution as the default

```shell
wsl --set-default <distribution-name>

# eg
wsl --set-default Ubuntu
```

## launch and terminate

```shell
# run it
wsl

# switch to a different distribution
wsl -d <distribution-name>
```

Stop other distributions

```shell
wsl --terminate <distribution-name>

eg.
wsl --terminate docker-desktop
wsl --terminate docker-desktop-data
```

## users

run wsl as the root user

```bash
wsl -u root
```

changing the password for a user

```bash
passwd <user_name>
```

## WSL configuration

editing the default wsl configurations
(`~/.wslconfig`)

- you can change the default user there (eg. to root or devcontainers)

![a](img/2024-12-16-16-32-12.png)

## Windows filesystem vs Linux filesystem

![a](img/2024-12-19-09-20-06.png)
