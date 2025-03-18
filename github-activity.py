import argparse
import requests
import sys

cmd_args = argparse.ArgumentParser('simple github activity')
cmd_args.add_argument('-u', '--USERNAME', required=True, help='enter the username you want')
args = cmd_args.parse_args()


def get_user_events(username: str):
    try:
        url = f'https://api.github.com/users/{username}/events'
        req = requests.get(url, timeout=10)
        if req.status_code == 200:
            print(f"you were able to connect to ")
            event = req.json()
            return event
        else:
            print(f'{username} does not exist try running again')
    except (requests.ConnectionError, requests.Timeout) as e:
        print(f'the following error {e} occurred ')


def parse_recent_events(username: str, event: list[dict]):
    try:
        for events in event:
            '''check for recently stared repos'''
            if events['type'] == 'WatchEvent':
                print(f"{username} stared {events['repo']['name']}")

            elif events['type'] == 'PushEvent':
                commit = events['payload'].get('commits', [])
                for commits in commit:
                    print(f"{username} committed the message {commits['message']} to {events['repo']['name']}")

            elif events['type'] == "ForkEvent":
                print(f"{username} forked {events['repo']['name']}")

            elif events['type'] == 'IssueEvent':
                print(f"{username} created an issue {events['payload']['issue']['number']}")
    except Exception as e:
        print(f'the following error {e} occurred ')


def main():
    if len(sys.argv) < 2:
        print(f'follow this format to run the script <script_name><username>')
    user = args.USERNAME
    events = get_user_events(user)
    if events:
        print("here are the recent activities")
        parse_recent_events(user, events)
    else:
        print("no recent activities found")


if __name__ == "__main__":
    main()
