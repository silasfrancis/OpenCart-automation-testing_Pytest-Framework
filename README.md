# Testing OpenCart Demo Application
This project involves the testing of the Customers Module on the OpenCart Demo Platform using the Pytest FrameWork

## Features
- Page Object Model
- HTML Reports
- Automation logs
- Multiple Browsers Support
- Parallel Testing

## Test Scenarios
- Register User on the OpenCart Demo site
- Login User
- Search for Products and add to Shopping Cart
- Check out Products in the Shopping Cart
  
## Languages, libraries and tools used
- Python
- Pytest
- pytest-html
- pytest-xdist
- Openpyxl
- Allure-pytest

## Installation
To install the required libraries for distributed testing, run the following command in your terminal:
```bash
pip install -U pytest
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest
```

## Test Execution
Test Execution commands can be found in the run.bat file located in this respository 

#### Browser Supported:
- Chrome (--browser chrome)
- Edge (--browser edge)
- Firefox (--browser firefox)
  
```bash
e.g.
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
```
> This will run test on Chrome Browser

_N/B: If no browser is specified test will be executed on chrome_
