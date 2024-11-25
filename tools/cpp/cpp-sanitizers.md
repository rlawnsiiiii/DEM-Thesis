# Sanitizers for C++

Did you ever try to read an array element beyond the array bounds and your program went kaboom? Did you ever use uninitialized variables and you got strange values you did not know where they came from? Did you wish that someone had told you you have such an issue in your code? Then you need to use a sanitizer!

There are multiple tools that can check your code at runtime, such as:
- [Address sanitizer](https://clang.llvm.org/docs/AddressSanitizer.html): find out-of-bound accesses, use-after-free, double free, and memory leaks.
- [Memory sanitizer](https://clang.llvm.org/docs/MemorySanitizer.html): find accesses of uninitialized variables (not supported in GCC, only Clang).
- [Undefined behavior sanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html): find common instances of undefined behavior.

and more. Using multiple sanitizers at the same time is not recommended. Expect significant runtime and memory increase when using a sanitizer. While using them in production is not a good idea, you may want to add them to your continuous integration system.

While there is also a thread sanitizer that can check for race conditions, you may want to try [archer](https://github.com/PRUNERS/archer), instead.

You may want to watch [this talk](https://www.youtube.com/watch?v=Q2C2lP8_tNE) to learn more about what they are and how they work.

## Example

For GCC, compile and link with `-fsanitize=address`. Enable debug symbols to get information about the location of the issue.

For example, try building and running this code:

```c++
#include <iostream>

int main() {

  double *array = new double[4];
  std::cout << array[4] << "\n"; // fsanitize=address complains for out-of-bounds

  delete[] array; // fsanitize=address complains for memory leak if we ommit this
  std::cout << array[3] << "\n"; // fsanitize=address complains for use-after-free

  int* x;
  std::cout << *x << "\n"; // fsanitize=memory complains for uninitialized access
}
```

with:
```bash
g++ -fsanitize=address -g test.cpp
clang++-11 -fsanitize=memory -g test.cpp
```
