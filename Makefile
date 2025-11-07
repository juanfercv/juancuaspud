# Variables
SERVICE_NAME=holaflask
IMAGE_NAME=holaflask
REGISTRY=ghcr.io
# Cambiar TU_USUARIO por tu usuario de GitHub
GITHUB_USER=juanfercv
FULL_IMAGE=$(REGISTRY)/$(GITHUB_USER)/$(IMAGE_NAME)

.PHONY: build run logs stop rm down rebuild clean run-local build-multi publish test status start check help

# Construir la imagen Docker
build:
	docker build -t $(IMAGE_NAME) .

# Ejecutar el contenedor
run:
	docker run -d -p 5000:5000 --name $(SERVICE_NAME) $(IMAGE_NAME)

# Ver logs del servicio Flask
logs:
	docker logs -f $(SERVICE_NAME)

# Detener el contenedor
stop:
	docker stop $(SERVICE_NAME)

# Eliminar el contenedor
rm:
	docker rm $(SERVICE_NAME)

# Detener y eliminar
down: stop rm

# Reconstruir completamente el servicio
rebuild:
	docker stop $(SERVICE_NAME) || true
	docker rm $(SERVICE_NAME) || true
	docker build -t $(IMAGE_NAME) .
	docker run -d -p 5000:5000 --name $(SERVICE_NAME) $(IMAGE_NAME)

# Limpiar imágenes huérfanas
clean:
	docker system prune -f

# Ejecutar localmente sin Docker
run-local:
	python app.py

# Construir imagen para múltiples plataformas
build-multi:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE_NAME) .

# Publicar en GitHub Packages
publish:
	docker buildx build --platform linux/amd64,linux/arm64 \
		-t $(FULL_IMAGE):latest \
		-t $(FULL_IMAGE):$(shell date +%Y%m%d-%H%M%S) \
		. --push

# Probar que el contenedor funciona correctamente
test:
	@echo "Probando el contenedor..."
	@sleep 3
	@curl -f http://localhost:5000 || echo "Error: El contenedor no responde"

# Ver estado del contenedor
status:
	@docker ps -a --filter name=$(SERVICE_NAME)

# Iniciar todo desde cero (build + run)
start: build run
	@echo "Contenedor iniciado. Prueba: http://localhost:5000"

# Verificar que todo está listo para Git
check:
	@echo "Verificando archivos..."
	@test -f app.py && echo "[OK] app.py" || echo "[ERROR] Falta app.py"
	@test -f Dockerfile && echo "[OK] Dockerfile" || echo "[ERROR] Falta Dockerfile"
	@test -f requirements.txt && echo "[OK] requirements.txt" || echo "[ERROR] Falta requirements.txt"
	@test -f .gitignore && echo "[OK] .gitignore" || echo "[ERROR] Falta .gitignore"
	@test -f .dockerignore && echo "[OK] .dockerignore" || echo "[ERROR] Falta .dockerignore"
	@echo "Verificacion completa!"

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make build       - Construir imagen Docker"
	@echo "  make run         - Ejecutar contenedor"
	@echo "  make start       - Build + Run en un comando"
	@echo "  make logs        - Ver logs del contenedor"
	@echo "  make status      - Ver estado del contenedor"
	@echo "  make test        - Probar que funciona"
	@echo "  make stop        - Detener contenedor"
	@echo "  make down        - Detener + Eliminar contenedor"
	@echo "  make rebuild     - Reconstruir todo"
	@echo "  make clean       - Limpiar imagenes huerfanas"
	@echo "  make check       - Verificar archivos para Git"
	@echo "  make publish     - Publicar en GHCR"
	@echo "  make run-local   - Ejecutar sin Docker"