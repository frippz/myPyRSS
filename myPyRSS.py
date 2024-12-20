def main():
    import feedparser
    from bs4 import BeautifulSoup

    feed = feedparser.parse("https://frippz.se/feed.xml")

    for i, entry in enumerate(feed.entries[:10], start=1):

        soup = BeautifulSoup(entry.description, "html.parser")
        asText = soup.get_text()
        summary = asText[:200]

        print(f"#{i}")
        print("---")
        print("Title: ", entry.title)
        print("Summary:\n", summary, "…\n")


if __name__ == "__main__":
    main()
