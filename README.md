# day01-web-automation
# Day 01 - Web Automation Test Suite

Automated test suite for [Books to Scrape](http://books.toscrape.com) 
built as part of my 14-Day QA Engineer Challenge.

## Tech Stack
- Python 3.13
- Selenium 4.18
- PyTest 8.1
- pytest-html
- WebDriver Manager

## Project Structure
day01-web-automation/
├── tests/
│   └── test_homepage.py
├── pages/
│   └── home_page.py
├── utils/
│   └── driver_factory.py
├── reports/
├── requirements.txt
└── README.md

## Test Cases
| Test | Type | Status |
|------|------|--------|
| Page title contains "Books to Scrape" | Smoke | ✅ Pass |
| Books are displayed on homepage | Functional | ✅ Pass |
| Navigation links are present | Functional | ✅ Pass |

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run tests
python -m pytest tests/test_homepage.py -v

### Run with HTML report
python -m pytest tests/test_homepage.py -v 
--html=reports/report.html --self-contained-html

## What I Learned
- Setting up a Selenium project from scratch
- Page Object Model pattern
- Driver Factory pattern
- Debugging ChromeDriver compatibility issues
- Writing robust assertions

## Author
Hrithi | 14-Day QA Engineer Challenge - Day 1
