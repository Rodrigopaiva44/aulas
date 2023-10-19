import re

pattern = re.compile("[a-z]+")  # without/with ^$

print(pattern.search("Hello World"))
print(pattern.search("hello world"))
print(pattern.search("helloworld"))

# The match funcion starts looking at the beginning
print(pattern.match("Hello World"))
print(pattern.match("hello world"))
print(pattern.match("helloworld"))

# 3 lowercase letters
# 3-5 digits
# one symbol
# up to two uppercase characters (optional)

resp = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(resp.search("ahd2331#AJ"))
print(resp.search("abc123456#AB"))