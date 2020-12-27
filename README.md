# Setup
1. create virtual environment: $python -m venv <<b>venv-name</b>>
2. set <b>venv-name</b> becomes the interpreter of project
3. install plugins: $ pip install -r requirements.txt
4. check installed-plugins: $ pip freeze

# Execute
$ pytest -m smoke -k customer --browser=chrome -s -v -n=1
- -m: pytest mark
- -k: run all tests that name match the keyword
- --browser: run with browser
- -s: show print text
- -v: show meta data
- -n: run multiple threads
- --last-failed: run tests failed
