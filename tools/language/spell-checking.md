# Spell checking

## Codespell

If you want to find spelling mistakes in code, a normal spell checker may be tricky to set up. For this use case, you can use [codespell](https://github.com/codespell-project/codespell), instead. This works with many programming languages and code formats, including C++, LaTeX, and Markdown.

### Installation

This is a Python tool, which you can get from your distribution's package manager (`apt`, `pacman`) or from PyPI:

```bash
pip3 install --user codespell
```

### Running

Here is a first example:

```bash
codespell file.cpp
```

This will check `file.cpp` for spelling mistakes and report them to the terminal.

Codespell also has several options. Here is a more advanced example:

```bash
codespell src -w -q 3 -L precice,asend
```

This will:
- check all files in the `src/` directory
- overwrite the files with the suggestions, if possible (`-w`)
- using the "quiet level 3 (1+2)", which disables warnings about wrong encoding or binary files (`-q 3`)
- ignoring the words "precice" and "asend" (must be lowercase, it will ignore or permutations), as these are special terms and not spelling mistakes (`-L precice,asend`)
