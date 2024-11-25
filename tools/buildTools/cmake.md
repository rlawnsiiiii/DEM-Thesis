# CMake

With CMake we can **configure and generate** a build system configuration file, such as a Makefile. There are a few more build configuration systems, but [CMake](https://cmake.org/) and [GNU Autoconf](https://www.gnu.org/software/autoconf/autoconf.html) are maybe the two most popular at the moment. Such a system is particularly useful in large projects with many files, as well as in projects aiming for cross-platform compatibility.

## Minimal Example

Instead of defining a (rather complex) `Makefile`, we only need to define one (or more) `CMakeLists.txt`. You can follow the [official CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html), but for now, here is an example:

```cmake
cmake_minimum_required(VERSION 3.1)
project(Code VERSION 0.1.0 LANGUAGES CXX )
add_executable(code code.cpp mysquare.cpp)
add_executable(testmysquare testmysquare.cpp)
```

As you may already guessed, CMake uses its own language and thus the learning curve is a bit steep (but rewarding).

- With the `cmake_minimum_required`, you specify the minimum CMake version that can understand this `CMakeLists.txt`, because of newer CMake features we may need. Note that the newer dependency versions (such as the Boost library) may need a newer CMake version that contains a newer `findBoost.cmake` module (look this up if needed).
- With `project` we define a name for the project (here `Code`), its version (here `0.1.0`, to be changed every time we release a new version), and the involved languages (here C++).
- With `add_executable` we can add targets for executables we want to produce (here the target `code` need `code.cpp` and `mysquare.cpp`. `testmysquare` needs `testmysquare.cpp`).

## Out-of-source Builds

A usual structure of a project is:
```
- my_project/
   - build/
     - code
     - testmysquare
   - src/
      - code.cpp
      - mysquare.cpp
      - ...
   - CMakeLists.txt
```
For a project with such a structure, we build our project into `my_project/build/`. This is called an `out-of-source` build. We first change into that directory and execute:
```shell
cmake ..
```
The `..` points to the directory containing the `CMakeLists.txt`.

On a Linux system, this will generate by default a `Makefile`. We can then build our project normally using `make`.

## Additional Hints

- During its `configure` step `cmake` stores the state of many variables in `CMakeCache.txt`. If you run into troubles after you edit your `CMakeLists.txt` delete `CMakeCache.txt`.
- To choose the compiler you want to use in a build folder prepend variables specifying it when you invoke `cmake` the first  time. E.g. `CC=clang CXX=clang++ cmake ..`. The easiest way to change to a different compiler is to create a new folder.
- Instead of calling `cmake ..` use `ccmake ..` to get a [command-line gui](https://cmake.org/cmake/help/latest/manual/ccmake.1.html) where you can look at all the project's and cmake's variables, their values, and documentation.
- CMake can get particularly helpful to [test and install](https://cmake.org/cmake/help/latest/guide/tutorial/index.html#installing-and-testing-step-4) your project (have a look at [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html)), as well as to [create packages](https://cmake.org/cmake/help/latest/guide/tutorial/index.html#packaging-debug-and-release-step-12).

## Tutorials

- [cmake.org](https://cmake.org/cmake/help/latest/guide/tutorial/index.html): Original documentation and therefore always up to date. However, it might be a bit confusing for beginners.
- [Riptutorial](https://riptutorial.com/cmake): Covers all the CMake basics with examples. Very beginner-friendly.
- [CLion](https://www.jetbrains.com/help/clion/quick-cmake-tutorial.html#lib-targets): Tutorial on how to use CMake inside CLion, the best IDE for C++.
