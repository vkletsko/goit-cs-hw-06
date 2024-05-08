import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

import pymongo


def initialize_database():
    ENV_PATH = Path(__file__).parent / ".env"
    load_dotenv(ENV_PATH)

    try:
        client = MongoClient(f"mongodb://{os.getenv("MONGO_DB_HOST")}:27017/")
        db = client["db-messages"]
        users_collection = db["messages"]

        init_post = [
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": "John Doe",
                "message": "message from John Doe",
            },
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": "Jane Smith",
                "message": "message from Jane Smith",
            },
        ]

        users_collection.insert_many(init_post)
        print("Database initialized successfully!")
    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred: {e}")
    return client


if __name__ == "__main__":
    client = initialize_database()
    db = client["db-messages"]
    collection = db["messages"]
    cats = collection.find()
    for cat in cats:
        print(cat)