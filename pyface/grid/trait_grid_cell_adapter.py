import logging

logger = logging.getLogger()
logger.warning('DEPRECATED: pyface.grid, use pyface.ui.wx.grid instead.')

from pyface.ui.wx.grid.trait_grid_cell_adapter import *
