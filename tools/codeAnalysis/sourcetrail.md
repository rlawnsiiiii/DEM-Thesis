# Sourcetrail

Are you looking into a huge code base and have no clue what is going on? This is the tool you want to use to connect the dots!
Sourcetrail is a code explorer that connects an interactive UML-ish view with the source code. Have a look at the [github repository](https://github.com/CoatiSoftware/Sourcetrail), they have pretty pictures ;)

Although the project is now officially discontinued, the github repository is archived and you will still be able to download releases.

Their documentation on installation and usage that you can find in the repo is already very good, so this document shall only serve as a TL;DR.


We will use a C++ project as an example, but Sourcetrail also supports other languages.

## Initializing a C++ project

The easiest way is to make use of CMake. If your project is built differently, refer to the documentation of Sourcetrail. One alternative is using [Bear](https://github.com/rizsotto/Bear) to generate the needed compilation database.

1. Create a [`compileCommands.json`](https://clang.llvm.org/docs/JSONCompilationDatabase.html) via the [`CMAKE_EXPORT_COMPILE_COMMANDS`](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html) option e.g. like this:
```bash
cd path/to/build/
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON path/to/CMakeLists.txt
```

2. In Sourcetrail: create a New Project -> Add Source Group -> C++ -> C/C++ from Compilation Database.

3. Make sure all relevant headers are included. Optionally exclude build, documentation, and tests folders.

4. Hit create to index the project. If you get errors, have a look at the error messages. In that case, click Project -> Edit Project and go back to step 3.

This will create the files `<project>.srctrlbm`, `<project>.srctrldb`, `<project>.srctrlprj`, which you may want to add to your `.gitignore` (if any).

### Troubleshooting

- If you are on Windows and the code is on the WSL this is [not supported](https://github.com/CoatiSoftware/Sourcetrail/issues/1207). The code needs to be located directly in the Windows file system.

- If you get errors about undefined references, you are missing includes / include paths.

- After a compiler or library update, some (include) paths might have changed, which leads to Sourcetrail not being able to find them anymore. To resolve, remove all includes and click detect.

- Even if you set it in your CMake code, Sourcetrail might not choose the correct C/C++ standard version. You can specify this by explicitly adding e.g. `-std=c++17` to the "Additional Compiler Flags".

## Use cases

Some ideas what you can do with the tool.
You can use it to click your way through classes and members, see what members are used by some function, search for logic flow connections between symbols (think: how is the call path from function A to B), or many more.

### Manual exploration

Find a symbol to start from via the search box at the top. Now you can click your way through the code base either by clicking on the fields in the graph view or clicking on the code.

### Logic Flow (aka. Custom Trail)

This feature gives you a visual representation how two symbols in the code are connected logically. For example, the call path of some function from another or through which interfaces a class accesses some variable.

Hit the Z shaped button ("custom trail") on the top left in the graph view. In the popup, define a start and end symbol (variable, function, class, ...). If the symbols are far apart, you might want to disable some node and edge types, otherwise Sourcetrail will complain that the generated graph is too large. Finally, be very careful with the maximum search depth.

### Tutorial

Sourcetrail comes with a tutorial project which contains annotated source code, explaining the usage of the tool. You can find it under "Recent Projects" in the main menu. Look for the `start_tour()` function to start.
