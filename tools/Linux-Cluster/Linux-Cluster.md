# Linux Cluster

The Linux cluster is a medium sized HPC system hosted by LRZ: 
The documentation can be found at it's [LRZ page](https://doku.lrz.de/display/PUBLIC/Linux+Cluster)

## Get Access

Talk to your advisor how to get access. You will then be able to connect to the login nodes via `ssh`.

## Transfer Data

- For code: any version control system (e.g. `git`)
- For data: `scp`

## Module System

On clusters it is common to have software installed in environment modules. For extensive documentation execute:
```shell
man module
```

To see all currently loaded modules run the following command.
```shell
module list
```

This command gives you a list of all installed software.
```shell
module avail        # see all modules
module avail gcc    # see all gcc modules
```

Execute the following to see the effect of modules:
```shell
module load intel-mpi
mpicc --version
module switch intel-mpi openmpi/4.0.4-gcc8 
mpicc --version
``` 
First you load Intel MPI with the Intel compiler, later you switch to openmpi in combination with gcc. This way you can e.g. compare performance of different libraries.

## Slurm

On a cluster you normally work asynchronously. You first prepare your application (compile your code, prepare input files, ...) on the login node. Then you write a job script, where you tell the workload manager (here Slurm) which resources (i.e. how many compute nodes) you need and for how long. This script needs to be submitted to Slurm:
```shell
sbatch myScript.sh
```
Upon submission Slurm checks whether the script contains all necessary information, thus you can start with a minimal script only containing the information you need and expand what is necessary. Slurm then decides when to run your job. The more resources you want to use and the longer you want to use them, the longer you have to wait.

You should enable email notification in the job script to receive a messsage when your job is completed. Do not insert fake email adressess! This creates internal spam and you will attract the anger of admins ;)

Further Resources:
- [Documentation on the different queues available](https://doku.lrz.de/display/PUBLIC/Job+Processing+on+the+Linux-Cluster).
- [How to write your job-script](https://doku.lrz.de/display/PUBLIC/Running+parallel+jobs+on+the+Linux-Cluster).
- [Official Slurm documentation](https://slurm.schedmd.com). Be aware that Linux Cluster does not have the latest version of Slurm.

## Disk Space

Please do not write huge amounts of data to your `$HOME` as you share the disk space with other people. If you fill this up completely, no one can start new jobs and people will be angry at you.

Instead write large output files directly to `$SCRATCH`. There you have "unlimited" space since this deletes old data once it is full. For this reason do not use it as a long term storage of results.

