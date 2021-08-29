# Reverse engineering 
-----

--> first of all we have to download the radare2 framework which is useful for reading binaries and assembly code 

--> after downloading radare2 first execute the file which we have to run 

`./file1`

![Pasted image 20210813135928.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813135928.png)

--> as we can see it's adding a and b and giving the value of c

-------

## Radare 2 

--> now Let's analyse it using radare2 

--> command : 

```c
r2 -d ./file1
```

![Pasted image 20210813140101.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813140101.png)

--> now first we analyse it by writing `aa`

--> we got the main function using `afl | grep main`

--> here `afl` lists all function but we are interested only in main function 

![Pasted image 20210813140253.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813140253.png)

--> we can see the assembly code for main function using `pdf@main` command where pdf stands for `print disassembly function`

![Pasted image 20210813141450.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813141450.png)

----

## Breakpoint

--> breakpoint is the place when program stops executing and we can analyse it 

--> here we will set the breakpoint at 4th line which is `mov dword [var_ch], 4`

--> to set the breakpoing use `db <address>` in this case `db 0x00400b55`

--> after that do `pdf@main` to check whether break point set or not 

--> and we can see the breakpoint is set

![Pasted image 20210813141757.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813141757.png)

--> now we can run the program using `dc` and we can see the program stopped at the breakpoint 

-------

## Analysing variable value 

--> and we will display the main function again 

![Pasted image 20210813142119.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813142119.png)

--> to see the value of the variable we use the `px@<address>` and in this case we want to see the value of `var_ch` and it's address is `rbp-0xc`

![Pasted image 20210813143350.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813143350.png)

--> now we will goto next instruction using `ds` and then we will again see the value of `var_ch`

--> now we can see the value is 4 in variable `local_ch`

![Pasted image 20210813143706.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813143706.png)

--> Let's do ds again and check the value but this time we will give the address of `local_8h` variable 

--> and we can see we got the value 5 in variable `local_8h`

![Pasted image 20210813143836.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813143836.png)

-------

## Analysing register value 

--> now we want to see the values of registers so for that we use `dr` command 

![Pasted image 20210813144353.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813144353.png)

--> Let's run `ds` and then again run `dr`  

--> we can see that the value of `rdx` changed to 4 

![Pasted image 20210813144541.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813144541.png)

--> Let's do it again 

--> and now the value of `rax` changed to 5 

![Pasted image 20210813144622.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813144622.png)

--> so now we  expect the value of `rax` should be 9 from this expression 

![Pasted image 20210813144735.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813144735.png)

--> so Let's try it !

--> and the value is changed !

![Pasted image 20210813144855.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-21/attachments/Pasted%20image%2020210813144855.png)

-------
