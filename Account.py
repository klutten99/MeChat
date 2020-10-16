class Account:
    accounts = []

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.accounts.append(self)
