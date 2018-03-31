## terminal

View core usage and split up.

## Limit RAM consumption

`ulimit -v 5000000`

for ongoing terminal process

## Multiprocessing

pool.map(f,argslist)

## Thread vs process

Thread is an OS level offering. Least overhead intensive. Share memory; may end up overwritting.

In python, it suffers from GIL. (Global Interpreter Lock). Redo in Cython.

Processes are isolated. Do not share information.

Perform code profiling to compare efficiency. Most of the time is spent in checking which core to run what code on.

## Spawning other Processes

Run other code while spawning one process:

pool.apply_async()

pool.map_async()

## Processes with Information Sharing


## Git lfs

chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=Git%20LFS%20-%20large%20file%20storage%20%7C%20Atlassian%20Git%20Tutorial&uri=https://www.atlassian.com/git/tutorials/git-lfs#how-git-lfs-works


 ## Cython in a Jupyter Notebook

 %load_ext Cython

 %%cython

use `cdef long func (long n)` as an example for cython. Fastest.
use `cpdef long func (long n)` as an example for python and cython.

## Define as a Cache function

Cache the declaration  of the function.

Under functools.

## profiling

cProfile, line_profile

cProfile.run(func,args)

Numba: JIT compiler for python (just in time compilation).

`from numba import jit`

Use as a function call or a jit decorator.

## ufuncs to vectorise

`from numba import vectorise`

vectorise(element_wise_function(*kwargs))
