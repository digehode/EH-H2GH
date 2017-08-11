
======================
 Scanning Web Servers
======================

There will be some overlap with these, but not 100%.  Nikto is good for general checking, testssl is great for checking the crypto settings, dirbuster really does a good job of enumerating folders.  Run them all.


Nikto
=====

Web server scanner. Highlights a number of potential issues.

Default nikto scan::

  $ nikto -host 192.168.0.11 > nik.log

testssl
=======

Tests SSL implementation and settings. Will highlight problems and throw up relevent CVE numbers.

Download::
  
  $ curl -L https://testssl.sh > testssl.sh
  $ chmod u+x ./testssl.sh

Run::
      
  $ ./testssl 192.168.0.11 > ssl.log

Dirbuster
=========

Brute-force a bunch of possible directories to discover web server layout.

With default word file::

  $ dirb 192.168.0.11 > dirbuster.log
