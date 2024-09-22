MAIN = main.py
REQUIREMENTS = requirements.txt

.PHONY: install clean run

install:
	python3 -m pip install -r $(REQUIREMENTS)

clean:
	rm -rf __pycache__ *.pyc .tmp

run:
	python3 $(MAIN)

