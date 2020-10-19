

class Account:
    accounts = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if self not in self.accounts:
            self.accounts.append(self)

    def __str__(self):
        return self.username + ":" + self.password


def save_accounts(folder):
    pass


def load_accounts(file):
    pass
