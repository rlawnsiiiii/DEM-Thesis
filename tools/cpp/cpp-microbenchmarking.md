# Microbenchmarking C++ 

Microbenchmarking is analyzing the performance of small snippets of code. A great framework for this is [Benchmark](https://github.com/google/benchmark) by Google. If you do not want to set up a whole project and just want to do simple quick tests [Quickbench](quick-bench.com/) is a easy way to use it.

## Google Benchmark

The idea is to write small functions that each represent a single benchmark. They should contain a loop that takes some state that is provided by the framework. This loop is then executed and measured until the framework considers the result to be stable.

To get insights on the code you actually use, these benchmarks should be compiled with optimizations enabled (e.g. -O3). In order to avoid having the compiler remove variables that are vital to your test, Benchmark provides a `DoNotOptimize()` function, which does not add any overhead but only marks this variable as relevant.

Have a look at the example to get an overview of the most important features:

```c++
static void vector_resize(benchmark::State& state) {
  // Code inside this loop is measured repeatedly
  for (auto _ : state) {
    std::vector<double> x{};
    x.push_back(10);
    x.push_back(20);
    x.push_back(30);
    // Make sure the variable is not optimized away by compiler
    benchmark::DoNotOptimize(x);
  }
}
// Register the function as a benchmark
BENCHMARK(vector_resize);

static void vector_reserve(benchmark::State& state) {
  // Code before the loop is not measured
  for (auto _ : state) {
    std::vector<double> x{};
    x.reserve(3);
    x.push_back(10);
    x.push_back(20);
    x.push_back(30);
    benchmark::DoNotOptimize(x);
  }
}
BENCHMARK(vector_reserve);
```

## Quickbench

See this [link](https://quick-bench.com/q/EtcGXL5xHrEnDnhOHorkYKW4YhY) for the example above in Quickbench. There you can try out different compilers, language and optimization levels, as well as directly look into the assembly.

## Additional Hints

* Watch the CppCon talk by Chandler Carruth ["Tuning C++: Benchmarks, and CPUs, and Compilers! Oh My!"](https://www.youtube.com/watch?v=nXaxk27zwlk) on analyzing code with perf, benchmarking with google benchmark and defeating compiler optimizers.
