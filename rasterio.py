"""Offline compatibility stub for rasterio"""
def open(*args, **kwargs):
    class _StubDataset:
        meta = {"crs": "EPSG:4326", "width": 100, "height": 100}
        def read(self, *a, **k):
            import numpy as np
            return np.zeros((1, 100, 100))
        def close(self): pass
        def __enter__(self): return self
        def __exit__(self, *a): pass
    return _StubDataset()
