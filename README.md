## Install Requirement
pip install -r requirements.txt

## Goal
```bash
# check if there are Python syntax errors or undefined names
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
# run testcase
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
pytest
```