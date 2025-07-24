import threading
from datetime import datetime


class URLStore:
    def __init__(self):
        self.store = {}
        self.lock = threading.Lock()

    def save(self, short_code, original_url):
        with self.lock:
            self.store[short_code] = {
                'url': original_url,
                'clicks': 0,
                'created_at': datetime.utcnow()
            }

    def get(self, short_code):
        with self.lock:
            return self.store.get(short_code)

    def increment_clicks(self, short_code):
        with self.lock:
            if short_code in self.store:
                self.store[short_code]['clicks'] += 1


# Singleton instance of URLStore
_store = URLStore()


# API functions expected by main.py
def add_url(short_code, original_url):
    _store.save(short_code, original_url)


def get_url(short_code):
    return _store.get(short_code)


def increment_click(short_code):
    _store.increment_clicks(short_code)


def get_stats(short_code):
    return _store.get(short_code)
