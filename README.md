# SofaWiki-3.9.2-Shell-Upload-open-tickets exploit
<br>

# Overview
<br>
This repository contains an exploit script for a Remote Code Execution (RCE) vulnerability in SofaWiki 3.9.2. The exploit leverages the Open Ticket feature to upload a malicious .phar file and execute arbitrary commands on the target system.



# Exploit Details
<br>

    Exploit Type: Remote Code Execution (RCE)
    Affected Version: 3.9.2
    Vendor Homepage: SofaWiki
    Tested on: Windows XP
    Exploit Author: Chokri Hammedi


    
<br>

# Vulnerability

Authenticated users can upload a .phar webshell through the ticketing system and then execute arbitrary commands by accessing the uploaded shell.


# Usage

```bash
usage: SofaWiki-open-tickets.py <target_url> <username> <password> <cmd> 

```


# POC 

![image](https://github.com/user-attachments/assets/bcace398-023c-4a8c-a8e4-bd1f8651077d)


# Disclaimer

This exploit is intended for educational and research purposes only. It should only be used on systems you own or have explicit permission to test. Unauthorized usage may result in legal consequences.
