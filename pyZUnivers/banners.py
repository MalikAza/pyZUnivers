class UserBanner:
    """
    Represents a user banner.

    Attributes:
        date (str): The date of obtention of the banner.
        title (str): The title of the banner.
        image_url (str): The image url of the banner.
    """

    def __init__(self, payload) -> None:
        self.__payload = payload
        self.__item = payload['banner']
    
    @property
    def date(self) -> str:
        return self.__payload['date']
    
    @property
    def title(self) -> str:
        return self.__item['title']
    
    @property
    def image_url(self) -> str:
        return self.__item['imageUrl']