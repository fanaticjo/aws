import redis
import json

redis_url='redis://rediscluster:6379'
client=redis.Redis.from_url(redis_url)
