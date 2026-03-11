# Amazon Automation Framework (Playwright + Python)

This project is an end-to-end automation testing framework for **Amazon.de**, built using:

- Playwright
- Python
- Pytest
- Page Object Model (POM)

The framework demonstrates automated UI testing of common e-commerce user journeys.

---

## Project Features

✔ Page Object Model architecture  
✔ Pytest fixtures  
✔ Parameterized tests  
✔ Dynamic waits and assertions  
✔ HTML test reports  
✔ Screenshots on failure  

---

## Test Scenarios Covered

The automation suite includes tests for:

- Homepage validation
- Product search
- Search suggestions
- Clicking search suggestions
- Product page validation
- Add product to cart
- Remove product from cart
- Category navigation
- Price filtering
- Rating filtering
- Language change
- Help page navigation
- Sell on Amazon page
- And more

Total tests: **~20 automated test cases**

---

## Project Structure

```
pages/          → Page Object Model classes  
tests/          → Test cases  
screenshots/    → Failure screenshots  
conftest.py     → Pytest fixtures  
pytest.ini      → Test configuration
```

---

## Running the Tests

Install dependencies:

```
pip install -r requirements.txt
playwright install
```

Run tests:

```
pytest -v
```

Generate HTML report:

```
pytest --html=report.html
```

---

## Example Test Flow

Example scenario automated in this framework:

```
Open Amazon homepage
Search for a product
Apply price filter
Open product
Add to cart
Remove from cart
Verify cart updates
```

---

## Author

**Abu Bakar Saadat**

Software Quality Assurance Engineer  
Automation Testing | Playwright | Python | Pytest