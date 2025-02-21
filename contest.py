# url = "https://codeforces.com/api/contest.list"  # 替换为实际的 URLimport json
# url = "https://ac.nowcoder.com/acm/calendar/contest"
import json, os, requests
from time import sleep
from datetime import datetime, timezone, timedelta
from colorama import init, Fore

# 初始化 colorama
init(autoreset=True)

def convert_timestamp_to_beijing(timestamp):
    beijing_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    print(f"{Fore.CYAN}[DEBUG] Original timestamp: {timestamp}, Beijing time: {beijing_time}")
    return beijing_time

def get_nowcoder_contests():
    url = "https://ac.nowcoder.com/acm/calendar/contest"  # 替换为实际的 URL
    print(f"{Fore.GREEN}[DEBUG] Fetching NowCoder contests from {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{Fore.RED}[DEBUG] Failed to fetch contest data (Status Code: {response.status_code})")
        return []

    contests = response.json().get("data", [])
    print(f"{Fore.GREEN}[DEBUG] Received {len(contests)} contests from NowCoder API")
    filtered_contests = []
    now = convert_timestamp_to_beijing(datetime.now(timezone.utc).timestamp()).strftime('%Y-%m-%d')
    print(f"{Fore.GREEN}[DEBUG] Current date (Beijing time): {now}")
    for contest in contests:
        start_time = convert_timestamp_to_beijing(contest["startTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        duration_time = (contest["endTime"] - contest["startTime"]) / 1000
        print(f"{Fore.CYAN}[DEBUG] Contest ID: {contest['contestId']}, Start Time: {start_time}, Duration: {duration_time} seconds")
        if start_time < now:
            print(f"{Fore.YELLOW}[DEBUG] Skipping contest {contest['contestId']} as it starts before today")
            continue
        contest_info = {
            "id": contest["contestId"],
            "name": contest["contestName"],
            "startTime": start_time,
            "type": contest["ojName"],
            "phase": "before",
            "durationSeconds": str(timedelta(seconds=duration_time)),
        }
        filtered_contests.append(contest_info)
        print(f"{Fore.GREEN}[DEBUG] Added contest to filtered list: {contest_info}")

    return filtered_contests

def get_codeforces_contests():
    url = "https://codeforces.com/api/contest.list"  # 替换为实际的 URL
    print(f"{Fore.GREEN}[DEBUG] Fetching Codeforces contests from {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{Fore.RED}[DEBUG] Failed to fetch contest data (Status Code: {response.status_code})")
        return []

    contests = response.json().get("result", [])
    print(f"{Fore.GREEN}[DEBUG] Received {len(contests)} contests from Codeforces API")
    filtered_contests = []

    for contest in contests:
        if contest["phase"] != "BEFORE":
            print(f"{Fore.YELLOW}[DEBUG] Skipping contest {contest['id']} as it is not in 'BEFORE' phase")
            continue

        start_time = convert_timestamp_to_beijing(contest["startTimeSeconds"]).strftime('%Y-%m-%d %H:%M:%S')
        duration_time = contest["durationSeconds"]
        print(f"{Fore.CYAN}[DEBUG] Contest ID: {contest['id']}, Start Time: {start_time}, Duration: {duration_time} seconds")
        contest_info = {
            "id": contest["id"],
            "name": contest["name"],
            "startTime": start_time,
            "type": contest["type"],
            "phase": contest["phase"],
            "durationSeconds": str(timedelta(seconds=duration_time)),
        }
        filtered_contests.append(contest_info)
        print(f"{Fore.GREEN}[DEBUG] Added contest to filtered list: {contest_info}")

    return filtered_contests

def save_to_json(contests, filename="contests.json"):
    desktop_path = os.path.join(os.path.expanduser('~'), "desktop/")
    file_path = os.path.join(desktop_path, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            existing_contests = json.load(f)
        print(f"{Fore.GREEN}[DEBUG] Loaded {len(existing_contests)} existing contests from file")
    except (FileNotFoundError, json.JSONDecodeError):
        existing_contests = []
        print(f"{Fore.YELLOW}[DEBUG] No existing contests file found, starting with an empty list")

    existing_ids = {contest['id'] for contest in existing_contests}
    new_contests = [contest for contest in contests if contest['id'] not in existing_ids]
    print(f"{Fore.GREEN}[DEBUG] Found {len(new_contests)} new contests to add")

    existing_contests.extend(new_contests)
    existing_contests.sort(key=lambda x: datetime.fromisoformat(x['startTime']))
    print(f"{Fore.GREEN}[DEBUG] Total contests after sorting: {len(existing_contests)}")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_contests, f, indent=4, ensure_ascii=False)
    print(f"{Fore.GREEN}[DEBUG] Saving contests to {file_path}")

if __name__ == "__main__":
    print(f"{Fore.GREEN}[DEBUG] Starting contest fetching process")
    cf_contests = get_codeforces_contests()
    if cf_contests:
        save_to_json(cf_contests)
    else:
        print(f"{Fore.YELLOW}[DEBUG] No ongoing or upcoming Codeforces contests found.")
    nc_contests = get_nowcoder_contests()
    if nc_contests:
        save_to_json(nc_contests)
    else:
        print(f"{Fore.YELLOW}[DEBUG] No ongoing or upcoming NowCoder contests found.")
    print(f"{Fore.GREEN}Done!!\n\n\n")
    input()

# import json
# import requests
# import os
# from datetime import datetime,timezone,timedelta
#
# def convert_timestamp_to_beijing(timestamp):
#     beijing_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone(timezone(timedelta(hours=8)))
#     return beijing_time
#
# def get_nowcoder_contests():
#     url = "https://ac.nowcoder.com/acm/calendar/contest"
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("Failed to fetch contest data")
#         return []
#
#     contests = response.json().get("data", [])
#     filtered_contests = []
#     now = convert_timestamp_to_beijing(datetime.now(timezone.utc).timestamp()).strftime('%Y-%m-%d')
#     for contest in contests:
#         d = convert_timestamp_to_beijing(contest["startTime"] / 1000).strftime('%Y-%m-%d')
#         durationTime = (contest["endTime"] - contest["startTime"]) / 1000
#         # print(timedelta(seconds=durationTime))
#         if d < now:
#             continue
#         contest_info = {
#             "id": contest["contestId"],
#             "name": contest["contestName"],
#             "startTime": convert_timestamp_to_beijing(contest["startTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
#             "type": contest["ojName"],
#             "phase": "before",
#             "durationSeconds": timedelta(seconds=durationTime),
#         }
#         filtered_contests.append(contest_info)
#
#     return filtered_contests
#
# def get_codeforces_contests():
#     url = "https://codeforces.com/api/contest.list"
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("Failed to fetch contest data")
#         return []
#
#     contests = response.json().get("result", [])
#     filtered_contests = []
#
#     for contest in contests:
#         if contest["phase"] != "BEFORE":
#             continue
#
#         contest_info = {
#             "id": contest["id"],
#             "name": contest["name"],
#             "startTime": convert_timestamp_to_beijing(contest["startTimeSeconds"]).strftime('%Y-%m-%d %H:%M:%S'),
#             "type": contest["type"],
#             "phase": contest["phase"],
#             "durationSeconds": convert_timestamp_to_beijing(contest["durationSeconds"]).strftime('%H:%M:%S'),
#         }
#         filtered_contests.append(contest_info)
#
#     return filtered_contests
#
#
# def save_to_json(contests, filename="contests.json"):
#     desktop_path = os.path.join(os.path.expanduser('~'), "desktop/")
#     file_path = os.path.join(desktop_path, filename)
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             existing_contests = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         existing_contests = []
#
#     existing_ids = {contest['id'] for contest in existing_contests}# 过滤掉重复的比赛，只保留新的比赛
#     new_contests = [contest for contest in contests if contest['id'] not in existing_ids]
#
#     existing_contests.extend(new_contests)
#     existing_contests.sort(key=lambda x: datetime.fromisoformat(x['startTime']))
#
#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump(existing_contests, f, indent=4, ensure_ascii=False)
#     print(f"Contests saved to {filename}")
#
# if __name__ == "__main__":
#     cf_contests = get_codeforces_contests()
#     if cf_contests:
#         save_to_json(cf_contests)
#     else:
#         print("No ongoing or upcoming contests found.")
#     nc_contests = get_nowcoder_contests()
#     if nc_contests:
#         save_to_json(nc_contests)
#     else:
#         print("No ongoing or upcoming contests found.")
#     # print(nc_contests)
