.PHONY: install run dev down logs shell clean

install:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Dependencies Installed. Activate venv with: source venv/bin/activate"

run:
	docker compose up --build

dev:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f api

shell:
	docker compose exec api bash

clean-venv:
	rm -rf venv
	@echo "venv deleted"

clean-all: clean clean-venv
	@echo "All cleaned"

clean:
	docker compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Done Cleaning"
