# Heading Hierarchy Checker for Safari

## Introduction
This Python script automates the process of checking the heading hierarchy of web pages using Safari's WebDriver. It reads URLs from a file, navigates to each page, checks the heading tags (h1, h2, h3, etc.) for logical order, and outputs the results to a CSV file.

## Dependencies
- **Python**: The script is written in Python and requires Python to be installed on the user's system.
- **Selenium**: A web automation tool used to control Safari browser programmatically.
- **Safari Browser**: The script uses Safari's WebDriver, so a macOS with Safari installed is required.

## Installation

### 1. Install Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/). Ensure that Python is added to your PATH.

### 2. Install Selenium
Install Selenium using pip. Open your terminal and run:

```bash
pip install selenium
```

### 3. Enable Safari WebDriver

Open Safari, go to "Safari" > "Preferences" > "Advanced" and enable the "Show Develop menu in menu bar" option.
In the "Develop" menu, check "Allow Remote Automation".

## Usage

#### Step 1: Prepare URL List

Create a text file named marshall.txt and list the URLs to be checked, one per line.
#### Step 2: Download the Script

Download script.py from this repository.
#### Step 3: Run the Script

Open a terminal, navigate to the directory containing script.py and marshall.txt, and run:

```bash
python script.py
```

#### Step 4: View Results

Check the generated results.csv file for the heading hierarchy check results.

## Limitations

The script assumes web pages are accessible and load properly. It does not handle network issues or non-standard HTML structures that might affect heading detection. Currently, the script is designed to work only with Safari on macOS.

## Contribution

Contributions to enhance this script or to extend its compatibility with other browsers and operating systems are welcome.
