# Install the required dependencies in the virtual environment
install:
	@python3 -m venv venv
	@. venv/bin/activate && python3 -m pip install -r requirements.txt

# Execute the game
run:
	@. venv/bin/activate && python3 -m src.main

# Execute the game without a graphic interface
run-nogui:
	@. venv/bin/activate && python3 -m src.main --no-gui

# Remove the virtual environment and the pycache folder
clean:
	@rm -rf venv/
	@find . -type d -name "__pycache__" -exec rm -rf {} +