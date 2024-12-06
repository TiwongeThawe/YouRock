# Define variables
PYTHON = python
PIP = pip
APP = app:app  # Flask app reference (module:function)
PORT = 8000  # Default port

# Default target: install dependencies and run the app
all: install run

# Install dependencies from requirements.txt
install:
	$(PIP) install -r requirements.txt

# Run the app with Waitress
run:
	waitress-serve --port=$(PORT) $(APP)

# Clean up the environment (optional)
clean:
	rm -rf __pycache__
	rm -f *.pyc
	rm -f *.log

# Freeze dependencies into requirements.txt
freeze:
	$(PIP) freeze > requirements.txt