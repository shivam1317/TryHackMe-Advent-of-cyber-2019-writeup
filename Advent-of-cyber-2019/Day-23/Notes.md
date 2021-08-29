--> we have this page and we have to find the santa's password !

![[Pasted image 20210814135701.png]]

--> i run sqlmap on this url and found `log_email` vulnerable 

```
sqlmap -u 'http://10.10.57.140/register.php' --data 'log_email=test@test.com&log_password=hacker&login_button=submit'
```

![[Pasted image 20210814135154.png]]

--> it's time based sql injection so it will take time !

--> after that i got some databases 

![[Pasted image 20210814135611.png]]

--> so Let's look into them !

--> i found the `users` table into `social` database 

![[Pasted image 20210814141019.png]]

--> so Let's see the content of `users` table 

--> after long wait we found columns in users table 

![[Pasted image 20210814141919.png]]

--> and after 15-20 minutes of wait i finally found a emails and password hashes 

![[Pasted image 20210814145026.png]]

--> so Let's crack santa's password !

![[Pasted image 20210814143253.png]]

--> so now we have password so let's login with his account !

----

#### Q. Santa has a secret! Which station is he meeting Mrs Mistletoe in?

--> after login as santa i found one message in inbox 

![[Pasted image 20210814145224.png]]

--> and we found the station name !

-----

==>now we have to get the reverse shell and find the flag !

--> so i tried to upload `php` and `php5` files but it didn't worked so i tried to upload `phtml` file and it worked !

![[Pasted image 20210814145428.png]]

--> so Let's search flag 

--> and i found flag in `/home/user`  

![[Pasted image 20210814145522.png]]

-----