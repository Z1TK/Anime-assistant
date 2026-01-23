import webbrowser

class WebWork:
    @classmethod
    def open_any_browser(url: str):
        return webbrowser.open(url)
    
    @classmethod
    def search_youtube(url: str, query: str):
        return webbrowser.open(url + f'/results?search_query={query}')
    
    @classmethod
    def search_google(url: str, query: str):
        return webbrowser.open(url + f'/search?q={query}')
    
    @classmethod
    def search_yandex(url: str, query: str):
        return webbrowser.open(url + f'/search/?text={query}')