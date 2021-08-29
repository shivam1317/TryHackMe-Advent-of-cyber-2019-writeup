## Q. 1 how many TCP ports under 1000 are open?

> PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 18:81:a7:cb:09:1e:27:4f:91:b5:3a:c2:4a:dc:d7:c5 (RSA)
|   256 7c:3c:5a:b4:8e:05:1c:22:bf:10:1d:5b:e2:8c:dd:64 (ECDSA)
|_  256 66:09:d9:6b:0b:7a:58:67:8d:d9:7d:6f:8c:39:92:f1 (ED25519)
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          39359/tcp   status
|   100024  1          49511/tcp6  status
|   100024  1          52729/udp6  status
|_  100024  1          58484/udp   status
999/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.8)
|_http-server-header: SimpleHTTP/0.6 Python/3.6.8
|_http-title: Directory listing for /


Ans : 3

------

## Q.2 What is the name of the OS of the host?

Ans : linux 

----

## Q.3 What version of SSH is running?

Ans : 7.4 (from nmap scan)

-----

## Q.4 What is the name of the file that is accessible on the server you found running?

![[Pasted image 20210723132852.png]]

Ans : interesting.file

----