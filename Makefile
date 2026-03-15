check:
	python3 tools/validate_samples.py
	python3 tck/runner/offline2.py tck/suites/nc
	python3 tools/gen_lint.py
