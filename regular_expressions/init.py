email = input("Whats your email? ").strip()

# At the first time we can verify if the email has "@" if not, invalid

if "@" in email:
    print("valid")
else:
    print("invalid")

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")

# What if we wanted to separated the email name and the domain

username, domain = email.split("@")

if username and ("." in domain):  # and domain.endswith(".com")
    print("Valid")
else:
    print("Invalid")
