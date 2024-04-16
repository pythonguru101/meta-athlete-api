POSTGRES_DB=meta_athelete
POSTGRES_USER=meta_athelete

.PHONY: start

start:
	docker-compose up --build -d
	sleep 10  # wait for services to start
	docker exec -i $$(docker-compose ps -q meta_postgres) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) < init.sql
