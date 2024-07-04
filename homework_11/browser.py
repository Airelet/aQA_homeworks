from abc import ABC, abstractmethod


class Browser(ABC):
    @abstractmethod
    def _set_browser(self):
        ...

    @abstractmethod
    def start_browser(self):
        ...


class Chrome(Browser):
    def __init__(self, version: str):
        self.__browser = "Chrome"
        self.__version = version

    def _set_browser(self):
        print(f'Setting your browser as {self.__browser} {self.__version}')

    def start_browser(self):
        self._set_browser()
        print(f'Starting {self.__browser} {self.__version}')


class Firefox(Browser):
    def __init__(self, version):
        self.__browser = "Firefox"
        self.__version = version

    def _set_browser(self):
        print(f'Setting your browser as {self.__browser} {self.__version}')

    def start_browser(self):
        self._set_browser()
        print(f'Starting {self.__browser} {self.__version}')


class Edge(Browser):
    def __init__(self):
        self.__browser = "Edge"
        self.__version = "126.0.2592.87"

    def _set_browser(self):
        print(f'Setting your browser as {self.__browser} {self.__version}')

    def start_browser(self):
        self._set_browser()
        print(f'Starting {self.__browser} {self.__version}')


if __name__ == '__main__':
    chrome = Chrome("2.0")
    firefox = Firefox("2.0")
    edge = Edge()

    chrome.start_browser()
    firefox.start_browser()
    edge.start_browser()
