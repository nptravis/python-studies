You already have a process bound to the default port (8000). If you already ran the same module before, it is most likely that process still bound to the port. Try and locate the other process first:

$ ps -fA | grep python
  501 81651 12648   0  9:53PM ttys000    0:00.16 python -m SimpleHTTPServer
The command arguments are included, so you can spot the one running SimpleHTTPServer if more than one python process is active. You may want to test if http://localhost:8000/ still shows a directory listing for local files.

The second number is the process number; stop the server by sending it a signal:

kill 81651
This sends a standard SIGTERM signal; if the process is unresponsive you may have to resort to tougher methods like sending a SIGKILL (kill -s KILL <pid> or kill -9 <pid>) signal instead. See Wikipedia for more details.

Alternatively, run the server on a different port, by specifying the alternative port on the command line:

$ python -m SimpleHTTPServer 8910
Serving HTTP on 0.0.0.0 port 8910 ...
then access the server as http://localhost:8910; where 8910 can be any number from 1024 and up, provided the port is not already taken.