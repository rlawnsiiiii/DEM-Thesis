# ParaView

The general concept of ParaView is to build visualization pipelines of sources and filters, and display selected elements of them in some view.

In principle all of this can be done via a Python API, however this file only covers the GUI application.

Fine tune all of the techniques to your needs.

## Particle Simulations

Sources for particle visualizations can be anything that contains coordinates. E.g. `VTK`/`VTU` or `CSV` files. However, the parsed data needs to be interpreted as `PointData`. How ParaView sees the data can always be checked in the `Spreadsheet View`.

### `CSV` to `PointData`

The `CSV` has to contain one column per coordinate dimension. It can contain arbitrary additional data columns. In the end, each row is one particle.

- Load the file using the `CSV Reader`
    - Make sure that the right field separator is used.
    - Make sure to only interpret the first line as header if there is one.
- `Table to Points` filter
    - Make sure the right fields are used as x/y/z coordinates.

### Simple Particle Visualization

This visualizations renders 3D points as spheres.

- Load particle data source (suitable `VTK` or see [`CSV`](#csv-to-pointdata).
- Glyph filter
    - Type "Sphere"\
    Also Interesting but highly dependent on context: "Arrow".
    - Scale Factor 1\
    This should match the size of your particles (approximately sigma).
    - Masking mode "All Points"\
    This depends on your machine. It is probably not able to visualize 10^20 particles. If you can not show all particles use "Every Nth Point" to preserve spatial distributions. Pitfall: Even if you set Maximum Number of Sample Points" in "Uniform Spatial Distribution" to something larger than your total number of particles not every particle might be shown since they are still selcted statistically.
- Zoom to data
- Select data for coloring and rescale the color scale

[These steps in pictures](https://www.in.tum.de/fileadmin/w00bws/i05/FG_uploads/ParaviewVisualizeParticles.pdf)

### Path Lines

This visualization creates for every point a 3D sphere and a line that shows how it flies through the domain.

- Load particle data source (suitable `VTK` or see [`CSV`](#csv-to-pointdata).
- Temporal Particles to Pathlines filter.
    - Mask Points\
    Similar to Masking mode in the [simple visualization](#simple-particle-visualization).
    - Max Step Distance\
    How far can points move between two visualiation steps to be considered one particle.
    - Id Channel Array\
    Which information does paraview use to associate particles from two input files.
    Either choose an id if your particles have one, or choose `Global or Local IDs` to use
    the ordering of rows within the file. If you neither have an identifying attribute nor
    a constant ordering this visualization will not work.
    - In the Particles sub filter change the representation to `3D Glyphs` as in the
    [simple visualization](#simple-particle-visualization)

### Domain Decomposition (MPI)

When visualizing MPI parallel simulations, it may be desirable to see where each rank's region is. If the information is known, you can either painstakingly add box sources to manually add each subdomain, or if your program writes this information to a file use this.

Such files should contain structured points (`VTS`) where each point is a corner point of a subdomain. So for a simulation with six MPI ranks you should have `8*6=48` points. Furthermore, the file needs to associate the points to cells of a certain shape. See the official [VTK documentation](https://vtk.org/documentation/) for details. These cells should be associated with cell data which identifies the rank.

- Load the source containing the structured points and cells.
    - Change Representation to `Surface with Edges`
    - Color by rank id
    - Reduce opacity to `0.3`
    - Activate advanced properties (gear symbol next to the search field)
    - Change backface representation to `Surface with Edges`
    - If edges between ranks inside the domain are not showing (depends on how you define the cells) apply the `ExtractEdges` filter.

## Macros

Are you visualizing many similar datasets and annoyed of the repetitive clicking workflows? Macros to the rescue! The easiest way is to let ParaView observe your workflow, and then replaying it on demand.

- Tools -> Start Trace
- Do your workflow\
  ParaView will write a Python script that replicates your steps
- Tools -> Stop Trace\
  This should open a window that shows the generated script. We need to slightly modify it in order to make it more general.
    - The first step, where the source is chosen, should not be a function that finds a named file or source. Instead use `GetActiveSource()`
    - Optional: remove redundant assignments (e.g. the glyph type or scaling will be set multiple times in the script)
- Save the file
- Macros -> Import new macro ... -> select the file you just saved\
  A new button should have appeared on the top right with the name of the script.

Try it out by loading a new source, then hitting the button!

See [visualizeParticles.py](visualizeParticles.py) for an example macro script for the [Simple Particle Visualization](#simple-particle-visualization) workflow.

## Remote connection

Are you working on a remote machine? You don't need to start a (very laggy) ParaView instance on the remote machine, and you do not need to mount the filesystem. There is a better, very easy solution!

ParaView offers [Remote and parallel visualization](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html). How to:
- The same version (at least `major.minor`) of ParaView needs to be installed on both the remote and the local machine
   - The server is usually already included if you have ParaView installed.
   - If you don't have the same versions, just replace the version on either machine. There are portable binaries for multiple versions on the [ParaView Downloads page](https://www.paraview.org/download/). You don't need to have admin rights.
- On the remote machine, execute `pvserver`. This will give you some address details.
- On the local machine, start ParaView, and go to "File > Connect..."
- Click on "Add a server", set an arbitrary name, choose "Client / Server", use the login details of the remote machine for the "Host" (e.g., `atsccs123.in.tum.de`), and the port that the ParaView server reported.
- Click "Configure", and keep the pre-selected "Manual" mode in the next screen (i.e., you need to first start the remote server yourself).
- Then, select the server, and click "Connect".

You will see the server name and address on the Pipeline Browser. When opening files, you will be directly into the remote filesystem. Just open a file and use ParaView normally.

Common issues:
- ParaView server defaults to port 11111. This port is often blocked by default. Try using the port 8080, which is often properly forwarded, by starting the server as `pvserver --server-port=8080`. Adjust the local client accordingly.
- Even when the remote computer is behind a firewall blocking incoming connections, ParaView offers alternatives. You could try setting up a [reverse connection](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html#sec-reverseconnections).
