import random

class setPAss:
    def __init__(self, item_mapping=None, bagspace=0):
        self.inventory = []
        self.bagspace = bagspace
        
        if item_mapping:
            self.item_mapping = item_mapping
        else:
            self.item_mapping = {
                1: {"name": 'A'},
                2: {"name": 'b'},
                3: {"name": 'c'},
                4: {"name": 'd'},
                5: {"name": 'e'},
                6: {"name": 'f'},
                7: {"name": 'g'},
                8: {"name": 'h'},
                9: {"name": 'i'},
                10: {"name": 'j'},
                11: {"name": 'k'},
                12: {"name": 'l'},
                13: {"name": 'm'},
                14: {"name": 'n'},
                15: {"name": 'o'},
                16: {"name": 'p'},
            }

    def random_password(self):
        password = []
        x = 0    
        while x < 10:
            item_number = random.randint(1, 16)
            item_name = self.item_mapping[item_number]["name"]
            password.append(item_name)
            self.inventory.append(item_name)
            self.bagspace += 1
            x += 1
        return ''.join(password)

# Testing
passwd_obj = setPAss()
print(passwd_obj.random_password())
