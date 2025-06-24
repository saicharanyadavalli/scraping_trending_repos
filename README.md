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

1. **Import Required Libraries**  
   The script uses the following libraries:
   - `requests` for sending HTTP requests
   - `BeautifulSoup` from `bs4` for parsing the HTML content
   - `csv` to write the scraped data into a CSV file
   - `datetime` to generate a timestamp for the output file name

2. **Fetch the GitHub Trending Page**  
   The script sends a GET request to [https://github.com/trending](https://github.com/trending) to retrieve the current list of trending repositories.

3. **Parse HTML Content**  
   The fetched HTML is parsed using `BeautifulSoup` with the `lxml` parser.  
   The script searches for all `<article>` tags with the class `"Box-row"`, each representing a trending repository.

4. **Extract Repository Data**  
   From each article block, the script extracts:
   - The `<a>` tag inside an `<h2>` tag with class `"h3 lh-condensed"`
   - The `href` attribute, which contains the path to the repository (e.g., `/DrKLO/Telegram`)
   - A full GitHub URL is built by prepending `https://github.com`
   - The repository name is cleaned by removing slashes

5. **Generate a Timestamped Filename**  
   A filename is created using the current date and time in the format `dd-mm-yyyy_HHMMSS`, ensuring uniqueness and traceability.

6. **Write Data to CSV**  
   The script writes data into a CSV file with the columns: `ranking`, `repository name`, and `link`. Only the top 5 repositories are recorded.

7. **Save Output**  
   The CSV file is saved in the same directory where the script is located.

