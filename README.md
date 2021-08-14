[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
# Sploit Exploit Searcher
  Search for Exploits easily without any need of a local database.
  This cli-app uses some webscraping in order to find the exploit .

## But why?
  Try searching for exploits of wordpress, or any other publicily vulnerable services.  
  I use this script during CTF's in order to find known exploits.

## ~ Syntax 
  ```
  mark@Kali:~$ python3 sploit.py --help
    usage: sploit.py [-h] [-o <file_name>] -s <keyword>

      Search and Find Exploits Easily.

      optional arguments:
        -h, --help            show this help message and exit
        -o <file_name>,  --output <file_name>
                           Save the Output to a file(.txt/.csv)
        -s <keyword>,   --search <keyword>
                         Keyword to search for

      Examples:
            1. python3 sploit.py -s wordpress
            2. python3 sploit.py --search "vsftpd 3.3"
            3. python3 sploit.py -s "sudo 1.8.2" -o sudo_exps.txt)

  ```
  
 ## Sample Output:
 ```
 elon@ubuntu:~$ py sploit.py --search vsftpd
+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                file                                        description        date                     author    type  platform port  |
|0         exploits/linux/dos/5814.pl  "vsftpd 2.0.5 - 'CWD' (Authenticated) Remote M...  2008-06-14        "Praveen Darshanam"     dos     linux       |
|1         exploits/linux/dos/16270.c                 "vsftpd 2.3.2 - Denial of Service"  2011-03-02  "Maksymilian Arciemowicz"     dos     linux       |
|2      exploits/windows/dos/31818.sh  "vsftpd 2.0.5 - 'deny_file' Option Remote Deni...  2008-05-21              "Martin Nagy"     dos   windows       |
|3      exploits/windows/dos/31819.pl  "vsftpd 2.0.5 - 'deny_file' Option Remote Deni...  2008-05-21        "Praveen Darshanam"     dos   windows       |
|4      exploits/unix/remote/17491.rb  "vsftpd 2.3.4 - Backdoor Command Execution (Me...  2011-07-05                 Metasploit  remote      unix       |
|5  exploits/multiple/remote/49719.py          "vsftpd 3.0.3 - Remote Denial of Service"  2021-03-29                    xynmaps  remote  multiple       |
|6      exploits/unix/remote/49757.py        "vsftpd 2.3.4 - Backdoor Command Execution"  2021-04-12                 HerculesRD  remote      unix       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[i]  7 Exploits found .
 
 ```
  ## ThankYou ! Happy Hacking
 [![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com) 
