# GitHub Trending Repositories Scraper

This Python script scrapes the top 5 trending repositories from [GitHub Trending](https://github.com/trending) and saves their ranking, repository name, and direct link to a timestamped CSV file.

## 📌 Features

- Extracts the top 5 repositories from GitHub Trending
- Captures:
  - Ranking
  - Repository name (e.g., `microsoft/edit`)
  - Direct GitHub link
- Saves results to a `.csv` file with a timestamped filename

## 🛠 Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install them using pip if needed:

```bash
pip install requests beautifulsoup4

✅ 📌 Description (70–80 words)
This Python script scrapes the top 5 trending repositories from GitHub Trending and saves the ranking, repository name, and link into a CSV file. It uses the requests library to fetch HTML and BeautifulSoup to parse the content. The output file is timestamped with the current date and time in the format dd-mm-yyyy_HHMMSS and saved in the same directory. This tool is helpful for quickly tracking what’s popular on GitHub at any moment.

✅ 🧠 Approach
Step-by-step:
Import Libraries

requests for making HTTP requests

BeautifulSoup from bs4 for HTML parsing

csv to write data to a file

datetime to generate a timestamp for the filename

Fetch Web Page

Use requests.get() to get the HTML content from https://github.com/trending.

Parse HTML Content

Use BeautifulSoup(html, 'lxml') to convert raw HTML into a structured format.

Find all <article> blocks with class "Box-row" which contain each repo listing.

Extract Repository Info

From each article block, extract:

The <a> tag inside <h2> with class "h3 lh-condensed"

The href attribute (relative link)

Combine it with https://github.com to get the full link

Strip slashes to get the repository name

Write to CSV

Create a CSV file named like trendingrepos_23-06-2025_210350.csv

Write column headers: ranking, repository name, link

Write the top 5 entries into the file

Save Location

The CSV is saved in the same directory as the script.
