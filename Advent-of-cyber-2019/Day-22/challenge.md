--> so we have one file named `if2` and we have to find the value of `local_8h` and `local_4h` variables at the ending of main function 

--> so let's start it using `r2 -d if2`

--> and set the syntax using `e asm.syntax=att` and analyse it using `aaa`

--> let's search for main function using `afl | grep main` and we got the main function 

![[Pasted image 20210814114547.png]]

--> let's read the main function using `pdf@main` 

![[Pasted image 20210814114741.png]]

--> we can see it's using `jle` which means less than or equal to so it means if the value of `eax` will less than or equal to `var_4h` then it will jump otherwise it will goto next instruction 

--> so first of all we have to set the breakpoints at both jump instructions 

```c
db 0x00400b65
db 0x00400b6b
```

--> let's check using `pdf@main`

![[Pasted image 20210814115012.png]]

--> ok so we are good to go so let's execute the program using `dc` and it will hit the breakpoint

![[Pasted image 20210814115129.png]]

--> so let's analyse the value of `var_4h` and `eax` register because eax register contains the value of `var_8h`

--> we can see the value of `var_4h` using `px@rbp-0x4`

![[Pasted image 20210814115252.png]]

--> and currently it's 2 so let's see the value of registers also

![[Pasted image 20210814115335.png]]

--> the value of `eax` is 8 

-----

--> so now let's goto next instruction using `ds` and analyse the values 

![[Pasted image 20210814115435.png]]

--> it will add `1` into `var_8h` so the value of `var_8h` should be 9

--> current value is `8`

![[Pasted image 20210814115532.png]]

--> after doing `ds` value is chaned to `9`

![[Pasted image 20210814115608.png]]

--> so we can see the final value of `var_8h` is `9`

--> let's see the value of `var_4h`

![[Pasted image 20210814115655.png]]

--> and the value is `2`

--> and we completed the challenge !

-------