from finman.commands import CreateUser, CreateExpense
from finman.db import MongoHelper
from pymongo import MongoClient
from datetime import datetime, timedelta
import unittest


class BaseCommandUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        server = 'localhost'
        port = 27017
        cls._db = 'finmantest'
        cls._mongoclient = MongoClient(server, port)
        cls._mongohelper = MongoHelper(server, port, cls._db)

        
    @classmethod
    def tearDownClass(cls):
        cls._mongoclient.drop_database(cls._db)



class WhenCallingCreateUserCommand(BaseCommandUnitTest):

        
    def test_a_user_is_created(self):
        createUserCommand = CreateUser(self._mongohelper)
        email = 'some_email@gmail.com'
        name = 'Some name'
        password = 'pwd123'
        createUserCommand(name, email, password)
        users = self._mongohelper.get_collection('users')
        user_from_db = users.find_one()
        self.assertEqual(user_from_db['name'],  name)
        self.assertEqual(user_from_db['email'], email)



class WhenCallingCreateExpenseCommand(BaseCommandUnitTest):

    def test_a_expense_is_created(self):
        createExpenseCommand = CreateExpense(self._mongohelper)
        amount = 10.0
        dateof  = datetime.utcnow()
        expenses = self._mongohelper.get_collection('expenses')
        createExpenseCommand(amount, dateof)
        expense_from_db = expenses.find_one()
        self.assertEqual(expense_from_db['amount'], amount)
        self.assertAlmostEqual(expense_from_db['dateof'], dateof, delta=timedelta(seconds=1))
        
