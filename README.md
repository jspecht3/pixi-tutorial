# pixi tutorial
A quick tutorial for the "project manager" `pixi`. Although this tutorial is in python, `pixi` supports many other languages.

(adapted from the [pixi github](https://github.com/prefix-dev/pixi), go here if you want a more in depth explaination of anything here)


## Sections
- [Overview](#overview)
- [Installation](#installation)
  - [Linux](#linux)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Others](https://github.com/prefix-dev/pixi/main?tab=readme-ov-file#installation)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [Making Your Own Project](#making-your-own-project)
  - [Using Somebody Else's Project](#using-somebody-elses-project)

## Overview
What is `pixi`?
- `pixi` is a package mangager that greatly simplifies the effort required by the user to replicate their development environment on other machines
- `pixi` allows you to recreate your development environment with a single command

Who should use `pixi`?
- anyone developing python packages
- anyone who wants to replicate their development environment for others easily

Where can you use `pixi`?
- any major operating stystem
  - Linux, Windows, macOS (including Apple Silicon)

When to use `pixi`?
- any project where you would use a `python` environment or virtual environment for development or testing
- if you want your coding environment to be easily reproducible

How to use `pixi`
- Follow the installation instructions below 🙂

## Installation
The installation donwloads and runs the current `install.sh` file from [pixi github](https://github.com/prefix-dev/pixi)

Go to the [pixi github](https://github.com/prefix-dev/pixi) to update and uninstall.

Jump to whichever operating system you are using
- [Linux](#linux)
- [macOS](#macos)
- [Windows](#windows)
- [Others](https://github.com/prefix-dev/pixi/main?tab=readme-ov-file#installation) 🤷‍♂️

### Linux

Bash
```
curl -fsSL https://pixi.sh/install.sh | bash
. ~/.bashrc
```
Brew
```
brew install pixi
. ~/.bashrc
```

### macOS

Zsh
```
curl -fsSL https://pixi.sh/install.sh | zsh
source ~/.zshrc
```
Bash
```
curl -fsSL https://pixi.sh/install.sh | bash
. ~/.bashrc
```
Brew
```
brew install pixi
# if you use .bashrc
. ~/.bashrc
# if you use .zshrc
source ~/.zshrc
```

### Windows

PowerShell (may need to run as administrator)
```
iwr -useb https://pixi.sh/install.ps1 | iex
```
winget
```
winget install prefix-dev.pixi
```

## Usage
- [Getting Started](#getting-started)
- [Making Your Own Project](#making-your-own-project)
- [Using Somebody Else's Project](#using-somebody-elses-project)


### Getting Started
Before getting into any development, a preperations should be made.

First, if you are currently in a conda environment, you will see something that looks like this:
```
(base) joe@v5:~$
```
If you are not in a `conda` environment, good, the next step will not apply to you.

To get into an isolated environment for testing and replication purposes, we do not want to be in our own python environment that will have random packages installed.
```
(base) joe@v5:~$
(base) joe@v5:~$ conda deactivate
joe@v5:~$
```

Check that `python` does not work to verify no funny business is afoot.
```
$ python
Command 'python' not found, did you mean:...
```

Next, we can install `python` (and a lot of other useful non-python tools) with:
```
pixi global install python
```

This installs `python` in its own `pixi` controlled environment in `~/.pixi/envs/`. You can remove these environments anytime with `pixi global remove <env-name>`.

Now running `python` will go into a python sub-shell where you can enter python commands. However, there are no modules that we would want, but that is covered in the [next section](#making-your-own-project).
```
$ python
>>> import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> exit()
```

### Making Your Own Project
To start, make a directory where you want your project to live and go into that directory
```
mkdir ~/project/path/pixi-example
cd ~/project/path/pixi-example
```
In this directory, we need to initialize a `pixi` project
```
pixi init
```
This creates a `pixi.toml`, which gives an overview of the project. Inside this file is where you can add github actions and add more platforms.
```
vi pixi.toml
```
This file is meant to be human readable, so anything information about the project you want is probably here. The `authors` will automatically populate with your linked `git` e-mail. In the `platforms` line, you will see your operating system. If you want to make your project compatible with other platforms, add them here.
```
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]
```
Next, close the `pixi.toml` file.


### Using Somebody Else's Project
test
