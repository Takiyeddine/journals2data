    # type: -> typing.Optional[Article]
    def scrap(self, raw_html: str = ""):
        """
        This function is used to scrap content from the web
        of the Article.
        Optionally, the function can take direct raw html.
        It retuns itself if the scraping was successful.
        It returns None if the article is no more available online.
        """
        try:
            article_scraper: scraper.ArticleScraperWithDownload = scraper.ArticleScraperWithDownload(self.url, raw_html)
            article_scraper.preprocessAndExtraction()

            self.title_from_page = article_scraper.article.title
            self.full_text = article_scraper.article_text
            self.publish_date = article_scraper.article.publish_date

            # log first scraping instant as self.timestamp_start
            if(self.timestamp_start == None or self.timestamp_start == ""):
                self.timestamp_start = datetime.datetime.now().strftime("%S_%M_%H_%d_%m_%Y")
            
            return self
        except Exception as e:
            print(e) # TODO: only temporary print

            # define this moment as the final timestamp for scraping
            self.timestamp_end = datetime.datetime.now().strftime("%S_%M_%H_%d_%m_%Y")

            # save the Article
            self.save_to_file()
            return None