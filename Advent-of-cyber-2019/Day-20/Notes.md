# SSH
----

--> found ssh running on port `4567` using nmap 

![[Pasted image 20210813125306.png]]

--> we have to find the password for `sam` but we don't have any other resource so brute force is the only way 

--> and i found the password using hydra !

![[Pasted image 20210813125511.png]]

--> so Let's login !

--> and we got our first flag !

![[Pasted image 20210813125637.png]]

-----

## Privesc 

--> i found that `cleanup.sh` script is running on every minute using `pspy`  
so Let's read that file !

![[Pasted image 20210813130837.png]]

--> so i added netcatmkfifo reverse shell and saved that file 

![[Pasted image 20210813130906.png]]

--> now just start our listener 

```c
nc -lvnp 4444
```

--> and i got the shell after 1 minute !

![[Pasted image 20210813130955.png]]

--> and i found the flag2 in `/home/ubuntu` 

![[Pasted image 20210813131104.png]]

-------