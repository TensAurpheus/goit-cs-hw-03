from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.mds

def create_db():
    try:
        db.cats.insert_many([
            {""
                "name": 'Lama',
                "age": 2,
                "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
            },
            {
                "name": 'Liza',
                "age": 4,
                "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
            },
            {
                "name": 'Boris',
                "age": 12,
                "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
            },
            {
                "name": 'Murzik',
                "age": 1,
                "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
            },
        ])

    except Exception as e:
        print(e)

if __name__ == "__main__":    
    print("Database generated!")
    [print(cat) for cat in db.cats.find()]
