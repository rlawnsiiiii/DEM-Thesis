# Code formatting for C++

One of the common arguments in collaborative software development is what indentation
style to use: tabs vs spaces, how many spaces, where should a `{}` block starts, etc.
This can also lead to merge conflicts that are formatting-only. For this reason,
it is very helpful to have one simple tool that manages the formatting for you
and keeps it consistent across code files and contributors.

One of the most popular tools for automatic C++ code formatting is [clang-format](https://clang.llvm.org/docs/ClangFormat.html).
You can use it in the terminal, but clang-format also integrates very well with common editors and IDEs.
For example, in VSCode, install the [clang-format extension](https://marketplace.visualstudio.com/items?itemName=xaver.clang-format).

If you prefer to run clang-format from the terminal, do:

```bash
# For formatting a single file
clang-format -style=file -i mycode.cpp

# For formatting all files in a directory
clang-format -style=file -i src/*

# For formatting all .h and .cpp files in all child directories
find . \( -iname "*.h" -o -iname "*.cpp" \) -exec clang-format -style=file -i {} \;
```

The `-i` option means that clang-format will format the file inline, i.e. it will overwrite it.
The `-style=file` means that it will use the settings defined in a `.clang-format` file, which
needs to be in the current or one of the parent directories.

You can also [define your own style](https://clang.llvm.org/docs/ClangFormatStyleOptions.html),
although this can be a long task. It is best and easiest to just use a [predefined style](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) and only change what you need (e.g. `ColumnLimit`).
At the end of the day, what matters most is that you have any automatic
formatting set up that everybody can use so you have a consistent look throughout your codebase
and avoid formatting-specific changes and conflicts.

It is important that you use the same clang-format version as the one used by the project, as different versions may yield different results. In case your OS distribution does not provide the specific version, you can also install it from PIP: `pip3 install --user clang-format=<version>`.
