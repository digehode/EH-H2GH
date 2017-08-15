============
Python Tips
============

General
=======

Dropping into an interactive python shell
-----------------------------------------

This is useful if you need to debug something in code that runs as a script.  Often you want to know what conditions are at a particular point, or want to see what happens if you do X or Y.

The `code` module has a function called `interact` that will drop you into a shell at the point it's called.  

For example::

  for i in range(10):
      print(i)
      if i==7:
          import code
          code.interact(local=locals())



When run::

  0
  1
  2
  3
  4 
  5
  6 
  7
  Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>> dir()
  ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'code', 'i']
  >>> print(i)
  7
  >>>  (Ctrl-D)
  8
  9
  >>> 
