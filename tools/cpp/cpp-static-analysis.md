# Static analysis of C++ programs

## clang-tidy

[clang-tidy](https://clang.llvm.org/extra/clang-tidy/) is a common static analysis tool that helps us discover common issues before we even compile our code. It also helps us follow the [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md) and discover more modern alternatives for some code parts. You can run it as a stand-alone tool from the command line, or integrate it with your IDE.

On Ubuntu, install the package `clang-tidy`. You may need to install additional packages in case clang-tidy does not find common headers (see an [issue with Ubuntu 22.04](https://askubuntu.com/a/1441954/142834)).

To use the full capabilities of clang-tidy, you will need to create a compilation database for your code, typically named `compile_commands.json`. If you are using CMake, you can enable the switch `CMAKE_EXPORT_COMPILE_COMMANDS` via `ccmake` or by specifying `cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON <path>`. In case you are not using CMake, [bear](https://github.com/rizsotto/Bear) can create such a database as well.

clang-tidy can perform several checks, most of which are disabled by default. Enabling everything will be overwhelming. Instead, select what you find relevant from the [list of checks](https://clang.llvm.org/extra/clang-tidy/checks/list.html). Start with the `modernize-*` and `cppcoreguidelines-*` checks.

Instead of specifying the checks you want via the command line, you can also add a `.clang-tidy` file in your project, describing the settings ([example](https://github.com/precice/precice/blob/develop/.clang-tidy)).

### Example

Consider the file `main.cpp`:

```c++
#include <iostream>

int main(){
  double * ptr;
  std::cout << *ptr << std::endl;
}
```

Analyzing it with

```shell
clang-tidy main.cpp -checks="cppcoreguidelines-*"
```

returns some warnings about not finding a compilation database, but also already some useful suggestions:

```text
/home/gc/Desktop/main.cpp:4:12: warning: variable 'ptr' is not initialized [cppcoreguidelines-init-variables]
  double * ptr;
           ^
               = nullptr
/home/gc/Desktop/main.cpp:5:16: warning: Dereference of undefined pointer value (loaded from variable 'ptr') [clang-analyzer-core.NullDereference]
  std::cout << *ptr << std::endl;
               ^~~~
/home/gc/Desktop/main.cpp:4:3: note: 'ptr' declared without an initial value
  double * ptr;
  ^~~~~~~~~~~~
/home/gc/Desktop/main.cpp:5:16: note: Dereference of undefined pointer value (loaded from variable 'ptr')
  std::cout << *ptr << std::endl;
               ^~~~
```

Before even compiling our code, we can spot that we are using `ptr` uninitialized.

Running `bear -- g++ main.cpp` or `bear -- clang++ main.cpp` generates a `compile_commands.json` and resolves the respective warnings.
