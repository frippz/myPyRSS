def main():
    import feedparser
    from bs4 import BeautifulSoup


    feed = feedparser.parse("https://frippz.se/feed.xml")

    for entry in feed.entries[:2]:

        soup = BeautifulSoup(entry.description, "html.parser")
        asText = soup.get_text()
        summary = asText[:200]

        print('-')
        print('Title: ',entry.title)
        print('Summary:\n', summary, '…')

if __name__ == '__main__':
    main()
