from pymongo import MongoClient

def connect_monogo():
    client = MongoClient("mongodb+srv://Nathan:Activeatlas3@hackumbc-nathenael-uhvrd.gcp.mongodb.net/test?retryWrites=true&w=majority")
    database = client.get_database('HackUMBC19')
    collection = database['Predection']
    print(collection.find_one({}))
    return database

connect_monogo()
