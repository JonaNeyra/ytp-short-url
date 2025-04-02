import redis
from flask import Flask, request, jsonify

from domain import generate_short_code
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

@app.route("/shorting_url", methods=["POST"])
def shorting_url():
    data = request.json
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "No URL provided"}), 400

    short_code = generate_short_code(long_url)
    return short_code


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
