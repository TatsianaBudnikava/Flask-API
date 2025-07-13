## Environment
Python 3.9.23

Platform macOS-15.5-x86_64-i386-64bit

API Framework:	Flask

Test Framework:	pytest + pytest-cov, pytest-html

Performance Testing: Locust

Reporting: pytest-html

## How to Run the Application and Tests
Requirements:
- Python 3.9+
- pip
- virtualenv or venv

Install dependencies:
```bash
cd project-root
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Start the Flask API
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
python run.py
```

## Employee & Skills REST API
Flask-based REST API to manage employees and their skills.

## Features
- Create, update, delete employees
- Create, update, delete skills
- List all employees and skills
- Search employees by name, surname, or skill
- Handles invalid data and error scenarios
- Proper HTTP status codes and error messages
- Automated testing with `pytest` + `pytest-html`
- (Optional) Authentication support

## Endpoints

## Employees

## Create Employee
`POST /employees`

```json
{
  "name": "John",
  "surname": "Doe"
}
```

API Testing

Automated tests are implemented with pytest and cover:
- CRUD operations for employees and skills
- Search functionality
- Error handling for:
- Missing or invalid data
- Not found (404)
- Unauthorized access (401 - placeholder for future support)

## Test Automation Reporting
To ensure the stability and reliability of the REST API, automated tests were implemented and configured to produce reports covering:

## Test Pass/Fail Status
* All test cases are executed using 'Pytest'.
* The output includes a summary of passed, failed, and skipped tests.
* Tests cover CRUD operations for employees and skills, input validation, and unauthorized access positive and negative scenarios.

Run API tests with:

```bash
pytest tests/ --tb=short -v
```

## Test Coverage
Test coverage is measured using `pytest-cov`. It shows which parts of the application code are covered by tests.
Coverage is measured using the pytest-cov plugin.
Current coverage: 84%

To generate a coverage report:
```bash
pytest --cov=employee_api --cov-report=html tests/
```
After running, open the generated report:

```bash
open htmlcov/index.html  # macOS
# or
xdg-open htmlcov/index.html  # Linux
```

The report highlights:
* Which functions are tested
* Any untested lines or branches

To generate test execution html report:
```bash
pip install pytest-html
pytest tests/ --html=reports/test_report.html --self-contained-html
```
After running the generated report will be created in the project folder.
test_report.html


## Potential Improvements or Observations
Authentication Coverage: Currently, unauthorized access scenarios (e.g., missing or invalid tokens) are not fully covered. Adding dedicated tests for 401 responses will strengthen security validation.

UI Layer Absence: The project does not include a user interface (UI), so no end-to-end or UI tests are available. Implementing even a minimal frontend (e.g., HTML + JS or React) would enable full-stack testing.

Test Coverage Gaps: Some edge cases (e.g., malformed payloads, very large inputs) are not yet tested. Expanding negative test scenarios will improve robustness.

No CI/CD Pipeline: Tests and coverage reports are generated locally. Integrating automated testing and reporting into a CI pipeline (e.g., GitHub Actions, GitLab CI) would enhance workflow efficiency and reliability.

## Performance Testing with Locust
To ensure the REST API performs well under load and scales appropriately, basic load testing is performed using [Locust](https://locust.io/).

### Overview
Locust allows simulating multiple concurrent users performing typical API workflows, measuring response times, throughput, and error rates.

## Setup & Running
1. Install Locust (if not installed):
```bash
pip install locust
```
2. Create locustfile.py (created)
3. Run Locust UI:
```bash
locust -f locustfile.py
```
4. Open the Locust web interface at [http://localhost:8089](http://localhost:8089), specify the number of users (e.g., 100) and spawn rate, then start the test.
5. Alternatively, run in headless mode for automated tests:
```bash
locust -f locustfile.py --headless -u 100 -r 10 --run-time 5m --csv=locust_report
```

## Tested Scenarios
* Employee CRUD operations
* Employee search functionality
* Handling of invalid requests and errors

## Metrics Collected
* Average and percentile response times
* Requests per second (RPS)
* Failure rates and error counts

## Notes
Performance testing complements functional tests by helping detect bottlenecks and verifying system stability under realistic user loads.
