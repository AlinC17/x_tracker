# x_tracker
Device tracker(server)

## Config `.env`
```
SECRET_KEY=<string_secret>
DATABASE_URL=<postgresql | mysql | sqlite> # the container is not properly configured for sqlite 
DEBUG=<False | True>
DADATA_API_KEY=<your_api_key>
USE_LIB=<True | False> # Either to use request api implementation or dadata client python library
USE_JWT=<True | False> # Use JWT Authentication or defaul rest_framework's TokenAuthentication 
```
> Without providing all fields service won't start properly


## Start command
`docker compose up`

> If u don't have a configured nginx for serving static files my advice is to keeb `DEBUG` setting on `False`, whitenoise will be used for serving static content


## Utility paths

- /admin/ > Admin Panel
- /docs/swagger/ > Swaggter ui documentation
- /docs/redoc/ > Redoc documentation
- /docs/schema > JSON schema
