# Auto-vectorization for C++

Vectorization refers to a special set of CPU instructions that are able to process multiple data simultaneously with a single instruction. These are called [Single Instruction Multiple Data (SIMD)](https://en.wikipedia.org/wiki/SIMD).

Auto-vectorization refers to the compiler's ability to detect the opportunity for such instructions automatically and generate assembly using SIMD. Warning: this feature varies greatly between compilers and even versions. Typically auto-vectorization is enabled by advanced optimization levels (-O2 or -O3) but we should check the compiler output (reports and / or assembly) to see whether vectorized code is actually generated.

An alternative to auto-vectorization are hand-written assembly or [intrinsics instructions](https://software.intel.com/sites/landingpage/IntrinsicsGuide). Both of these options might result in faster code but at the cost of readability and portability to other architectures.

## GCC

```shell
g++ -O2 -ftree-loop-vectorize -fopt-info-vec-all mycode.cpp
```

- `-ftree-loop-vectorize` enables auto-vectorization of loops explicitly (default in `-O3`)
- `-fopt-info-vec-all` as well as `-fopt-info-vec-missed` and `-fopt-info-vec-optimized` print the vectorization report.

Read the manual for more information: `man g++`.
(How to search a manual? It it usually displayed in `less`, where you can search with `/your text` and move to the next entry with `n` (or previous with `N`). Quit with `q`.)

## Clang

```shell
clang++ -O2 -Rpass=loop-vectorize -Rpass-missed=loop-vectorize mycode.cpp
```

- `-Rpass=loop-vectorize` shows the loops that were vectorized.
- `-Rpass-missed=loop-vectorize` shows the loops that were not vectorized and why.

## Intel compiler

You can get the Intel compiler either from Intel's website or you can use it on the Linux cluster.
```shell
icpc -O2 -qopt-report=5 mycode.cpp
```

- `-O2` includes auto vectorization.
- `-qopt-report=5` will write the vectorization report to `mycode.optrpt`.
