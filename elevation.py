"""Offline compatibility stub for elevation"""
def clip(bounds=None, output=None, product="SRTM3", **kwargs):
    return output or "elevation_data.tif"
def clean(**kwargs): pass
def seed(bounds=None, product="SRTM3", **kwargs): pass
