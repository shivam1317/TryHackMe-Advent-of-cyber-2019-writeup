--> i got  this on port `3000` 

![[Pasted image 20210829035241.png]]

--> let's use `dirsearch` to brute force the directories 

### disearch results

```c
[03:53:55] Starting: 
[03:53:59] 302 -   27B  - /ADMIN  ->  /home
[03:53:59] 302 -   27B  - /Admin  ->  /home
[03:53:59] 302 -   27B  - /admin  ->  /home
[03:54:01] 301 -  179B  - /assets  ->  /assets/
[03:54:04] 301 -  173B  - /css  ->  /css/
[03:54:09] 302 -   28B  - /home  ->  /login
[03:54:09] 302 -   28B  - /Home  ->  /login
[03:54:11] 301 -  171B  - /js  ->  /js/
[03:54:12] 200 -    2KB - /login
[03:54:12] 200 -    2KB - /Login
[03:54:12] 302 -   28B  - /logout  ->  /login
[03:54:21] 200 -    2KB - /sysadmin
[03:54:21] 200 -    2KB - /SysAdmin
```

--> most directories are redirecting us to `/home` but `/sysadmin` looks interesting so Let's go in that directory 

--> and we got admin login page 

![[Pasted image 20210829035631.png]]

--> but we don't have username and password 

--> So i checked source code and i found this comment !

![[Pasted image 20210829035855.png]]

--> So let's check their github repo 

![[Pasted image 20210829035935.png]]

--> and now we have credentials : `admin:defaultpass`

### Q.3 What do you have to take to the 'partay'

![[Pasted image 20210829040208.png]]

==> Ans : eggnog 

-----