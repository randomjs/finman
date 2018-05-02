from finman.commands import CreateUser
from finman.db import MongoHelper
import unittest


class WhenCallingCreateUserCommand(unittest.TestCase):
    def setUp(self):
        self.mongohelper = MongoHelper('localhost', 72, 'test')
        self.createUserCommand = CreateUser(self.mongohelper)

        
    def test_a_user_is_created(self):
        email = 'some_email@gmail.com'
        name = 'Some name'
        password = 'pwd123'
        self.createUserCommand(name, email, password)
        users = self.mongohelper.get_collection('users')
        user_from_db = users.find_one()
        self.assertEqual(user_from_db.name, name)
        
        
