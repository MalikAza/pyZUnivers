class UserBanner:
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