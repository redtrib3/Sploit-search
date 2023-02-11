# https://github.com/redtrib3
# Python Libraries used: requests,pandas,colorama,argparse.

try:
    import requests
    import pandas as pd
    from colorama import Fore, Back, Style, init
    import argparse
except ImportError:
    Print("Module Requirements Not satisfied.\n > pip install -r requirements.txt")


# ARGPARSE 
epi ='''Examples:
            1. python3 sploit.py -s wordpress
            2. python3 sploit.py --search "vsftpd 3.3"
            3. python3 sploit.py -s "sudo 1.8.2" -o sudo_exps.txt)
    '''

# formatter_class helps in raw formatting of text in RAW format(epilog)
parser = argparse.ArgumentParser(description='Search and Find Exploits Easily.',formatter_class=argparse.RawTextHelpFormatter,epilog = epi)
parser.add_argument('-o','--output',metavar="<file_name>",type=str,help="Save the Output to a file(.txt/.csv)")
parser.add_argument('-s','--search',metavar="<keyword>",type=str,required=True,help="Keyword to search for")
args = parser.parse_args()



#function to create Border around the output

def borderit(text):
    text = text.splitlines()
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    print('+'+'-'*colwidth+'+')
    for s in text:
        print('|'+s+'  |')
    print('+'+'-'*colwidth+'+')



# Get the Raw data from Github (/offensive-security fork)

r = requests.get("https://raw.githubusercontent.com/blackorbird/exploit-database/master/files_exploits.csv")
data = r.text
data = data.split('\n')

# User-Aurguments

if args.search:
    q = args.search
    q = q.lower()

#initialise colorama with autoreset 
init(autoreset=True)

# Make a list of each row in csv
lst = []
count=0

for i in data:
    if q in i.lower():
        count+=1
        lst.append(i.split(','))

# create a pandas df
df = pd.DataFrame(lst,columns=['id','file','description','date','author','type','platform','port']) 
del df['id']
if not df.empty:
    borderit(str(df))

if count > 20:
    print(Fore.YELLOW+"\n[!] More than 20 exploits Found.]\n[~] TIP:""Use -o,--output to Save table into a File .")
 
print(Fore.GREEN + f"\n[i]  {count} Exploits found . ")



#Save the data into a file
if args.output:
    path = args.output
    with open(path,'w',encoding='utf-8') as file:
        dfAsString = df.to_string(index=False)
        file.write(dfAsString)

    print(Fore.GREEN+f"[+] Data Saved as '{path}' successfully.")

    
# Thank you for reading the code! cheers and happy Hacking! <3
