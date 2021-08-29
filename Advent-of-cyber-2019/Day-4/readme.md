#1.How many visible files are there in the home directory(excluding ./ and ../)?

Ans : 8

-----

#2.What is the content of file5?

Ans : recipes

-----

#3.Which file contains the string ‘password’?

command : grep password *

Ans : file6

-----

#4.What is the IP address in a file in the home folder?

command : egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" *

Ans : 10.0.0.05

-----

#5.How many users can log into the machine?

command : cat /etc/passwd | grep "/bin/bash" | wc -l

Ans : 3

-----

#6.What is the sha1 hash of file8?

command : sha1sum file8

Ans : fa67ee594358d83becdd2cb6c466b25320fd2835

-----

#7.What is mcsysadmin’s password hash?

Ans : $6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/

-----