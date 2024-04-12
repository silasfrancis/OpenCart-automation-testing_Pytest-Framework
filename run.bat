pytest -s -v -m "sanity" --html=./Reports/report.html testCases/
pytest -s -v -m "regression" --html=./Reports/report.html testCases/
