# Discord
Automate daily commands for games/discord currency collection/etc

## Get Started

### 1. Install python3
#### Windows
1. Open Powershell
2. type `python3` and hit `<Enter>`
3. On Microsoft Store, select `Get` to download the latest available python3 from the Python Foundation

#### Linux
1. Use package manager to install python3 (apt/yum/etc)

### 2. Download Repo and Unzip

### 3. Install python3 requirements
1. From terminal/Powershell, navigate to the unzipped directory
```
cd <directory>
```
2. Install dependencies
```
python3 -m pip install -r requirements.yml
```

### 4. Create access.secret file with your access token
https://pcstrike.com/how-to-get-discord-token/#:~:text=To%20find%20your%20token%2C%20click,What%20is%20this%3F&text=Right%2Dclick%20the%20value%20on,edit%20value%2C%20then%20copy%20it.

### 5. Fill in desired values for channel id and command to daily.py
Example:
```
"channel_id": "906671688463290420",
"payload": {"content": "!daily"}
```

### 6. Run script
```
python3 daily.py
```