import shelve 

db = shelve.open('class-shelve','rb')
for key in db:
    print(key, "=>\n    ", db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
