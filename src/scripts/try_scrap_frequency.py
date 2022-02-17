# this file is used to test the scrap-frequency feature

# run at ".." level
from context import get_python_run_context
get_python_run_context()


import time
import datetime as dt

from journals2data import scraper

# variables
DEBUG: bool = True
base_out_file_path: str = "out/articles_"
out_file_path = base_out_file_path + dt.datetime.now().strftime("%d%m%Y%H%M%S") + ".csv"



# test Article Full text extractor with frequencies
test_urls: list = [
    "https://www.wsj.com/articles/novavax-covid-19-vaccine-is-90-effective-in-key-study-11623664800?mod=hp_lead_pos3",
    "https://eu.usatoday.com/story/news/world/2021/06/14/vladimir-putin-refuses-guarantee-alexei-navalnys-safety-prison/7682827002/",
]

#url = "http://www.industrie-mag.com/article13165.html"

# csv manipulations
def write_in_csv(data: dict, csv_file_name: str):
    """
    Write a dictionary of URLs to a CSV file with provided name
    """
    with open(csv_file_name, mode='a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow([data["date"], data["status"]])

#def scrap_url_frequency(url: str, scrap_frequency: int, LIMIT_TEST: bool = false):
    # TODO: try it for real


# test_scraper


def scrap_urls(urls: list):
    for url in urls:
        try:
            article_scraper: scraper.ArticleScraperWithDownload = scraper.ArticleScraperWithDownload(url)
            article_scraper.preprocessAndExtraction()
            print("URL : " + article_scraper.url)
            print("\n")
            print("=======")
            print("Title:" + article_scraper.article.title)

            print("Texte")
            if article_scraper.article_text=="":
                print("texte VIDE")
            print(article_scraper.article_text)
            print("\n")
            print("=======")
            print("\n")
        except Exception as e:
            print(e)

            print("**********************************************")

# scraping loop
nb_scrap_loop_test: int = 3
while(nb_scrap_loop_test < 0):

    # scrap urls
    scrap_urls(test_urls)
