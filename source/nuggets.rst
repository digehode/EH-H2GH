=======
NUGGETS
=======

--------------------------------------------------------------------
Stuff that needs to go somewhere when there's somewhere for it to go
--------------------------------------------------------------------


Linux
=====

Log and view at once
--------------------

**Option 1**: use ``tee``.  This dumps to a file and still shows the output::
  
  $ someCommand | tee some.log

**Option 2**: use ``tail``. In one terminal you run the command and log the output. In another, you watch the log file::
    
  $ somecommand > some.log

And in another terminal::
    
  $ tail -f some.log

The ``-f`` switch means "follow", so rather than show just what's there now, it shows things that get added.


Use ``aha`` to make HTML logs
-----------------------------

You can use thr ``aha`` command to make logs that have formatting (escape codes and tabbed tables, etc) into nice HTML files::

  $ someCommand | aha > some.log.html

What ports do I have open?
--------------------------

Forgotten what you have running?  Cant remember the port you used for your reverse shell listener?::

  $ netstat -tulpn
  

Windows
=======


Find windows version from cmd/ps
--------------------------------

Very simple::

  c:\> ver
  Microsoft Windows [10.0.15063]

Check for updates from cmd/ps
-----------------------------

Let's say you have a cmd or powershell shell on a windows box and want to know if the exploit you found will work. If you know the update number, you can check it with::

  c:\> wmic qfe | find "0224"

Where 0224 is replaced by the update ID. If nothing shows, the patch isn't applied.  You can also get a full list of applied fixes with::

  c:\> wmic qfe    

Now try reading the official WMIC docs and see id you can find "qfe" as an option. I'll even give you the link: https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/wmic.mspx?mfr=true

Horrible windowses.  
