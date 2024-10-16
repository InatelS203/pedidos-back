from pymongo import MongoClient
import os

mongo_client = None

def init_db():
    global mongo_client
    
    try:
        mongo_uri = os.getenv('MONGO_URI', 'mongodb+srv://thuliobalbuena:C209@cluster0.u6sph.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        mongo_client = MongoClient(mongo_uri)
        print('Connected to MongoDB')
    except Exception as e:
        print(f'Error connecting to MongoDB: {str(e)}')
        
def get_db():
    global mongo_client
    if not mongo_client:
        init_db()
    return mongo_client['S203']