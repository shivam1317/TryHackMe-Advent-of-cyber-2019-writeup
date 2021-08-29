## Cryptography
----

==> Symmetric encryption : This type of encryption uses same key to encrypt and decrypt data 

Example : 

using the gpg (default tool for kali linux) we can encrypt or decrypt any file 

```c
gpg -c <filename>
```

![](https://cdn.discordapp.com/attachments/860126060821217280/874715109841334332/unknown.png)

--> here we enter password to decrypt file and then it will generate .gpg file 

```c
gpg -d <filename>
```

![Pasted image 20210810140841.png](https://github.com/shivam1317/Advent-of-cyber-2019-writeup/blob/main/Advent-of-cyber-2019/Day-12/Attachments/Pasted%20image%2020210810140841.png)

------

==> Asymmetric encryption : This type of encryption uses 2 keys to encrypt and decrypt 

Example :

SSH keys uses asymmetric encryption . they use private key and public keys for authentication 

you place your public key to the server and you use your private key to login to the ssh 


To generate a private key we use the following command (8912 creates the key 8912 bits long):

 ```c
 openssl genrsa -aes256 -out private.key 8912
```

To generate a public key we use our previously generated private key:

```c
 openssl rsa -in private.key -pubout -out public.key
 ```

Lets now encrypt a file (plaintext.txt) using our public key:

```c
 openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt
```
 
Now, if we use our private key, we can decrypt the file and get the original message:

```c
 openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt
 ```
 
 -----
 
 ## Challenge
 
 --> we have 3 files so we have to decrypt them so Let's start with note1
 
 ![[Pasted image 20210810142115.png]]
 
 --> i got the passphrase for note1 in hint which was  **25daysofchristmas**
 
 ![[Pasted image 20210810141642.png]]
 
 --> so Let's decrypt second file using private.key 
 
 --> i also got the passphrase for private key in hint which was **hello**
 
 ![[Pasted image 20210810142009.png]]
 
 --> and we got the flag !
 
 ------
