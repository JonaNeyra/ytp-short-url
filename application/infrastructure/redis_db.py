import redis
import os

class RedisDb:
    def __init__(self):
        self.redis_host = os.getenv("REDIS_HOST", "redis")
        self.redis_port = int(os.getenv("REDIS_PORT", 6379))
        self.client = redis.Redis(host=self.redis_host, port=self.redis_port, decode_responses=True)

class UrlRedisHandler:
    """Cliente para interactuar con Redis."""
    def __init__(self, client=None):
        self.db = RedisDb()
        self.client = self.db.client if client is None else client


    def save_url(self, short_code, long_url):
        self.client.set(short_code, long_url)

    def get_url(self, short_code):
        return self.client.get(short_code)
