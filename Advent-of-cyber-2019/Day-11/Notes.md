## nmap results 

>PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.2
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 500 OOPS: invalid pasv_address
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.9.3.121
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.2 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 14:6f:fc:4d:82:43:eb:e9:6e:f3:0e:01:38:f0:cb:23 (RSA)
|   256 83:33:03:d0:b4:1d:cb:8e:59:6f:13:14:c5:a2:75:b3 (ECDSA)
|_  256 ec:b1:63:c0:6d:98:fd:be:76:31:cd:b9:78:35:2a:bf (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      20048/tcp   mountd
|   100005  1,2,3      20048/tcp6  mountd
|   100005  1,2,3      20048/udp   mountd
|   100005  1,2,3      20048/udp6  mountd
|   100021  1,3,4      41455/udp   nlockmgr
|   100021  1,3,4      44067/tcp6  nlockmgr
|   100021  1,3,4      44317/tcp   nlockmgr
|   100021  1,3,4      44991/udp6  nlockmgr
|   100024  1          35845/tcp   status
|   100024  1          53498/udp   status
|   100024  1          56829/tcp6  status
|   100024  1          57408/udp6  status
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs_acl 3 (RPC #100227)
3306/tcp open  mysql   MySQL 5.7.28
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.28
|   Thread ID: 3
|   Capabilities flags: 65535
|   Some Capabilities: LongPassword, SwitchToSSLAfterHandshake, InteractiveClient, LongColumnFlag, FoundRows, Speaks41ProtocolOld, SupportsCompression, IgnoreSigpipes, ConnectWithDatabase, ODBCClient, SupportsLoadDataLocal, Support41Auth, DontAllowDatabaseTableColumn, IgnoreSpaceBeforeParenthesis, SupportsTransactions, Speaks41ProtocolNew, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: U&%3\x13\x1C)D"	HxW %qP`\x19\x14
|_  Auth Plugin Name: mysql_native_password
| ssl-cert: Subject: commonName=MySQL_Server_5.7.28_Auto_Generated_Server_Certificate
| Not valid before: 2019-12-10T23:10:36
|_Not valid after:  2029-12-07T23:10:36
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Unix`

-------

## FTP 

--> got one file called file.txt in ftp and it contains

```c
remember to wipe mysql:
root
ff912ABD*
```

------

## NFS

--> in NFS first of all we start with checking for shared files 

```c
showmount -e <ip>
```

--> and i found one directory 

![[Pasted image 20210810133504.png]]

--> so Let's mount it into our local machine using command 

```c
mount <ip>:/<path> <local_machine_path>
```

--> and then we got a file called creds.txt and inside that i got the below text


```c
the password is securepassword123
```

-------

## Mysql 

--> first of all i need to connect to the mysql database remotely using command :

```c
mysql -h <ip> -u <username> -p
```

--> after using credentials as **root:ff912ABD*** i got logged in !

--> after accessing database i got the password !

![[Pasted image 20210810135007.png]]


-------