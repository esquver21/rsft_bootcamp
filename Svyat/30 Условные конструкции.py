def normalize_url(url: str) -> str:
    if ("https://" in url[:9]):
        return url
    return f"https{url[4:]}" if ("http://" in url[:8]) else f"https://{url}"