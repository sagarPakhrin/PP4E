import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 3000, 'software')
sue = Person('Sue Jones', 45, 4000, 'hardware')
tom = Manager('Tom Dow', 50, 5000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
