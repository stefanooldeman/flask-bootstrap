
test: clean-pyc
	python -m unittest discover
	coverage report
	coverage html -d docs/coverage/

clean-pyc:
	find . -type f -name "*.pyc" -delete
	rm -rf {*.egg-info,bin,dist,build,include,lib,lib64}

documentation:
	cd docs && make clean html

pep8:
	pep8 -r --ignore E501 liverail_importer && echo "All good!"

