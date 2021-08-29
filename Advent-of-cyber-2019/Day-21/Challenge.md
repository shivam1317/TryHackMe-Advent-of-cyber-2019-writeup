--> so it's challenge time !

--> so we have one file called `challenge1` and we have to find the value of `local_ch , eax and local_4h`

--> so Let's start by analysing the file 

```c
r2 -d ./challenge1
aa
```

--> we got the main function using `afl` 

![Pasted image 20210813150132.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150132.png)

--> now let's read it using `pdf@main` command 

![Pasted image 20210813150253.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150253.png)

--> so this program is multiplying two numbers and then adding them into a variable 

--> so Let's set a breakpoint at 3rd line 

`db 0x00400b51`

--> now check whether it's set or not 

![Pasted image 20210813150420.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150420.png)

--> breakpoint is set so let's analyse the value of the variables

--> as usual at starting the value of `local_ch` is 0

![Pasted image 20210813150527.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150527.png)

--> now let's go to next instruction using `ds` and analyse the value 

--> so now the value is 1

![Pasted image 20210813150626.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150626.png)

--> Let's do it again for another variable 

![Pasted image 20210813150659.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150659.png)

--> now we have to see the value of `local_4h` so we can see it after doing `ds` 3 times which we can see from below instruction 

![Pasted image 20210813150916.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813150916.png)

--> and we can see the value of `local_4h` 

![Pasted image 20210813151005.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813151005.png)

--> and we completed the challenge !

------
