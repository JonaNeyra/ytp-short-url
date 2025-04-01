import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.StrictRedis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.route('/')
def hello_world():
    try:
        redis_client.ping()
        msg = "Hello YTP! con conexión exitosa a Redis ✅"
    except redis.ConnectionError as e:
        msg = f"❌ Error al conectar a Redis: {e}"
    return msg


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
