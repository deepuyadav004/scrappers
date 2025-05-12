# Entry point for the web scraper project

from scraper_module import scrape_site

def main():
    print("Welcome to the Web Scraper Project!")
    url = "https://en.wikipedia.org/wiki/Main_Page"  # Replace with the target URL
    print(f"Scraping the site: {url}")
    scrape_site(url)

if __name__ == "__main__":
    main()
