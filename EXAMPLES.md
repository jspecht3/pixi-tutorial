# Compiling C++ source code with CMake using pixi
While pixi is a conda package manager, various packages on the different conda channels can compile others codes, such as: C++ and ForTran. 

In this example, we will demonstrate C++ compliation with some basic C++ source code, which will be compiled with CMake. CMake is a widely used tool that compiles C++ software (e.g., OpenMC). This example is NOT a CMake or C++ tutorial, but rather, shows how pixi can reduce end-user compilation errors and trouble.

If you are interested in learning more about CMAKE and how to use it, please visit their [website](https://cmake.org/) for documentation and use-cases.

## User Compilation with pixi
After having cloned [the repository for this tutorial](https://github.com/jspecht3/pixi-tutorial), make your way to `examples/compiling-cpp`.
 
In `compiling-cpp`, you will find a `pixi.toml` file. As you have learned, this `.toml` file indicates that you are in a pixi project. In this case, the project is called `NameGetter`. Normally, when compiling C++ source code with CMake, a lot of terminal commands are needed, but, in this project, we only need two. 

First, we will first run `pixi install` to initialize the `pixi` environment. Second, we will run `pixi run compile` to compile the files, where the `compile` command is a task created to minimize the number of steps the end-user needs to run.
```
$ pixi install
✔️ The default environment has been installed.
$ pixi run compile
```

Now, we can check the directory to see `NameGetter`, the executable file that was created:
```
$ tree -I 'build'
.
├── CMakeLists.txt
├── NameGetter
├── README.md
├── main.C
├── pixi.lock
└── pixi.toml

1 directory, 6 files
```

❓❓❓❓❓❓ To run the `NameGetter` executable, you must use `./NameGetter` as the executable is not installed on your computer (as that would be silly for a quick example guide). ❓❓❓❓❓❓

## User Compilation without pixi
Now, lets see what we would need to do without pixi. First, when installing, we always ensure CMake is up to date.
```
CMake --version
```
If the output is an older version than the `cmake_minimum_required` parameter in the CMakeLists.txt, we must then upgrade our CMake to be compatible. For much larger projects with many more dependencies, this would have to be run for each dependecy. Luckily, `pixi` automatically checks for compatibility and updates CMake if needed when we run `pixi install`.

After we check to make sure our CMake is installed and up to date, now we can try to compile. To do this, the following code block is needed:
```
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
```

For this project, it should be noted that CMake builds `NameGetter` in the `build` directory. However, we want `NameGetter` in the `compiling-cpp` directory.
```
.../build:$ mv NameGetter ../
.../build:$ cd ../
```

Now, we can investigate the directory to make sure `NameGetter` arrived as expected.
```
$ tree -I 'build'
.
├── CMakeLists.txt
├── NameGetter
├── README.md
├── main.C
├── pixi.lock
└── pixi.toml

1 directory, 6 files
```

## Conclusions
Although this example is very short, I am sure you can see how powerful `pixi` can be when you want your code to be replicated and compiled easily on another machine. Depending on how dense your `pixi` tasks are and how strict you are with dependencies, there can be little to no room for end-user error when compiling, even across platform.
