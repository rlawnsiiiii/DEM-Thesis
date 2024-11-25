# Building C++ programs from your terminal

In order to execute C++, C or Fortran programs we need to "compile" them.
Compiling them translates the C++ code into machine instructions that the CPU can execute.

Imagine you have a single file with the following code:

```cpp
 #include <iostream>

 int main(int argc, char *argv[]) {
   std::cout << "Hello World!" << std::endl;
   return 0;
 }
```

You saved this code in a file called `mycode.cpp`.

A very common compiler is [GCC](https://gcc.gnu.org/).
But there is also the option to use [CLANG](https://llvm.org) or the Intel C++ Compiler.

## Building single files

In order to compile the C++ code we use the program `g++`. Note that `gcc` is a C compiler and does not have the capabilities to compile C++. If you try to compile C++ Code with `gcc` you will get weird error messages.

Below you find the command on how to invoke g++ to compile the mycode.cpp file into an exectuable called mycode.

```shell
g++ mycode.cpp -o mycode
```

### Optimizations

All major compilers implement the same optimization level options, although the actual optimizations might differ. Every level includes all optimizations from the lower ones. The levels are:

* `-O0`: No compiler optimizations (default)
* `-Og`: Reasonable level of optimization while maintaining fast compilation and a good debugging experience.
* `-O1`: Light optimizations that are quick to apply
* `-O2`: Most optimizations that do not significantly increase the size of the binary
* `-O3`: Full optimization focus on execution speed at the expense of the size of the binary and compile time.

Note, that if you want to debug your program using `-O0` or `-Og` is recommended, because otherwise optimizations might transform your code, and it becomes harder to match what is going on to your source code.

For more details, refer to your compiler's documentation. E.g. [GCC's](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)

## Run executable

After building the executable `mycode` you can run it by invoking it like:

```shell
./mycode
```

This should give you the `Hello World!` output in your terminal.
