import hashlib
import string

BASE62_ALPHABET = string.ascii_letters + string.digits


def base62_encode(num, length=6):
    """
    Convierte un número en una cadena Base62 de longitud fija
    ¿Por qué Base62?
    Simple:
    26 Mayúsculas
    26 Minusculas
    10 Digitos
    """
    base = len(BASE62_ALPHABET)
    encoded = []

    while num:
        num, rem = divmod(num, base)
        encoded.append(BASE62_ALPHABET[rem])

    return ''.join(encoded)[-length:]


def generate_short_code(url, length=6):
    """
    Genera un código corto basado en el hash SHA256 de la URL
    El SHA256 es muy utilizado y seguro
    """
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    numeric_hash = int(url_hash[:10], 16)

    return base62_encode(numeric_hash, length)
