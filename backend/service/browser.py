import webbrowser


class WebWork:
    @classmethod
    def open_any_site(url: str):
        webbrowser.open(url)

    @classmethod
    def search_youtube(url: str, query: str):
        webbrowser.open(url + f"/results?search_query={query}")
