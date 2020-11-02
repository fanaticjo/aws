import redis
import json
from caching.secrets.getSecet import redisSecret
import os

redis_url=redisSecret(os.environ['redis'])
client=redis.Redis.from_url(redis_url)
