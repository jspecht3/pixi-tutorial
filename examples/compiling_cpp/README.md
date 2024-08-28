# Compiling C++ source code with CMake using pixi
While pixi is a conda package manager, there are packages on the various conda channels that can compile C++, ForTran, and other codes! This example aims to demonstrate this with a very basic C++ source code compiled with CMake, a tool widely used to compile C++ software (an example being OpenMC). This example is NOT a CMake or C++ tutorial, but rather shows how pixi can reduce end-user compilation errors and trouble!

If you are interested in learning more about CMAKE and how to use it, please visit their [website](https://cmake.org/) for documentation and use-cases.

## User Compilation with pixi
Please make your way to the `compiling_cpp` sub-directory in the `examples` directory. 
In this directory you will find a `pixi.toml` file. This .toml file, as you have learned, indicates that you are in a pixi project, this time the project is called `NameGetter`. 
Normally, when compiling C++ source code with CMake, a lot of terminal commands are needed. in this project only one is needed after initializing the pixi project. To initialize the pixi project, please run:

```
pixi install
```

With the project initialized you can now run:

```
pixi run compile
```

Now checking the directory to see if an executable file was created:

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
we can see the exectuable `NameGetter`! To run this executable, you must use `./NameGetter` as the executable is not installed on your computer (as that would be silly for a quick example guide).

## User Compilation without pixi
Now, lets see what we would need to do without pixi. First, when installing we must always make sure that CMake is up to date.

```
CMake --version
```
If the output is an older version than the `cmake_minimum_required` parameter in the CMakeLists.txt, we must then upgrade our CMake to be compatible. For much larger projects with many more dependencies, this would have to be run for each dependecy, whereas pixi automatically does this with `pixi install`. 

After we check to make sure our CMake is installed and up to date, now we can try to compile. To do this, the following code block is needed:

```
mkdir build
cd build
cmake ..
cmake --build .
```

Note that CMake, for this project, builds the executable in the `build` directory; to move it to the base diectory please run (while in the build directory):

```
mv NameGetter ../
cd ../
```
Now, finally we can investigate the directory for the executable.

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
Although this example is very short, I am sure you can see how useful pixi can be when you want your code to be easily replicated and compiled on someone else's machine. Depending on how dense you make your pixi tasks and how strict you are with the dependencies, there can be very little room for end-user error in compiling; even across platforms!

