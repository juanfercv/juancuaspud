APP_NAME=cuaspud
STACK_FILE=stack.yml
STACK_NAME=ecuador

build:
	docker build -t $(APP_NAME):1.0.1 .

deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

logs:
	docker service logs -f $(APP_NAME)_$(APP_NAME)

rm:
	docker stack rm $(APP_NAME)

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy