===================================
 Connecting one machine to another
===================================


Using /dev/tcp
==============

You can create netcat-like connections like this::

  cat /some/file.txt > /dev/tcp/10.10.10.12/8765

Which pushes the contents of the file to port 8765 on machine 10.10.10.12, where you would have previously run something like::

  nc -lp 8765
