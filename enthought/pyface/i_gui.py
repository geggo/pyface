#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" The interface of a pyface GUI. """


# Standard library imports.
import logging
import os.path

# Enthought library imports.
from enthought.etsconfig.api import ETSConfig
from enthought.io.api import File
from enthought.traits.api import Bool, Interface, Unicode


# Logging.
logger = logging.getLogger(__name__)


class IGUI(Interface):
    """ The interface of a pyface GUI. """

    #### 'GUI' interface ######################################################

    # Is the GUI busy (i.e. should the busy cursor, often an hourglass, be
    # displayed)?
    busy = Bool(False)

    # Has the GUI's event loop been started?
    started = Bool(False)

    # A directory on the local file system that we can read and write to at
    # will.  This is used to persist layout information etc.  Note that
    # individual toolkits will have their own directory.
    state_location = Unicode

    ###########################################################################
    # 'object' interface.
    ###########################################################################

    def __init__(self, splash_screen=None):
        """ Initialise a new GUI.  splash_screen is an optional splash screen
        that will be displayed until the event loop is started.
        """

    ###########################################################################
    # 'GUI' class interface.
    ###########################################################################

    def invoke_after(cls, millisecs, callable, *args, **kw):
        """ Call a callable after a specific delay in the main GUI thread. """

    invoke_after = classmethod(invoke_after)

    def invoke_later(cls, callable, *args, **kw):
        """ Call a callable in the main GUI thread. """

    invoke_later = classmethod(invoke_later)

    def set_trait_after(cls, millisecs, obj, trait_name, new):
        """ Sets a trait after a specific delay in the main GUI thread. """

    set_trait_after = classmethod(set_trait_after)

    def set_trait_later(cls, obj, trait_name, new):
        """ Sets a trait in the main GUI thread. """

    set_trait_later = classmethod(set_trait_later)

    ###########################################################################
    # 'GUI' interface.
    ###########################################################################

    def start_event_loop(self):
        """ Start the GUI event loop. """

    def stop_event_loop(self):
        """ Stop the GUI event loop. """


class MGUI(object):
    """ The mixin class that contains common code for toolkit specific
    implementations of the IGUI interface.

    Implements: _state_location_default()
    """

    def _state_location_default(self):
        """ Trait initializer. """

        state_location = os.path.join(ETSConfig.application_home, 'pyface', ETSConfig.toolkit)

        try:
            File(state_location).create_folders()

        except ValueError:
            # The folders already exist.
            pass

        logger.debug('GUI state location is [%s]', state_location)

        return state_location

#### EOF ######################################################################
