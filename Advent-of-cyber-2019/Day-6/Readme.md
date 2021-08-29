
### Q.1 What data was exfiltrated via DNS? 

--> In wireshark i got this hash in dns packet 

![Pasted image 20210723114600.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723114600.png)

--> after decoding this hash i got the data : 

![Pasted image 20210723115133.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723115133.png)

Ans : Candy Cane Serial Number 8491

-----

### Q.2 What did Little Timmy want to be for Christmas?

--> i cracked the password of zip file using zip2 john and i got the password :

```c
december
```

--> after extracting the file i got some txt files 

--> we have to write timmy's file as per the question 

![Pasted image 20210723115905.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723115905.png)

Ans : pentester 

----

### Q.3 What was hidden within the file?
--> i got this 2 items in extract data 

![Pasted image 20210723115346.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723115346.png)

--> so first i extracted the image using steghide 

```c
steghide extract -sf Tryhackme.jpg
```

--> i got this txt file in the image 

![Pasted image 20210723115545.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723115545.png)

--> let's read this file 

![Pasted image 20210723115624.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-6/Attachments/Pasted%20image%2020210723115624.png)

--> got this text in file 

Ans : RFC527

-----
