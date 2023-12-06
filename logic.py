import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to check heading hierarchy
def check_headings(driver):
    headings = driver.find_elements(By.XPATH, "//h1|//h2|//h3|//h4|//h5|//h6")
    if not headings:
        return "Fail"  # Fail if there are no headings

    heading_tags = [h.tag_name for h in headings]
    expected = 'h1'
    for tag in heading_tags:
        if tag != expected:
            return "Fail"
        expected = f"h{int(tag[1]) + 1}" if int(tag[1]) < 6 else 'h6'
    return "Pass"

# Setup WebDriver
driver = webdriver.Safari()

# Read URLs from file and check headings
results = []
with open('urls.txt', 'r') as file:
    for url in file:
        url = url.strip()
        if url:
            driver.get(url)
            result = check_headings(driver)
            results.append([url, result])

# Writing results to CSV
with open('results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['URL', 'Result'])
    csvwriter.writerows(results)

# Close the WebDriver
driver.quit()
