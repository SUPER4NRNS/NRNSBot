import re

group_id = "quit1234567890"
match = re.search(r"\d+", group_id)
if match:
    group_id = match.group(0)
    print(group_id)
