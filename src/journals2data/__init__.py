# -*- coding: utf-8 -*-
"""
Imagination is more important than knowledge. --Albert Einstein
"""

__title__ = "journals2data"
__author__ = "Onyr (Florian Rascoussier <florian.rascoussier@insa-lyon.fr)"
__license__ = "GLP-3+"
__all__ = ["console", "data", "scraper", "utils", "exception"]

from .configuration import J2DConfiguration
from .journals2data import Journals2Data
from .cli import main