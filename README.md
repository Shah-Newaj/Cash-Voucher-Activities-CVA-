# Cash Voucher Activities (CVA) Automation Framework
International Live Project of Save the children international (SCI). 
A robust end-to-end test automation framework for the Cash Voucher Activities (CVA) 
application developed using Python, Playwright, and Pytest. The framework follows 
the Page Object Model (POM) architecture to ensure maintainability, scalability, and 
reusable test components.

# Key Features
## Functional Automation
End-to-end automation of CVA business workflows
* Page Object Model (POM) architecture
* Pytest-based test execution
* Data-driven testing using Excel
* Dynamic test data management
* Reusable page objects and utility methods
* Reliable Playwright locator strategy

## User Creation Automation
* Automated user creation using Excel test data
* Supports multiple user records through data-driven execution
* Reduces manual effort and simplifies test maintenance

## Reporting
* Allure Report integration
* Automatic screenshot capture on failures
* Video recording attachment for test execution
* Detailed execution logs
* Rich test execution reporting

## Feature-wise Performance Report
A custom HTML performance dashboard that measures the execution time of 
each business feature during an end-to-end workflow.

The report includes:

* Application information
* Environment details
* Country and Project information
* Total execution time
* Average response time
* Feature-wise execution time
* PASS/FAIL summary
* Interactive Bar Chart
* PASS/FAIL Pie Chart
* Fastest and Slowest feature summary

## Automated Business Flow

Current Happy Path automation covers:
* User Login
* Country Selection
* Project Selection
* Beneficiary List Creation
* Send Beneficiary List for Approval
* Beneficiary List Approval

Each business feature is individually timed and included in the performance dashboard.

## Technology Stack
* Python
* Playwright
* Pytest
* Allure Report
* HTML5
* CSS3
* OpenPyXL (Excel data handling)
* Page Object Model (POM)

## Framework Highlights
* Data-driven testing with Excel
* Modular Page Object Model architecture
* Custom feature-level performance reporting
* Allure reporting with video attachments
* Reusable and maintainable framework
* Enterprise-ready automation structure
* Easy CI/CD integration

## Future Enhancements
* API automation integration
* Database validation
* Cross-browser execution
* Parallel test execution
* Performance trend comparison across executions
* Automatic PDF report generation
* CI/CD pipeline integration

### Command to run the project...

    pytest -s .\tests\test_cva.py --headed

### Command to run the project with report...

    pytest -s .\tests\test_cva.py --headed --html=report.html --self-contained-html

### Command to run the project with allure report...

    pytest -v -s --alluredir="AllureReports/reports" .\tests\test_cva.py --headed

### Run Allure Report (in Command Prompt(cmd))...

    allure serve C:\Users\shah.newaj\PycharmProjects\Cash-Voucher-Activities-CVA-\AllureReports\reports

### Used Packages in this Project...

pip	26.0.1

pkginfo	1.12.1.2	

platformdirs	4.9.6	

playwright	1.58.0	

pluggy	1.6.0

poetry	1.8.4	

poetry-core	1.9.1	

poetry-plugin-export	1.8.0	

ptyprocess	0.7.0	

pyee	13.0.1	

pygments	2.20.0	

pyproject-hooks	1.2.0

pytest	9.0.3

pytest-base-url	2.1.0

pytest-playwright	0.7.2

python-slugify	8.0.4

pywin32-ctypes	0.2.3

rapidfuzz	3.14.5

requests	2.33.1

requests-toolbelt	1.0.0

shellingham	1.5.4

text-unidecode	1.3

tomlkit	0.14.0

trove-classifiers	2026.1.14.14

typing-extensions	4.15.0

urllib3	2.6.3

virtualenv	20.39.1

wheel	0.46.3
