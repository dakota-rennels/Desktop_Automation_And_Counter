import os
import random
import time
import schedule

REPO_PATH = os.getcwd()  # Automatically detect the repo folder
COUNTER_FILE = os.path.join(REPO_PATH, 'counter.txt')

COMMIT_MESSAGE_TEMPLATE = 'Auto-increment counter to {counter}'

# Increment the counter and push changes
def commit_and_push():
    # Increment the counter
    with open(COUNTER_FILE, 'r+') as f:
        current_value = int(f.read().strip())
        new_value = current_value + 1
        f.seek(0)
        f.write(str(new_value))
        f.truncate()

    # Git commands
    os.system(f'cd {REPO_PATH} && git add {COUNTER_FILE}')
    os.system(f'cd {REPO_PATH} && git commit -m \"{COMMIT_MESSAGE_TEMPLATE.format(counter=new_value)}\"')
    os.system(f'cd {REPO_PATH} && git push')

if __name__ == "__main__":
    commit_and_push()