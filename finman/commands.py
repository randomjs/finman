

class MongoCreateCommand:
    
    def __init__(self, mongohelper):
        self._mongohelper = mongohelper

    def _create_document(self, collection_name, new_document):
        collection = self._mongohelper.get_collection(collection_name)
        collection.insert_one(new_document)

        
class CreateUser(MongoCreateCommand):

    def __init__(self, mongohelper):
        super().__init__(mongohelper)

    def __call__(self, name, email, password):
        new_user = { 'name': name, 'email': email, 'password': password }
        self._create_document('users', new_user)



class CreateExpense(MongoCreateCommand):

    def __init__(self, mongohelper):
        super().__init__(mongohelper)

    def __call__(self, amount, dateof):
        new_expense = {'amount': amount, 'dateof': dateof }
        self._create_document('expenses', new_expense)
