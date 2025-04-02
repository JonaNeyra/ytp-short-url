## Acortador de URLs

### Dependencias

- Docker & Docker Compose
- Curl o un Cliente para hacer peticiones

Se puede levantar el proyecto de manera sencilla, con este comando:

```bash
docker-compose up --build -d
```

En el proyecto en la carpeta `request` se puede visualizar el ejemplo con url existente.
Ejecuta el request como gustes, aquí se muestra como sería via cURL:

```bash
curl --request POST \
  --url http://localhost:8081/shorting_url \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
	"url": "http://localhost:8081/ping_to_redis"
}'
```

Si es más comodo puede usar un cliente y añade en un request `POST` este cuerpo:

URL: http://localhost:8081/shorting_url
```json
{
	"url": "http://localhost:8081/ping_to_redis"
}
```

Una vez generada la url corta, puedes hacer uso de esta