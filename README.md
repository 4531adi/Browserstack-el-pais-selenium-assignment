# BrowserStack EL País Selenium Assignment

## Overview

This project is a technical assignment demonstrating web scraping, API integration, text processing, and cross-browser testing using Selenium and BrowserStack.

The script scrapes articles from the **Opinion section of EL País**, translates the article titles to English, analyzes repeated words, and runs automated browser tests on BrowserStack across multiple browsers in parallel.

## Features

### 1. Web Scraping

Using Selenium, the script:

* Opens the EL País website
* Navigates to the **Opinion** section
* Extracts the **first five articles**
* Prints:

  * Article titles (Spanish)
  * Article content (Spanish)

### 2. Image Download

If available, the script downloads and saves the **cover image of each article** to the local `images/` folder.

### 3. Translation

Article titles are translated from **Spanish → English** using a translation API.

### 4. Text Analysis

The translated titles are analyzed to:

* Identify words repeated **more than twice**
* Print the word and its occurrence count.

### 5. Cross-Browser Testing (BrowserStack)

The test is executed on **BrowserStack Automate** using Selenium across **5 parallel browser sessions**.

Browsers used:

* Chrome – Windows 10
* Firefox – Windows 10
* Edge – Windows 11
* Chrome – macOS Ventura
* Firefox – macOS Ventura


