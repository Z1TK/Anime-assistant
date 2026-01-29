from backend.service.browser import WebWork

sites = {
    "google": "https://www.google.com",
    "edge": "https://www.bing.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "reddit": "https://www.reddit.com",
    "x": "https://x.com/home",
    "instagram": "https://www.instagram.com",
}


def open_site(command: str) -> bool:
    words = command.split()
    if len(words) == 2 and command.startswith("открой"):
        url = f"https://{words[1]}.com"
        WebWork.open_any_site(url)
        return True
    if command == 1 and command in sites:
        WebWork.open_any_browser(command)
        return True
    return False


def request_to_youtube(command: str) -> bool:
    query = command.split()[2:]
    if len(command) > 2 and command.startswith("нади видео"):
        WebWork.search_youtube(sites["youtube"], "+".join(query))
        return True
    return False
