Test Planning and Strategy

### Test level
The testing approach was based on the Test Pyramid concept:
- Unit tests (Base) – Test individual components in isolation. Fast, automated, and high in coverage (70-80%).
- Integration tests (Middle) – Verify data flow between components. Moderate speed and coverage (15-20%).
- E2E tests (Top) – Validate the full system. Slow, complex, but crucial for key workflows (5-10%).

### Objectives and scope
The main objective is to validate the correctness and reliability of the REST API responsible for managing employees and their skills. The testing strategy covers:

Functional testing:
- CRUD operations for employees and skills
- Employee search functionality
- Error and edge case handling (e.g., invalid data, missing fields)

Non-functional testing:
- Performance: Evaluate response times, throughput, and scalability under load using Locust to simulate realistic user behavior and concurrent access.

Non-functional testing (future scope):
- Security: Ensure endpoints handle unauthorized access appropriately
- Usability (optional): Ensure API responses are intuitive and well-documented.

Scope

✅ Features to Test
Create, read, update, and delete employees
Create, read, update, and delete skills
Search employees by name, surname, or skill
Error handling for invalid or missing input
404 responses for missing resources

❌ Features Excluded from This Phase
UI testing (no UI implemented yet).
Authentication & Authorization (not implemented in base version).
Advanced performance/load testing.

### Data Integrity (Future Scope)

Once the UI is implemented, E2E tests will validate data consistency between the API and UI.
Tests will verify that operations (create, update, delete) performed via API are accurately reflected in the UI,
and vice versa, ensuring synchronized data presentation and backend state.

### Types of Testing Planned

Unit tests:	For utility functions/models (future).
Integration tests:	API endpoint testing with Flask test client.
API tests:	Automated via pytest.
Manual testing:	For exploratory tests and edge-case coverage.

### Test Environment
Python 3.9.23
SQLite in-memory database
Test runner: pytest
Platform: macOS-15.5-x86_64-i386-64bit
API Framework:	Flask
Test Framework:	pytest + pytest-cov, pytest-html
Performance Testing: Locust
Reporting: pytest-html

### Prioritized Areas
	                        
CRUD for Employees & Skills: Core functionality; used in every flow.
Search functionality: Affects discoverability and user experience.
Error handling for malformed requests: Ensures robustness and stability.
Recent changes: Often introduce regressions.
API boundaries and unexpected input: High-risk for bugs and misuse.

### Testing Types
Testing strategy combines automated and manual tests to ensure proper coverage of both functionality and system reliability.

Automated Testing:

Unit Tests: To validate individual components like data validation and helper functions. (planned)
API Tests: Verify core REST API endpoints (CRUD, validation, search, error handling). Implemented using pytest.
Integration Tests: Test interactions between layers such as routes and the database. Partially covered.
UI Tests: Not implemented in this project scope. In the future, tools like Playwright or Selenium may be used.

Manual Testing:
	
Edge-case testing, unexpected inputs, API status/response inspection: Postman / Curl
Smoke testing, DB migration checks: CLI tools, SQLite GUI

Functional testing:

Automated tests for successful user flows (creating, retrieving, updating, deleting).
Negative test cases for invalid input, missing fields, and non-existent resources.

Non-Functional Coverage:

Performance: Basic load testing using tools like Locust.
Security: Checked for proper HTTP status codes, error masking (no stack traces).
Stability: All tests are isolated, using temporary databases created/dropped per test run.
Scalability: Modular code and test structure to easily support future features.

Load and Performance Testing:

To verify system behavior and responsiveness under expected and peak user loads, ensuring the application meets performance requirements and remains stable during high traffic.
Locust — open-source load testing tool written in Python, which allows writing user behavior scripts and running distributed tests simulating hundreds or thousands of users.

Key Features of the Load Testing Approach:

User scenarios: Automate critical API workflows (e.g., employee CRUD, search) with simulated concurrent users.
Scalability testing: Gradually increase the number of users to find performance thresholds.
Metrics collected: Response time percentiles, error rates, requests per second (RPS), failure counts.
Test execution: Run Locust tests locally during development and as part of CI/CD pipelines in headless mode for automation.
Reporting: Use Locust UI for real-time monitoring and export data for further analysis.

Integration into Testing Process:

Load tests are designed alongside functional API tests and run regularly to detect regressions impacting performance.
Performance results feed back into development for optimization priorities.
Load testing scenarios and parameters are documented alongside test cases to ensure reproducibility.

### Test Data Management
Factories & Fixtures: pytest fixtures are used to generate consistent test data (e.g., employee and skill records).
Data Isolation: Each test run starts with a clean, in-memory SQLite database.
Data Sets: Include valid, boundary, and invalid values.
Teardown: The database is reset or dropped after each test to ensure isolation.

### Test Execution & Automation

Test Runner: pytest
CI Integration: GitHub Actions / GitLab CI / Makefile for local use (not integrated yet)
Reporting: pytest-html
Coverage: pytest-cov, goal ≥ 80% on API
Parallel Testing: Supported via pytest-xdist
Trigger: On every PR + nightly runs (not implemented yet)
Notifications: (Optional) Slack/email integration for failures (not implemented yet)

### Quality Metrics (for team environments)

Test Coverage: ≥ 80% (API level).
Defect Leakage Rate: < 5% in production (best practices).
Mean Time to Detect: < 1 hour (best practices).
CI Build Duration: ≤ 5 minutes (best practices).

### Regression and Maintenance Strategy
Each fixed bug is followed by a dedicated regression test.
New features must include or be accompanied by test coverage.
Pull requests are blocked unless tests pass in CI.
Testing documentation lives in TestStrategy.md and Confluence.

### Change Management
All test cases reviewed when business logic/API contract changes.
High-risk endpoints (e.g., POST /employees, PATCH /skills) marked and monitored in PRs.

### Test Case Review
All manual and automated tests go through peer review.
Tests are updated or deprecated when features change.

### Post-deployment Testing
Basic smoke tests run after deployment.
Monitoring and logs are checked for anomalies in real usage.

### Risk-Based Testing
High-priority features (CRUD, search) are tested with both normal and edge cases; low-risk areas get smoke-level testing.

