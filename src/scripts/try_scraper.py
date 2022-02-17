# calculate scores

# run at ".." level
'''
from context import get_python_run_context
get_python_run_context()

from journals2data.scraper import SourceScraper
from journals2data import J2DConfiguration
from journals2data import exception

# get sources
config: journals2data.J2DConfiguration

sources = config.get_sources()
if(len(sources) <= 0):
    raise exception.NoSourcesError(
        """
        Error: No sources were found.
        Nothing to do. Terminating.
        """
    )
# create source scrapers
source_scrapers = []
for source in sources:
    source_scraper: SourceScraper = SourceScraper(
        source, config
    )
    source_scrapers.append(source_scraper)

#excute funtions here
for source_scraper in source_scrapers:
    source_scraper.save_debug()
'''