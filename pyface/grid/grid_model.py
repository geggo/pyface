import logging

logger = logging.getLogger()
logger.warning('DEPRECATED: pyface.grid, use pyface.ui.wx.grid instead.')

from pyface.ui.wx.grid.grid_model import *
