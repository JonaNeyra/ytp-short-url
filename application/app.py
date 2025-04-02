import redis
from flask import Flask, request, jsonify, redirect

from app import UrlShortenerSrv
from infrastructure import RedisDb, UrlRedisHandler

app = Flask(__name__)

redis_client = RedisDb().client
url_db_handler = UrlRedisHandler(redis_client)
short_srv = UrlShortenerSrv(url_db_handler)

@app.route('/ping_to_redis')
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
        return jsonify({"error": "No proporcionaste la URL"}), 400

    short_code = short_srv.save(long_url)

    return jsonify({"short_url": f"http://localhost:8081/{short_code}"})


@app.route("/<short_url>", methods=["GET"])
def redirect_to_url(short_url):
    long_url = short_srv.resolve(short_url)

    if long_url:
        return redirect(long_url, code=302)

    return jsonify({"error": "No se encontró la ruta"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
