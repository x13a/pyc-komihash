.PHONY: venv

NAME    := komihash

venvdir := ./venv

all: venv

define make_venv
	python3 -m venv --prompt $(NAME) $(1)
	( \
		source $(1)/bin/activate; \
		pip install -U pip; \
		pip install -r requirements.txt; \
		pip install -U "."; \
		deactivate; \
	)
endef

venv:
	$(call make_venv,$(venvdir))

clean:
	rm -rf $(venvdir)/
	rm -rf ./build/
	rm -rf ./$(NAME).egg-info
	rm -rf ./$(NAME).*.so
	rm -rf ./$(NAME)/$(NAME).c
	rm -rf ./__pycache__/
	rm -rf ./$(NAME)/__pycache__/

test:
	python3 -m unittest
