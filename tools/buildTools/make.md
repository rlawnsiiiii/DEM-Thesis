# GNU Make

## Minimal Example 

With [GNU Make](https://www.gnu.org/software/make/) we can automate our code building, so that we simply type `make`. To be able to do that, we need to write a file named `Makefile`, such as:

```Makefile
CXX = g++
CXXFLAGS = -g -Wall    

code: code.o mysquare.o
    $(CXX) -o code code.o mysquare.o $(CXXFLAGS)

code.o: code.cpp mysquare.h
    $(CXX) -c -o code.o code.cpp $(CXXFLAGS)

mysquare.o: mysquare.cpp
    $(CXX) -c -o mysquare.o mysquare.cpp $(CXXFLAGS)

clean: 
    rm mysquare.o code.o code
```

- The `CXX` sets the C++ compiler we want to use.
- The `CXXFLAGS` are the options that we will be passing to the C++ compiler (here `-g` to enable Debug symbols and `-Wall` to enable all warnings).
- The **target** `code` is the first one in the file and thus the one executed when running `make`. This target depends on the object files `code.o` and `mysquare.o`. If these files are already present, Make will run `g++ -o code code.o mysquare.o -g -Wall`. If some of these files are not present, Make will build them following the rules that follow.
- `code.o:` depends on the files `code.cpp` and `mysquare.h`. It builds `code.o` running `g++ -c -o code.o code.cpp -g -Wall`.
- Similarly for `mysquare.o`.
- `clean` defines a target that completely cleans up the build: it deletes the object files and the executable binary. We can call it as `make clean`. Similarly, we could add more custom targets to our Makefile.

One of the main advantages of a build system (such as Make) is that it only builds the required object files only if the source files they depend upon change. This can save substantial amount of time when we rebuild a project during development.

## Additional Hints

- Parallel building: In a project that depends on multiple object files, we can also parallelize the building using the `-j` flag. For example, if we want to build four objects at the same time, we can run `make -j 4`. But how many should we use? A good guideline is to use as many threads as the logical cores of our CPU. A higher number will likely not offer much benefit (may even slow down), while it will also increase the memory usage significantly, potentially leading to issues of excessive memory usage.
- Verbosity: To check what exactly `make` does execute `make VERBOSE=1` to see every single command. This is very useful for debugging the build process.
