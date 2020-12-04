from pydustry import Server

# Functions
def stats():
    pass


# Definitions
server = Server('localhost')
run = True

try:
    print("Console is ready to use, type help for more info.")
    while run:
        user_input = input()
        if user_input == 'stop':
            print("Stopping controller")
            run = False
        elif user_input == 'help':
            print(open('help.txt', 'r').read())
        elif user_input is not None:
            server.send_command(user_input)
        else:
            print('Blank message!')
except KeyboardInterrupt:
    print("\nStopping controller - Keyboard Interrupt")
    exit(0)
except ConnectionRefusedError:
    print('\nFailed to connect to Mindustry server')
    try:
        ping = server.ping()
    except ConnectionError:
        ping = 10000
    print(f'Ping: {ping}')
    if ping < 100:
        print("Retrying to connect")
        server.send_command(user_input)
    else:
        print('Server is not running or wrong port is set')
        exit(3)