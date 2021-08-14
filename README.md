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
  
  
  ## ThankYou ! Happy Hacking
 [![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com) 
