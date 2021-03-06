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
""" The interface for a dialog that allows the user to open/save files etc. """

# Enthought library imports.
from traits.api import Any, Bool, Int, Str

# Local imports.
from pyface.i_dialog import IDialog


class IProgressDialog(IDialog):
    """ A simple progress dialog window which allows itself to be updated
    """

    #### 'IProgressDialog' interface ##################################

    #: The message to display in the dialog
    message = Str

    #: The minimum progress value
    min = Int

    #: The maximum progress value
    max = Int

    #: The margin around the progress bar
    margin = Int(5)

    #: Whether the operation can be cancelled
    can_cancel = Bool(False)

    #: Whether to show progress times
    show_time = Bool(False)

    #: Whether to show progress percent
    show_percent = Bool(False)

    #: Label for the 'cancel' button
    cancel_button_label = Str

    ###########################################################################
    # 'IProgressDialog' interface.
    ###########################################################################

    def update(self, value):
        """ Update the progress bar to the desired value

        If the value is >= the maximum and the progress bar is not contained
        in another panel the parent window will be closed.

        Parameters
        ----------
        value :
            The progress value to set.
        """


class MProgressDialog(object):
    """ The mixin class that contains common code for toolkit specific
    implementations of the IProgressDialog interface.

    Implements: update()
    """

    #: The progress bar toolkit object
    # XXX why not the control?
    progress_bar = Any

    ###########################################################################
    # 'IProgressDialog' interface.
    ###########################################################################

    def update(self, value):
        """ Update the progress bar to the desired value

        If the value is >= the maximum and the progress bar is not contained
        in another panel the parent window will be closed.

        Parameters
        ----------
        value :
            The progress value to set.
        """

        if self.progress_bar is not None:
            self.progress_bar.update(value)

        if value >= self.max:
            self.close()
