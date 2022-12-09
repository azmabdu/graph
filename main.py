import os
from Node import Node, graph


# Function to display all objects
def display_hashmap() -> None:
    for key, values in graph.items():
        print(key, '-', *values)


# Function to recommend peoplem
def recommendation(user: Node) -> dict:
    i = 1
    hashmap = {}
    for friend1 in graph[user]:
        for friend2 in graph[friend1]:
            hashmap[i] = friend2
            print(f'{i}.', friend2)
            i += 1
    return hashmap


# Function to display subscribers
def subscribers(user: Node) -> dict:
    hashmap = {}
    for num, friend in enumerate(graph[user], 1):
        print(f'{num}. {friend}')
        hashmap[num] = friend
    return hashmap


# Main Function
def main():
    name = str(input('Enter Name: '))
    user = Node(name)
    graph[user] = set()

    # Your Friends
    adam = Node('Adam')
    kristen = Node('Kristen')
    john = Node('John')

    # John's Friends
    sofia = Node('Sofia')
    mateo = Node('Mateo')

    # Add John's Friends
    john.add_friends(sofia, mateo)
    mateo.add_friends(john)
    sofia.add_friends(john)

    # Kristen's Friends
    johnson = Node('Johson')
    jack = Node('Jack')

    # Add Kristen's Friedns
    kristen.add_friends(johnson, jack)
    johnson.add_friends(kristen)
    jack.add_friends(kristen)

    # Adam's Friends
    james = Node('James')
    ezra = Node('Ezra')

    # Add Adam's Friends
    adam.add_friends(james, ezra)
    james.add_friends(adam)
    ezra.add_friends(adam)

    # Music Topic
    music = Node('Music', True)

    # Add Music People
    eminem = Node('Eminem')
    adele = Node('Adele')
    music.add_friends(eminem, adele)

    # Politics Topic
    politics = Node('Politics', True)

    # Add Politics' People
    putin = Node('Putin')
    modi = Node('Modi')
    politics.add_friends(putin, modi)

    # Sport Topic
    sport = Node('Sport', True)

    # Add Sport's People
    ronaldo = Node('Ronaldo')
    nadal = Node('Nadal')
    sport.add_friends(ronaldo, nadal)

    # Suggest friends to follow
    print('1. Adam\n2. Kristen\n3. John')

    friend = int(input('Select Friend: '))
    if friend == 1:
        # Add Adam to user's friends
        user.add_friends(adam)
    elif friend == 2:
        # Add Kristen to user's friends
        user.add_friends(kristen)
    elif friend == 3:
        # Add John to user's friends
        user.add_friends(john)

    os.system('clear')

    # Suggest topics to follow
    print('1. Politics\n2. Sport\n3. Music')

    choice = int(input('Select Topic: '))
    if choice == 1:
        # Add Politics to user's friends
        user.add_friends(politics)
    elif choice == 2:
        # Add Sport to user's friends
        user.add_friends(sport)
    elif choice == 3:
        # Add Music to user's friends
        user.add_friends(music)
    os.system('clear')

    while True:
        os.system('clear')
        # Menu options
        print('1. Subscribers\n2. Subscribe\n3. Unsubscribe')
        choice = int(input('Select: '))

        os.system('clear')

        # Display Subscribers
        if choice == 1:
            subscribers(user)
            input()

            # Subscribe to a person
        elif choice == 2:
            hashmap = recommendation(user)
            subscribe = int(input('Select: '))
            # Add to user's friends
            user.add_friends(hashmap[subscribe])

            # Unsubscribe to a person
        elif choice == 3:
            hashmap = subscribers(user)
            choice = input('Select: ')
            # Remove from user's friends
            user.delete_friends(hashmap[int(choice)])


# Run Main Function
if __name__ == '__main__':
    main()
