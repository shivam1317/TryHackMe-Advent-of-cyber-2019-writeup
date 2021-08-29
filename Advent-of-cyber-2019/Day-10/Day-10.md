--> i found the backend server in tips 

![[Pasted image 20210804145133.png]]

--> so i searched for this on metasploit and found many payloads 

--> we will use 8th payload as shown in tips 

![[Pasted image 20210804145255.png]]

--> so first we have to set the options 

![[Pasted image 20210804145505.png]]

--> for TARGETURI i went to the port 80 and found directory 

![[Pasted image 20210804145754.png]]

--> so after setting everything i run the exploit and got the meterpreter shell !

![[Pasted image 20210804145850.png]]

--> i found first flag in /tomcat/webapps/ROOT

![[Pasted image 20210804151325.png]]

--> and also i found santa's ssh creds in his home directory 

![[Pasted image 20210804151513.png]]

--> so Let's login as santa 

![[Pasted image 20210804151538.png]]

--> so here we have 2 lists 

![[Pasted image 20210804151607.png]]

--> Q.1 Who is on line 148 of the naughty list?

![[Pasted image 20210804151717.png]]

--> Q.2 Who is on line 52 of the nice list?

![[Pasted image 20210804151804.png]]

-------