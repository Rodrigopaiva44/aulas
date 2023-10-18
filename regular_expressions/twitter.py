import re


# url = input("URL: ").strip()
# print(url)  # https://twitter.com/manoabelha


# username = url.replace("https://twitter.com/")
# print(f"Username: {username}")

# And we a done for today? of course no.
# Theres a bunch of problems here. So lets use REGEX

# re.sub(patter,repl, string, count=0, flags=0)

url = input("URL:").strip()

# Careful with ".com" (. means any char)
# Some use https, other http (?)
# Some use "www." ( (www\.)? )
# the https:// is optional ( (https?://)? )
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# search for user's url and capture by using () the username
matches = re.search(r"https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: {matches.group(1)}")  # its wrong! Use 2 instead

# We need to especify that we are capturing the group (www\.)? but we dont need
# www. coming back, so use (?:)
if matches := re.search(r"https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
