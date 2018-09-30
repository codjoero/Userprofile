import re


class User:
    def __init__(self, *args):
        self.name = args[0]
        self.username = args[1]
        self.password = args[2]
        self.email = args[3]
        self.age = args[4]
        self.active = False
        self.users = []
        self.user = {}

    def valid_username(self):
            """check that username is not < 4 charaters or equal to name.
            Returns 'True' for check, and 'False' otherwise."""

            if self.username != self.name and len(self.username) >= 4:
                return True
            return False

    def valid_password(self):
        """Check that a password is longer than 4 characters,
        contains uppercase, lowercase, a number and a special character.
        Returns True for all the above and False otherwise.
        """
        rules = [lambda i: any(x.isupper() for x in i),
                lambda i: any(x.islower() for x in i),
                lambda i: any(x.isdigit() for x in i),
                lambda i: any(x for x in i if x in "!@#$%^&*(),./-`~" ),
                lambda i: len(i) >= 4
                ]
        if all(rule(self.password) for rule in rules):
            return True
        return False
    
    def valid_email(self):
        """ Check that user email is a valid format.
        True - for email matching required attributes.
        False otherwise. """
        
        if re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", self.email):
            return True
        return False

    def valid_age(self):
        """ Check that user's age is an integer > 0.
        True For integer > 0, False otherwise """

        if isinstance(self.age, int) and self.age > 0:
            return True
        else:
            return False

    def register_user(self):
        """ Registers a user using: name, username, password, age, email.
        Returns success message with a succesfull registration.
        """
        new_user = dict(
            name = self.name,
            username = self.username,
            password = self.password,
            email = self.email,
            age = self.age,
            )
        self.user.update(new_user)

        if not self.valid_age:
            return 'Please enter the right Age!'
        if not self.valid_email:
            return 'Invalid email! Email should be in the form - johndoe@mail.com'
        if not self.valid_password:
            return 'Password should have uppercase, lowercase, a number\
                    and 4 characters long!'
        if not self.valid_username:
            return 'Username can\'t be the same as your name or less than\
                    4 characters long!'
        else:
            self.users.append(self.user)
            return '{0} registered successfully!'.format(self.username)

    def login_user(self, username, password):
        """ Method logs a user into their account.
        Also changes the value of active to True
        """
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.active = True
                return 'You are logged in now.'
            else:
                return 'Wrong username or password!'

    def get_all_info(self, username, password):
        """Method checks that a valid user is logged in and returns\
        their information on the platform.
        """
        self.active = False
        self.login_user(username, password)
        if self.active:
            return "Name: {0}, Username: {1}, Email: {2}, Age: {3}".format(
                        self.user['name'], 
                        self.user['username'],
                        self.user['email'], 
                        self.user['age']
                        )
        else:
            return 'Wrong username or password!'

