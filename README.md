# pixi tutorial
A quick tutorial for the "project manager" `pixi`. Although this tutorial is in python, `pixi` supports many other languages.

(adapted from the [pixi github](https://github.com/prefix-dev/pixi), go here if you want a more in depth explaination of anything here)


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


## Getting Started
Before getting into any development, preperations should be made.

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


## Making Your Own Project
To start, make a directory where you want your project to live and go into that directory
```
mkdir ~/project/path/pixi-example
cd ~/project/path/pixi-example
```
In this directory, we need to initialize a `pixi` project
```
pixi init
```
### Introduction to `pixi.toml`
Initializing a `pixi` project creates a `pixi.toml`, which gives an overview of the project. Inside this file is where you can add github actions and add more platforms.
```
vi pixi.toml
```
This file is meant to be human readable, so any information you want about the project is probably here. The `authors` will automatically populate with your linked `git` e-mail. In the `platforms` line, you will see your operating system. If you want to make your project compatible with other platforms, add them here and `pixi` will handle the rest.
```
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]
```

### Adding the First Python Package
Right now, we have no non-standard `python` packages, but adding them is very easy. Let's add numpy to our project:
```
pixi add numpy
```

Adding the first package does two things: creates a `pixi.lock` file and updates the `pixi.toml` file to include the new dependency. The `pixi.lock` file is for robots and is how `pixi` is able to recreate the environment on other machines. Inside `pixi.toml`, we can now see `numpy` was added to the dependencies.
```
$ cat pixi.toml | tail -2
[dependencies]
numpy = ">=2.0.1,<3"
```

### Running Python
Before moving on, we should have a file we can test with. Create a `.py` file and add the following.
```
$ vi example.py

##### Add the following #####
import numpy as np
print(np.pi)
```

Try running the file, which should not work.
```
$ python example.py
ModuleNotFoundError: No module named 'numpy'
```

`numpy` was added to the `pixi` project in `pixi-example/`, not globally, so the global `python` command has no idea what `numpy` is.

To run our file, we can use two main methods: in a `pixi` sub-shell or using `pixi run python-file.py`. The choice of which method to use is primarily personal preference.


#### Sub-shell Method
Enterning the sub-shell creates a temporary python environment with all the installed packages being available.
```
joe@v5:~/...$ pixi shell
(pixi-example) (base) joe@v5:~/...$
```
Running the file now returns the expected result.
```
$ python example.py
3.141592653589793
```
If you want to stay in the file:
```
$ python -i example.py
3.141592653589793
>>> print(np.cos(np.pi / 2))
6.123233995736766e-17
>>> exit()
```
You can exit the sub-sell the same way you exit a regular shell.
```
(pixi-example) (base) joe@v5:~/...$ exit
joe@v5:~/...$
```

#### `pixi run` Method
Using `pixi` run does not require you to enter a sub-shell and can be done with
```
joe@v5:~/...$ pixi run python example.py
3.141592653589793
```

### Tasks
Tasks are user-built commands with an analogous level of versitility to bash scripts. The sky ☁️ is the limit.

We can create a task that outputs the result of `example.py` from earlier.
```
pixi task add example "python example.py"
```

We can run the task and see that the output is $\pi$ as expected.
```
joe@v5:~/...$ pixi run print
✨ Pixi task (example): python example.py
3.141592653589793
```

#### Tasks with Dependencies
A lone task may not change the world, but together they just might. You can create tasks that depend on other tasks. To do this, let's open `example.py` 
```
$ vi example.py
```
and modify it to write to an output file.
```
import numpy as np
print(np.pi)

# add the three following lines
f = open('pi.txt', 'w')
f.write(str(np.pi))
f.close()
```

Now we can add a new task that outputs the value in `pi.txt` with a bit more than just the value.
```
pixi task add print "echo 'According to numpy, pi = $(cat pi.txt)'" --depends-on example
```
The `depends-on` option tells pixi that `example` needs to be run before `print`. Let's first verify `pi.txt` does not exist yet.
```
$ ls *.txt
commands.txt
```

We can then look at the output of this task.
```
joe@v5:~/...$ pixi run print
✨ Pixi task (example): python example.py
3.141592653589793

✨ Pixi task (print): echo 'According to numpy, pi = 3.141592653589793'
According to numpy, pi = 3.141592653589793
```
Without us ever having ran the `python` file `example.py` or the `pixi` task `example`, we generate the output file `pi.txt` that we can see is now in the directory.
```
$ ls *.txt
commands.txt  pi.txt
```

This is a rather trivial example, but hopefully you see how powerful these tasks can be when trying to make your code easy for others to run.

## Using Somebody Else's Project
First, you have to make sure somebody used `pixi` for their project. Usually, people that use `pixi` will not miss the chance to tell others about it, so it should be pretty easy to spot. Luckily, this repository is somebody else's `pixi` project.

First, nagivate to the folder you want the repository in, clone the repository, and navigate inside.
```
cd ~/projects

# with an ssh key
git clone git@github.com:jspecht3/pixi-tutorial.git
# with the URL
git clone https://github.com/jspecht3/pixi-tutorial.git

cd pixi-tutorial
```
