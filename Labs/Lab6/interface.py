from user import User
class Interface:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def command(self):
        command = input()
        command = command.split()
        if 'add' in command:
            self.add(command)
        elif 'login' in command:
            self.login(command)
        elif 'quit' in command:
            exit()
        elif self.current_user:
            if 'logout' in command:
                self.logout(command)
            elif 'append' in command:
                self.append(command)
            elif 'remove' in command:
                self.remove(command)
            elif 'show' in command:
                self.show(command)
            elif 'share' in command:
                self.share(command)
            elif 'revoke' in command:
                self.revoke(command)
        else:
            print("Invalid Command")

    def add(self, command):
        name = command[1]
        password = command[2]
        if name in self.users:
            print('user exists')
        else:
            self.users[name] = User(name=name, password=password) 
        print(self.users)

    def login(self, command):
        name = command[1]
        password = command[2]
        if self.users[name]:
            if self.users[name].password == password:
                self.current_user = self.users[name]
    
    def logout(self, command):
        self.current_user = None

    def append(self, command):
        self.current_user.add_item(command[1])

    def remove(self, command):
        self.current_user.remove_item(command[1])

    def show(self, command):
        try:
            name = command[1]
            self.current_user.show(name)
        except:
            self.current_user.show()

    def share(self, command):
        name = command[1]
        self.current_user.share(name=name, user=self.users[name])

    def revoke(self, command):
        name = command[1]
        self.current_user.revoke(name=name)
