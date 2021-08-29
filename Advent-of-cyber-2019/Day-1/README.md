--> we got this page at port `3000` 

![Pasted image 20210829030430.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-1/Attachments/Pasted%20image%2020210829030430.png)

--> so Let's register and login !

![Pasted image 20210829030557.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-1/Attachments/Pasted%20image%2020210829030557.png)

--> so the instructions say that we have to check the cookies so Let's intercept the request 

--> we have one `authid` parameter and some value in it 

![Pasted image 20210829030748.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-1/Attachments/Pasted%20image%2020210829030748.png)

### Q.1 What is the name of the cookie used for authentication?

==> Ans : authid 

-----

--> so Let's decrypt it !

![Pasted image 20210829031101.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-1/Attachments/Pasted%20image%2020210829031101.png)

--> so here we can see the cookie contains the username which is `hacker` and some random value !

### Q.2 If you decode the cookie, what is the value of the fixed part of the cookie?

==> Ans : v4er9ll1!ss

----

--> So let's add `mcinventory` at the starting of cookie and forward the request because we want to access his account 

--> i just changed cookies from `storage` and then pressed `ctrl+shift+r` to refresh the page and i got access of his account !

![Pasted image 20210829033205.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-1/Attachments/Pasted%20image%2020210829033205.png)


### Q.3 After accessing his account, what did the user mcinventory request?
==> Ans : firewall 

----
