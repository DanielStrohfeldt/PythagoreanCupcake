class User:
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.item_list = []
        self.shared = {} # name : User(name, password) 


    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        try: 
            self.item_list.remove(item)
        except:
            print("Item not in list {} : {}".format(item, self.item_list))

    def show(self, name=None):
        if name:
            print(self.shared[name].item_list)
        else: 
            print(self.item_list)

    def share(self, name, user):
        self.shared[name] = user

    def revoke(self, name):
        self.shared.pop(name ,None)

