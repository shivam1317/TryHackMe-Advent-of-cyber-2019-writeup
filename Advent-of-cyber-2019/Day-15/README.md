# LFI 
-----

--> we got one website which is representing some notes 

![Pasted image 20210811142418.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811142418.png)

--> then i saw the source code 

![Pasted image 20210811142501.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811142501.png)

--> found on js script which was adding filename in `get-file` directory and displaying it !

--> so there is a chance for doing LFI 

--> so i encoded my payload to URL and then send it after /get-file directory 

![Pasted image 20210811142707.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811142707.png)

--> and boom we have /etc/passwd file !

![Pasted image 20210811142733.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811142733.png)

--> so let's see /etc/shadow file 

![Pasted image 20210811142859.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811142859.png)

--> so Let's crack this hash 

![Pasted image 20210811143023.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811143023.png)

--> and we have password !

------

## SSH

--> ssh is open on this machine so Let's login !

![Pasted image 20210811143146.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811143146.png)

--> and we got the flag !

![Pasted image 20210811143254.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-15/Attachments/Pasted%20image%2020210811143254.png)

-----
