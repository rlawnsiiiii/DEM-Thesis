# Measuring and profiling runtime of C++ programs

We can measure runtime in different ways. First, we can profile our code to see where most of the runtime is spent. Next, we can focus on specific areas using our own timers.

## Profiling with gprof

gprof is a tool that comes with the GCC compiler collection. General workflow:

1. Compile your code with `g++ -pg mycode.cpp -o mycode`
2. Execute your code normally and it will generate data (stored in `gmon.out`)
3. Analyze the data with `gprof mycode gmon.cout > report.txt`. Read `report.txt` in any text editor.

See also this nice [page from LRZ](https://www.lrz.de/services/compute/linux-cluster/tuning/gprof/index.html) for more details.

## Profiling with perf

[perf](https://perf.wiki.kernel.org/index.php/Main_Page) is a very powerful tool for deep performance analysis. General Workflow:

0. Compile with `-fno-omit-frame-pointer` (e.g. by adding it to the `cmake target_compile_options`) for higher quality results. This does not have a significant performance impact.
1. Execute your code via: `perf record -g ./myProgram`
    - `-g`: stores a call-graph
2. Display collected data: perf report -g 'graph,0.5,caller'
    - `-g`: call-graph
    - `graph`: print type as absolute overhead rates
    - `0.5`: threshold what to throw out
    - `caller`: invert call tree (=more intuitive)
3. Press `a` to dive into the assembly and see exactly (maybe one instruction off due to sampling inaccuracy) where time was spent.

Note: The first time you run perf, you will get an error that access to performance monitoring and observability operations is limited. Follow the instructions to enable this and remember to reset it to the default option afterwards, for security reasons.

## Measuring time with the chrono library

We can also time specific regions of our code:

```cpp
#include <chrono>

//...
std::chrono::time_point<std::chrono::system_clock> start;
std::chrono::time_point<std::chrono::system_clock> end;

start = std::chrono::system_clock::now();
// ... code region measured
end = std::chrono::system_clock::now();

auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

std::cout << "Elapsed time:" << elapsed_time.count() << "ms" << std::endl;
```

