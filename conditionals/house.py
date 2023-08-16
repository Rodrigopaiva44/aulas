name = input("Whats your name? ")

if name == "Rodrigo":
    print("Vila Isabel")
elif name == "David":
    print("Vila Isabel")
elif name == "Vitin":
    print("Cabuçu")
else:
    print("Who?")


if name == "Rodrigo " or name == "David":
    print("Vila isabel")
elif name == "Vitin":
    print("Cabuçu")
else:
    print("Who?")


# using match

match name:
    case "Rodrigo":
        print("Vila Isabel")
    case "David":
        print("Vila Isabel")
    case "Vitin":
        print("Cabuçu")
    # And if the case we did not catch?
    case _:
        print("Who?")


match name:
    case "Rodrigo" | "David":
        print("Vila Isabel")
    case "Vitin":
        print("Cabuçu")
    case _:
        print("Who?")
