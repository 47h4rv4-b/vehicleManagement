# from os import environ
# import redis
# from dotenv import load_dotenv
# from pymongo import MongoClient

# load_dotenv()

# #############
# # Mongo Connection
# #############
# mongo_client = MongoClient(environ.get("mongo_uri"))
# db = mongo_client[environ.get("db_name")]


# #############
# # Redis Connection
# #############
# def init_redis_pool():
#     redis_host = environ.get("REDIS_HOST", "localhost")
#     redis_port = int(environ.get("REDIS_PORT", 6379))
#     redis_pass = environ.get("REDIS_PASSWORD")
#     pool = redis.ConnectionPool(
#         host=redis_host, port=redis_port, password=redis_pass, db=0
#     )
#     return pool


# redis_client = redis.Redis(connection_pool=init_redis_pool())
