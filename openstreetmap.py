"""Offline compatibility stub for OpenStreetMap"""
class Crawler:
    def __init__(self, *a, **k): pass
    def get(self, *a, **k): return {}
    def extract(self, *a, **k): return []
class Extractor:
    def __init__(self, *a, **k): pass
    def extract(self, *a, **k): return []
