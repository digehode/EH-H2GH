=========
 NUGGETS
=========

Log and view at once
====================

**Option 1**: use ``tee``.  This dumps to a file and still shows the output::
  
  $ someCommand | tee some.log

**Option 2**: use ``tail``. In one terminal you run the command and log the output. In another, you watch the log file::
    
  $ somecommand > some.log

And in another terminal::
    
  $ tail -f some.log

The ``-f`` switch means "follow", so rather than show just what's there now, it shows things that get added.


Use ``aha`` to make HTML logs
=============================

You can use thr ``aha`` command to make logs that have formatting (escape codes and tabbed tables, etc) into nice HTML files::

  $ someCommand | aha > some.log.html

What ports do I have open?
==========================

Forgotten what you have running?  Cant remember the port you used for your reverse shell listener?::

  $ netstat -tulpn
  
