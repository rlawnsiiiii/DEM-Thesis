# Debugging

At some point in the code development cycle bugs will creep into the software.
Very common types of problems are:

* The program throws a SIGSEV (Segmentation fault; exit code 139) and crashes
* The program crashes because of an unhandled exception
* The program simply does not work as intended.

Even though these problems have different sympomatics and are quite different problems, the tools we use to mitigate them are the same.

## The printing approach

A very straight forward idea would be to insert a lot of `std::cout << "i am here" << std::endl;` statements into the code and check which line got executed last.
For small projects where you already know roughly where it crashes, this approach might work.
For bigger projects or problems that only occur seemingly unpredictably, this approach might not work very well.

## Debuggers

Since the printing approach is not really helpful with bigger and more complex programs, people developed specialized software to debug C++ programs.
A very common tool used for debugging is `gdb`, which is part of the [GCC](https://gcc.gnu.org/) toolchain.
[CLANG](https://llvm.org) also has a tool for debugging which is called `lldb`. It has a similar featureset as `gdb`, but with some differences in some commands.
Intel also has a debugger packaged with their compiler suite.

In this document however, we only show `gdb`.

In order to have a good debugging experience, it is highly recommended that the code is compiled either with the minimum optimization level (`-O0`) or with the [special debugging optimization flag](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#index-Og) (`-Og`). Additionally debug symbols should be added to the binary with the option (`-g`).
Otherwise, the debugger will just show adresses and offsets which are not really understandable. The compilation command could then look like:

```shell
g++ -O0 -g mycode.cpp -o mycode
```

After building the application, there are bascially two options on how to proceed:

1. Start the program with the debugger in a interactive way by typing `gdb mycode`, or
2. Execute the program and use post mortem analysis `./mycode`

### Debugging with gdb

After starting the debugger with the program via `gdb mycode`, the terminal should look something like:

```shell
GNU gdb (GDB) 13.2
....
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from mycode...
(gdb)
```

Now, `gdb` is ready to debug the application. In general, gdb has a command-line interface which is the default view that is opened when starting gdb. In this command line, it is possible to execute commands. Below, you can find a non-exaustive list of commands. Detailed descriptions are following in the next sections.

#### Important commands overview

* `run` : starts the execution of the program
* `quit`: exit execution and gdb
* `breakpoint mycode.cpp:3` set a breakpoint in the file `mycode.cpp` in line 3
* `breakpoint myfunc` sets a breakpoint for the function `myfunc`
* `watch variable`: watches changes to the `variable` and stops executions like a breakpoint
* `next`: when execution is stopped typing next advances the execution one line
* `step`: same as next but also "steps" down the callstack into functions
* `until`: iterate over loop
* `print name`: prints the variable called `name`
* `backtrace`: print stacktrace
* `continue`: run until the next breakpoint
* `frame 4`: selects the frame 4 as displayed in the `backtrace` command to be the active frame
* `up / down`: move up or down in the stacktrace
* `tui enable`: enable text user interface
* `STR + L`: refresh a broken interface

It is not necessary to type out the full commands. You can abbreviate as much as you want as long as it is unambiguous. E.g. `r` for `run` or `bt` for `backtrace`
##### Controlling execution

If you want to stop your program in a certain function or line and investigate the values of variables you need to setup the breakpoints before executing the program.
Typical commands would be:

```shell
$ gdb ./mycode 

(gdb) breakpoint mycode.cpp:3
> Breakpoint 1 at 0x1178: file mycode.cpp, line 3.
(gdb) run
> Hit Breakpoint 1
(gdb) step
(gdb) next
(gdb) print my_variable
> my_variable="Hello World!"
(gdb) watch my_variable
(gdb) continue
(gdb) quit

```

The `>` symbol indicates output by the gdb interface.

##### Enabling the TUI

Even though the cli of gdb is powerful, sometimes it makes sense to also have the source code displayed in the same file. This is also possible by enabling the text user interface by typing `tui enable`.
To disable it, type `tui disable`.
With the `focus` command, you can switch which window your keystrokes (such as arrow up and down) will target.
`focus cmd` sets the focus to the command window whereas `focus src` set it to the source code browser. This enables you to browse through the source file with the arrow keys.
Sometimes the TUI gets broken: In this case, press `STR` togehter with `L` on your keyboard and the TUI will refresh.

##### Customizing `.gdbinit`

You can configure `gdb`'s behavior and appearance through the config file `~/.gdbinit`. This is extremely powerful and allows for IDE-like visuals and experience. You can use elaborate approaches like [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard) by simply downloading the config file.
##### Navigating the stacktrace

Another important concept for debugging is to know how to traverse through the stacktrace. The hierarchy of functions calling other functions is represented in the stacktrace. By typing `backtrace`, gdb will give you a complete overview about the caller hierarchy. In other words: Which function was called by which other function with what arguments. To navigate this hierarchy, gdb provides two mechanisms: By typing `up` or `down` to move up or down respectively. Another way to do it is to directly indicate which frame is selected by `frame 3` to select frame 3.

### Find the problem after the program crashed

If the program crashes, sometimes the operating system saves a `core` with the last state of the program before it crashed.
The operating system will let you know that it created one by writing `(core dumped)` in the terminal after execution finished.

#### Investigate the core

In order to load the core you can use the tool `coredumpctl`.
Executing `coredumpctl --help` should give a nice overview of the options available:

```shell
coredumpctl [OPTIONS...] COMMAND ...

List or retrieve coredumps from the journal.

Commands:
  list [MATCHES...]  List available coredumps (default)
  info [MATCHES...]  Show detailed information about one or more coredumps
  dump [MATCHES...]  Print first matching coredump to stdout
  debug [MATCHES...] Start a debugger for the first matching coredump
```

`coredumpctl debug` will load the last dumped core and open with the default debugger (normally gdb).
Note that all the commands that control the execution are not available anymore, since the program already has crashed. Normally you can navigate the stacktrace and look at the instruction / line in your code that caused the program to crash in the first place.
Sometimes, the crashes happen somewhere deep in a library that might not have debug symbols available. In this case, it might be helpful to navigate up the stacktrace until you find the location where your code called that library function.