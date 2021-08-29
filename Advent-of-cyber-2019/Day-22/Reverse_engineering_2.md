# If-else conditions 

-----

--> so Let's start by using radare2 using command `r2 -d if1`

--> and we have to run this command also : `e asm.syntax=att` to set the syntax for assembly

--> now let's analyse the program using `aaa`

--> after that we will search for main function using `afl | grep main` command 

--> and we got the main function 

![[Pasted image 20210814111644.png]]

--> so Let's read that function using command `pdf@main`

![[Pasted image 20210814111716.png]]

--> and there are 2 jump instructions `jge` is for jump if value is greater than or equal to given value and `jmp` stands for unconditional jump 

--> first of all we will set the breakpoints at `jge` and `jmp`

![[Pasted image 20210814111843.png]]

--> now execute the program using `dc` and it will hit the breakpoint 

![[Pasted image 20210814111925.png]]

--> so we can see the `cmpl` is the comparing the value of `var_4h` and `eax` register so Let's read the value of them

--> to see the value of register we use `dr` command 

![[Pasted image 20210814112053.png]]

--> and it contains `3`

--> to see the value of `var_4h` we use `px @rbp-0x4 (which is address of var_4h)`

![[Pasted image 20210814112240.png]]

--> and we can see it contains `4`

--> so `jge` means if eax register is greater than or equal to the var_4h then it will jump but 3 is not greater than or equal to 4 so it will move to the next instruction 

--> so let's goto next instruction using `ds` command and we can see it's adding 5 into the `var_8h` so let's analyse this also 

![[Pasted image 20210814112812.png]]

--> let's do `px @rbp-0x8` to see the value of `var_8h`

![[Pasted image 20210814112954.png]]

--> so let's go to next instruction and analyse it again !

![[Pasted image 20210814113034.png]]

--> and we can see the value of `var_8h` changed to 8 means 5 has been added into it 

-----