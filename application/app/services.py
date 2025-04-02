from domain import generate_short_code


class UrlShortenerSrv:
    """Servicio que resuelve las URLs"""

    def __init__(self, url_db_handler):
        self.db_handler = url_db_handler

    def save(self, long_url):
        """Acorta una URL y la guarda en Redis"""
        short_code = generate_short_code(long_url)
        self.db_handler.save_url(short_code, long_url)
        return short_code

    def resolve(self, short_code):
        """Obtiene la URL original"""
        return self.db_handler.get_url(short_code)
