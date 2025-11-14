.PHONY: setup install run visualize clean help

# Default Python interpreter
PYTHON := python3
VENV := venv
BIN := $(VENV)/bin

help:
	@echo "Kaprekar's Constant (6174) - Makefile Commands"
	@echo "==============================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make install    - Install dependencies (venv must exist)"
	@echo "  make run        - Run the interactive Kaprekar routine app"
	@echo "  make visualize  - Generate analysis and visualizations"
	@echo "  make clean      - Remove virtual environment and generated files"
	@echo "  make help       - Show this help message"
	@echo ""

setup:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Upgrading pip..."
	$(BIN)/pip install --upgrade pip
	@echo "Installing dependencies..."
	$(BIN)/pip install -r requirements.txt
	@echo ""
	@echo "✓ Setup complete!"
	@echo ""
	@echo "Run 'make run' to start the app or 'make visualize' for analysis"

install:
	@echo "Installing dependencies..."
	$(BIN)/pip install -r requirements.txt
	@echo "✓ Dependencies installed"

run:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi
	@$(BIN)/python app.py

visualize:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi
	@$(BIN)/python visualize.py

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	rm -f kaprekar_6174_analysis.png
	rm -rf __pycache__
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	@echo "✓ Cleanup complete"
