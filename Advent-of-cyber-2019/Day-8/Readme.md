## Q.1 What port is SSH running on?

--> got the port number from hint 

Ans : 65534

-----

## Q.2 _Find_ and run a file as _igor_. Read the file /home/igor/flag1.txt

--> i found the .bash_history file in holly's home directory 

![Pasted image 20210723140447.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-8/Attachments/Pasted%20image%2020210723140447.png)

--> so i did the same and get the flag 

```c
touch test
find test -exec cat /home/igor/flag1.txt \
```

-----

## Q.3 Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?

--> i tried this command to find SUID files which can be run as root 

```c
`find / -user root -perm -4000 -exec ls -ldb {} \;`
```

--> and i found some files but i found system-control file useful !

![Pasted image 20210723143125.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-8/Attachments/Pasted%20image%2020210723143125.png)

--> so i run that file and got the root flag !

![Pasted image 20210723143237.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-8/Attachments/Pasted%20image%2020210723143237.png)

-----


