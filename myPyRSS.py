def main():
    import feedparser
    from bs4 import BeautifulSoup


    feed = feedparser.parse("https://frippz.se/feed.xml")

    for entry in feed.entries[:2]:

        soup = BeautifulSoup(entry.description)
        asText = soup.get_text()
        summary = asText[:120]

        print('-')
        print('Title: ',entry.title)
        print('Summary:\n', summary, '…')

if __name__ == '__main__':
    main()
