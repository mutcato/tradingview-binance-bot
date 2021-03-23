1. cp app/config.example.py app/config.py
2. Set the empty variables in config.py
3. Set ProdSettings or TestSettings at the end of the config.py
4. docker-compose up

for recreate the container:
docker-compose up --force-recreate --build 