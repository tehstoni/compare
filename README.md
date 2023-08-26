# compare
python script to parse the output of the hashcat potfile and the dump of the ntds.dit file to match usernames and hashes to the cracked password.


usage:

general 
```bash
python3 compare.py hashcat.potfile ntds.txt
```

output to file
```bash
python3 compare.py hashcat.potfile ntds.txt > matched.txt
```
