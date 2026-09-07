# method vs @classmethod vs @staticmethod
# method - self, instance method
# @classmethod - cls, class method
# @staticmethod - static method(❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg): # It's an ordinary function, just like the function below.
        return f'LOG: {msg}'

def connection_log(msg): # This one
    return f'LOG: {msg}'

c1 = Connection.create_with_auth('John', '123')
# c1 = Connection()
# c1.set_user('John')
# c1.set_password('123')
print(Connection.log('That is the log message'))
print(c1.user, c1.password)