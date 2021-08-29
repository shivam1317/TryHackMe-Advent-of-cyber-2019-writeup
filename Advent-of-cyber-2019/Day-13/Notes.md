## Dirsearch results

```c
[14:47:04] Starting: 
[14:47:34] 301 -  150B  - /retro  ->  http://10.10.116.121/retro/
[14:50:05] 301 -  150B  - /Retro  ->  http://10.10.116.121/Retro/
```

------
--> got this page on that directory 

![[Pasted image 20210810150140.png]]

--> found some wordpress files after running dirsearch on /retro 

```c
[15:12:13] Starting: 
[15:12:16] 301 -  161B  - /retro/wp-content  ->  http://10.10.116.121/retro/wp-content/
[15:12:19] 301 -  162B  - /retro/wp-includes  ->  http://10.10.116.121/retro/wp-includes/
[15:12:56] 301 -  159B  - /retro/wp-admin  ->  http://10.10.116.121/retro/wp-admin/
```

--> so i ran wpscan on it !

--> and i found user wade

![[Pasted image 20210810151936.png]]

------

--> found one comment on one post :

```c
parzival
```

![[Pasted image 20210810152512.png]]

--> Let's try it as password !

--> And boom ! we got logged in !

![[Pasted image 20210810152548.png]]

-----

## Wordpress 

--> i tried to change the 404.php and index.php files but i was not able to get the reverse shell 

--> then i realized that it's a windows machine so we have to do something else 

--> then i tried to connect with remmina using RDP and then tried the same creds 

--> and i got logged in into the windows machine !

![[Pasted image 20210811113952.png]]

--> lets read the user.txt 

![[Pasted image 20210811114028.png]]

--> and we got our user flag !

------

## Privesc 

--> we only have one file on desktop named hhupd so i searched for hhupd privilege escalation and found the way to do it so Let's go !

--> first of all right click on that file and do run as administrator 

![[Pasted image 20210811114752.png]]

--> click show more details and then click on show info about publisher's certificate 

![[Pasted image 20210811114836.png]]

--> then click on the link 

![[Pasted image 20210811114907.png]]

--> you will get one error page 

![[Pasted image 20210811115000.png]]

--> then click on the settings icon on right side and then go to file -> save as 

![[Pasted image 20210811115044.png]]

--> save that file in C:/windows/system32 as `*.*` name and then you will find one cmd file 

![[Pasted image 20210811115422.png]]

--> right click on that file and open that file 

![[Pasted image 20210811115606.png]]

--> and boooom we got root !

--> and i got root flag in C:/Users/administrator/root.txt

![[Pasted image 20210811115825.png]]

--> and we got the flag !

![[Pasted image 20210811115929.png]]

-------





