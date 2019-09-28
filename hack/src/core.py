from pymongo import MongoClient
import dns

client = MongoClient("mongodb+srv://Nathan:Activeatlas3@hackumbc-nathenael-uhvrd.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


