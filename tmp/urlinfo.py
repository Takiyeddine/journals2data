# values of the MapURLInfo map

class URLInfo:

    title_from_a_tag: str
    scraped_nb_times: int

    def __init__(
        self,
        title_from_a_tag: str
    ):
        self.title_from_a_tag = title_from_a_tag

        # default init values
        self.scraped_nb_times = 0
        
