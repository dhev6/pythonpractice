def main():
    network = {}

    print("Social Network Analyser")

    while True:
        user = input("\nEnter person's name(or done): ").strip().title()
        if user.lower() == "done":break

        friends_input = input(f"Enter {user}' friend's(seperated by comas): ")
        friends_set = {f.strip().title() for f in friends_input.split(",") if f.strip()}

        network[user] = friends_set

    if len(network) >= 2:
        names = list(network.keys())
        p1, p2 = names[0], names[1]

        print(f"-------comparing {p1} and {p2}--------")

        mutual = network[p1] & network[p2]
        print(f"Mutual friends: {mutual if mutual else 'None'}")


        suggestions = network[p2] - network[p1]
        suggestions.discard(p1)
        print(f"Suggestions for {p1}(Friend of {p2}): {suggestions}")

main()