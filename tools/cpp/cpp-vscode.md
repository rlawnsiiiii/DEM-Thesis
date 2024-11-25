# Visual Studio Code for C++

[Vistual Studio Code](https://code.visualstudio.com/) is a code editor for Windows, macOS, and Linux. While the [source is open](https://github.com/microsoft/vscode), the binaries are freeware.
We use VSCode as an example not only because of the open-source development and multi-platform availability, but also because it is simpler than traditional Integraded Development Environments, while being able to work nicely with other tools.

## C++ extensions

We will be using the following extensions:
- [C/C++ for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [C++ Intellisense](https://marketplace.visualstudio.com/items?itemName=austin.code-gnu-global)

## Configuring your project

**Important:** Before being able to build, run, or debug your code, you need to [configure VS Code for C++](https://code.visualstudio.com/docs/cpp/config-linux). Alternatively, you can try the [Code Runner extension](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner), or [start a terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) and call your compiler manually (see separate Moodle page).

Summary / quick start:

- Your file needs to be inside a folder and you need to "Open folder".
- VSCode will create a hidden folder `.vscode` with configuration files for building and running your project.
- To build:
    - (1st time) In the menu bar, click `Terminal > Configure default build task`. Select `C/C++: g++ build active file`. This will create a file `tasks.json`. Save it and focus on your C++ code file.
    - With your C++ code file active, press `Ctrl`+`Shift`+`B` (or click on `Terminal > Run build task`).
- To run from the integrated terminal:
    - Focus on the `TERMINAL` at the bottom of the screen and execute your program (e.g. `./helloworld`).
- To run/debug:
    - (1st time) In the menu bar, click `Run > Add configuration...`. Select `C++ (GDB/LLDB)`.
    - In the sidebar, focus on the `Run` view and click `Start debugging` (the "play" button).

<br/>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QNFGtTbTH-A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br/>

## Working on remote machines

Are you running your code on a remote machine? Then why not directly edit and build it there as well, directly from your local VSCode installation?

VSCode offers very easy [Remote development using SSH](https://code.visualstudio.com/docs/remote/ssh). Just install the ["Remote - SSH" extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh). Then, on the left sidebar, under "Remote Explorer", click on "Add New". Just add the usual SSH command you would normally use to access your files.

Then connect to the new SSH target. You don't need to have anything special installed: VSCode will set up the environment for you, without requiring any special rights.

Continue with opening some project. You will notice that VSCode points directly to the remote machine. Similarly for the integrated terminal. While you see and edit the code locally, all commands are being executed on the remote machine, allowing you to use the toolchain available in the remote machine without having to install anything else than VSCode on your local system.

## Resources

- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
