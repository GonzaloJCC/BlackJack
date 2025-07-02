# Install the required dependencies in the virtual enviroment
install:
	@python3 -m venv venv
	@. venv/bin/activate && python3 -m pip install -r requirements.txt

# Execute the game
run:
	@. venv/bin/activate && python3 -m src.main


# Remove the virtual enviroment and the pycache folder
clean:
	@rm -rf venv/
	@rm -rf $(find . -path './venv' -prune -o -type d -name "__pycache__" -print)