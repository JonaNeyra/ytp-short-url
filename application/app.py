import redis
from flask import Flask

from infrastructure import RedisDb, UrlRedisHandler

app = Flask(__name__)

redis_client = RedisDb().client
url_db_handler = UrlRedisHandler(redis_client)

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
