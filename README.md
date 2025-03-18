# Git-hub-user-activity
A simple script that checks the recent events of a git-hub user with the git-hub api was part of the roadmap.sh projects

https://roadmap.sh/projects/github-user-activity

## Features  
- Retrieves recent events for a given GitHub username.  
- Displays actions like starred repositories, commits, forks, and issue creation.  

## Installation  
Ensure you have Python installed, then install the required dependency:  
```bash
pip install requests
```

## Usage  
Run the script with a GitHub username:  
```bash
python script.py -u <GitHub_Username>
```

Example:  
```bash
python script.py -u octocat
```

## Requirements  
- Python 3.x  
- `requests` module

