import pickle
from initdata import db

dbfile = open('people-pickle','wb')
pickle.dump(db, dbfile)
dbfile.close()
