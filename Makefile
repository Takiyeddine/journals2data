# A makefile to automate the creation process of the .zip package

# WARN: don't put " and use the echo command, not echo -e
LIGHT_ORANGE_COLOR=\e[38;5;216m
TURQUOISE_COLOR=\e[38;5;43m
LIGHT_BLUE_COLOR=\e[38;5;153m
RED_COLOR=\e[38;5;196m
NO_COLOR=\e[0m

# variables
ECHO = echo # @echo hides this command in terminal, not its output

# package variables
PKG_NAME = journals2data
PKG_VERSION = 0.1.2
FULL_PKG_NAME = $(PKG_NAME)-$(PKG_VERSION)
ZIP_PATH = releases/$(FULL_PKG_NAME).zip
PGK_BUILD_DIR = build/journals2data


# targets
# set default target : https://stackoverflow.com/questions/2057689/how-does-make-app-know-default-target-to-build-if-no-target-is-specified
.DEFAULT_GOAL := run
.PHONY: build rebuild clean clean_all clean_last run dirs default compile

# build zip
# clean python: https://stackoverflow.com/questions/28991015/python3-project-remove-pycache-folders-and-pyc-files 
build:
	@$(ECHO) "$(LIGHT_BLUE_COLOR)*** Making empty dir $(PGK_BUILD_DIR) *** $(NO_COLOR)"
	mkdir -p $(PGK_BUILD_DIR)

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* Copying src/journals2data/ $(NO_COLOR)"
	cp -ru src/journals2data/* $(PGK_BUILD_DIR)
	rm $(PGK_BUILD_DIR)/docker_conda_config.yml

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* Copying src/setup.py $(NO_COLOR)"
	cp src/setup.py $(PGK_BUILD_DIR)

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* Copying some conf/ files $(NO_COLOR)"
	cp ./conf/j2d.yml $(PGK_BUILD_DIR)
	cp ./conf/requirements.txt $(PGK_BUILD_DIR)

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* Copying cmd/ $(NO_COLOR)"
	cp -ru ./cmd $(PGK_BUILD_DIR)

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* Copying doc/README.md $(NO_COLOR)"
	cp ./doc/README.md $(PGK_BUILD_DIR)

	@$(ECHO) "$(LIGHT_BLUE_COLOR)* making empty logs/ and out/stdout $(NO_COLOR)"
	mkdir -p $(PGK_BUILD_DIR)/logs
	mkdir -p $(PGK_BUILD_DIR)/out/stdout

	@$(ECHO) "$(LIGHT_BLUE_COLOR)*** Cleaning $(PGK_BUILD_DIR)  *** $(NO_COLOR)"
	find ./build | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

	@$(ECHO) "$(LIGHT_BLUE_COLOR)*** Building $(ZIP_PATH)  *** $(NO_COLOR)"
	mkdir -p releases/
	(cd build/ && zip -r ../$(ZIP_PATH) journals2data/)

clean_last:
	rm -rf $(PGK_BUILD_DIR)

clean_build:
	rm -rf build/*

clean_releases:
	rm -rf releases/*


# Determine this makefile's path.
# Be sure to place this BEFORE `include` directives, if any.
THIS_FILE := $(lastword $(MAKEFILE_LIST))

clean_all:
	@$(MAKE) -f $(THIS_FILE) clean_build
	@$(MAKE) -f $(THIS_FILE) clean_releases

rebuild:
	@$(MAKE) -f $(THIS_FILE) clean_last
	@$(MAKE) -f $(THIS_FILE) build

# run command accepting parameters (command flags)
#   + https://stackoverflow.com/questions/6273608/how-to-pass-argument-to-makefile-from-command-line
# define macro ARGS
ARGS = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:${1}}`
# define variable for default string
DEFAULT_STR = --t # WARN: add an extra "-" to make it run correctly
run:
	@$(ECHO) "$(LIGHT_BLUE_COLOR)*** run program: ./cmd/run.sh $(NO_COLOR)"
	(./cmd/run.sh $(call ARGS,$(DEFAULT_STR)))

# accept extra arguments (by doing nothing when we get a job that doesn't match, rather than throwing an error
%:
    @:

dirs:
	mkdir -p build/
	mkdir -p releases/