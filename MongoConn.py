from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import os

# ------Configuración---------
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


