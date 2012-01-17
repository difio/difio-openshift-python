build:
	./setup.py sbuild

clean:
	./setup.py clean
	rm -f MANIFEST

distclean: clean
	rm -rf dist/

help:
	@echo "Usage: make <target>                   "
	@echo "                                       "
	@echo " build - build the package             "
	@echo " clean - remove all build files        "
	@echo " distclean - remove all non git files  "
	@echo " help - show this help and exit        "
