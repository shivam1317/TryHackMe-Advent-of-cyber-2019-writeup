#  Amazon s3 buckets 

-----

--> if we know the amazon s3 bucket name and it lacks permission then anyone can read files from that bucket 

--> like in this challenge we have bucket name as  **advent-bucket-one**

--> so the command to list files on any bucket is :

```c
--> just go to this URL 
<bucket-name>.s3.amazonaws.com
```

--> after going to this URL i found this 

![Pasted image 20210811135611.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-14/Attachments/Pasted%20image%2020210811135611.png)

--> so to read this file we just need to go to :

```c
<bucket-name>.s3.amazonaws.com/<filename>
```

--> and you can see the contents of the file 

![Pasted image 20210811135719.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-14/Attachments/Pasted%20image%2020210811135719.png)
