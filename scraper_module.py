from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

class GenericSpider(Spider):
    """A Scrapy spider to extract links and text content."""
    name = "generic_spider"

    def __init__(self, start_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.visited_links = set()  # To keep track of visited links

    def parse(self, response):
        # Extract and print the page title
        print("Page Title (Scrapy):", response.xpath("//title/text()").get())

        # Extract all text content from the page
        text_content = response.xpath("//body//text()").getall()
        text_content = "\n".join([line.strip() for line in text_content if line.strip()])

        # Save the text content to a file
        page_title = response.xpath("//title/text()").get().replace(" ", "_").replace("/", "_")
        filename = f"{page_title}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_content)
        print(f"Text content saved to '{filename}'.")

        # Extract all links on the page
        links = response.xpath("//a[@href]/@href").getall()
        for link in links:
            # Normalize the link
            if link.startswith("/"):
                link = response.urljoin(link)
            if link.startswith("http") and link not in self.visited_links:
                self.visited_links.add(link)  # Mark the link as visited
                yield response.follow(link, callback=self.parse)  # Visit the link

def scrape_site(url):
    """Run the Scrapy spider for the given URL."""
    process = CrawlerProcess()
    process.crawl(GenericSpider, start_url=url)
    process.start()
