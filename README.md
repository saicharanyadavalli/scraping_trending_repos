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
```

## 📌 Description (70–80 words)
This Python script scrapes the top 5 trending repositories from GitHub Trending and saves the ranking, repository name, and link into a CSV file. It uses the requests library to fetch HTML and BeautifulSoup to parse the content. The output file is timestamped with the current date and time in the format dd-mm-yyyy_HHMMSS and saved in the same directory. This tool is helpful for quickly tracking what’s popular on GitHub at any moment.

## 🧠 Approach
Import Required Libraries
The script uses the following libraries:

requests for sending HTTP requests

BeautifulSoup from bs4 for parsing the HTML content

csv to write the scraped data into a CSV file

datetime to generate a timestamp for the output file name

Fetch the GitHub Trending Page
The script sends a GET request to https://github.com/trending to retrieve the current list of trending repositories.

Parse HTML Content
The fetched HTML content is parsed using BeautifulSoup with the lxml parser. The script searches for all <article> tags with the class "Box-row", each representing one trending repository.

Extract Repository Data
From each article block, the script extracts:

The <a> tag inside the <h2> tag with class "h3 lh-condensed"

The href attribute, which contains the repository path (e.g., /DrKLO/Telegram)

A full GitHub URL is built by prepending https://github.com

The repository name is cleaned by stripping slashes

Generate a Timestamped Filename
A filename is created using the current date and time in the format dd-mm-yyyy_HHMMSS, ensuring uniqueness and traceability.

Write Data to CSV
The script writes the data to a CSV file with columns: ranking, repository name, and link. Only the top 5 repositories are recorded.

Save Output
The CSV file is saved in the same directory where the script is located.
