# Matplotlib

`matplotlib` is a very popular and versatile python library for plotting
figures and graphs. However, sometimes it can also come across as a little
confusing to beginners because there are two (somewhat different) plotting APIs
offered by `matplotlib`:

1. The `pyplot` (procedural) API that mimics MATLAB and

2. The object-oriented `Fig/Axes` API that really allows you to customize your plots
   as much as you want.

The `pyplot` API is what you want for quick and dirty
plots in an interactive session while you would probably reach for the
object-oriented API when creating plots for say a paper or a thesis when you
need more control. Here, we will only cover the `pyplot` API.

## `pyplot`

The pyplot API is very simple to get started with. While going through these
examples, you may want to refer to the [pyplot documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot). We will only cover a very tiny subset of what the reference contains. Let's begin by creating a simple plot. We'll be using `numpy` for some simple functions:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
# syntax: plot(x, y)
plt.plot(x, np.sin(x))
```

If you are running these commands from within a shell, you may additionally
need to call `plt.show()`.

What does this do? It creates a Figure (in a window) that contains an Axes (area
on which the plot is shown - not to be confused with the plot axis/axes). If a 
figure already exists, `plt.plot()` will use that one. Then, a sine wave is plotted
on this Axes.

You don't absolutely need to remember these terms right now but having some
idea of them will come in handy while reading the documentation.

### Labels, Titles and Colors

We can also set labels, titles and other things like that:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

# plot (x, y, args)
plt.plot(x, np.sin(x), color='red')

# fontsize only set for illustration purposes
plt.title("Displacement over time for an oscillating body", fontsize='14')
plt.xlabel("time (s)", fontsize='12')
plt.ylabel("displacement (m)")

# set x and y limits of the plot axes
plt.xlim(-5,5)
plt.ylim(-10,10)

# the resolution of the saved figure
# depends on the implicit "Figure" object.
# you can customize this by explicitly
# creating the figure yourself (see plt.figure())
plt.savefig("./displacement.png")
```

### Multiple plots with a legend

We can also have multiple plots, with different colors, linestyles, labels and a legend:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

plt.plot(x, np.sin(x), color='blue', label='sine', linestyle='dashed')
plt.plot(x, np.cos(x), color='red', label='cosine', linestyle='dotted')

# generate legend using "label"s defined on plt.plot
# and place it in the upper left (by default 'best')
plt.legend(loc="upper left")
```

`label`, `linestyle` and other properties like this are called keyword
arguments in python lingo. If you look at the documentation for `plt.plot` for
example, these are included in the `**kwargs` argument in the function
signature. `matplotlib` functions offer many keyword arguments like this that allow you
to customize your plot.

### `plt.subplot()` - Multiple Plots with separate Axes

What if you want to create separate plots, each with its own title, label, legend
and customization? Oh, you also want them to be different types of plots? Okay:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

# not strictly needed but allows us
# to set figsize -- used when saving figure.
plt.figure(figsize=(9,3))

# here's how to read the number within subplot:
# 1 (one row), 3 (3 columns), 1 (select first one of these):
plt.subplot(131)
plt.plot(x, np.cos(x))
plt.xlabel("time (s)")
plt.ylabel("displacement")
plt.title("displacement vs time")

# second plot is a bar plot
plt.subplot(132)
grades = ['1.0', '2.0', '3.0', '4.0']
num_students = [11, 24, 9, 2]

plt.bar(grades, num_students)
plt.xlabel("grade category")
plt.ylabel("num students with grade")
plt.title("Grade distribution")

# plot with errorbars
plt.subplot(133)
x = [1, 5, 8, 12]
plt.errorbar(x, np.sin(x), yerr=[0.08, 0.05, 0.1, 0.07], marker='o')

plt.xlabel("time (h)")
plt.ylabel("voltage reading (mV)")
plt.title("Voltage reading with select error bars")
```

## Where to go from here?

At this point, you should have a decent idea of how to use the `pyplot` API of
matplotlib. If you have a particular type of plot in mind, you can look at the
catalogue of [example
plots](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html)
on the matplotlib website, or the much more extensive [gallery of plots
here](https://matplotlib.org/stable/gallery/index.html). Beyond this, you are
encouraged to read the documentation. You will naturally pick up the Object
Oriented API doing this - [these tutorials will help you on the
road](https://matplotlib.org/stable/tutorials/index.html).
