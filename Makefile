DC = docker compose
APP_FILE = docker_compose/app.yaml
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
STORAGES_FILE = docker_compose/storages.yaml
APP_CONTAINER = main-app


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${env} ${ENV} up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} ${ENV} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest
