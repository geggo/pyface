""" The handler used to restore views. """


# Enthought library imports.
from enthought.logger.api import logger
from enthought.pyface.dock.api import SetStructureHandler


class ViewSetStructureHandler(SetStructureHandler):
    """ The handler used to restore views.

    This is part of the 'dock window' API. It is used to resolve dock control
    IDs when setting the structure of a dock window.

    """

    ###########################################################################
    # 'object' interface.
    ###########################################################################

    def __init__(self, window_layout):
        """ Creates a new handler. """

        self.window_layout = window_layout

        return

    ###########################################################################
    # 'SetStructureHandler' interface.
    ###########################################################################

    def resolve_id(self, id):
        """ Resolves an unresolved dock control *id*. """

        window_layout = self.window_layout
        window        = window_layout.window

        view = window.get_view_by_id(id)
        if view is not None:
            # Get the view's toolkit-specific control.
            #
            # fixme: This is using a 'private' method on the window layout.
            # This may be ok since this is really part of the layout!
            control = window_layout._get_view_control(view)

        else:
            logger.warn('could not restore view [%s]', id)
            control = None
            
        return control

#### EOF ######################################################################