import os
import random
import time
import schedule

REPO_PATH = os.getcwd()  # Automatically detect the repo folder
COUNTER_FILE = os.path.join(REPO_PATH, 'counter.txt')

def initialize_counter():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w') as f:
            f.write('0')

def commit_and_push():
    with open(COUNTER_FILE, 'r+') as f:
        current_value = int(f.read().strip())
        new_value = current_value + 1
        f.seek(0)
        f.write(str(new_value))
        f.truncate()

    os.system(f'cd {REPO_PATH} && git add counter.txt')
    os.system(f'cd {REPO_PATH} && git commit -m \"Update counter to {new_value}\"')
    os.system(f'cd {REPO_PATH} && git push')

def schedule_daily_commits():
    random_commits = random.randint(20, 30)
    interval = int(24 * 60 / random_commits)

    print(f"Scheduled {random_commits} commits for today (every {interval} minutes).\")

    for _ in range(random_commits):
        schedule.every(interval).minutes.do(commit_and_push)

if __name__ == "__main__":
    initialize_counter()
    schedule_daily_commits()

    while True:
        schedule.run_pending()
        time.sleep(1)

