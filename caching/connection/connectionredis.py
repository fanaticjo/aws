import redis
import json

redis_url='redis://rediscluster.91do8p.ng.0001.use1.cache.amazonaws.com:6379'
client=redis.Redis.from_url(redis_url)
