# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

import unittest
from random import randint
from .. import Server
from ..util import tmux
from .helpers import TmuxTestCase, TEST_SESSION_PREFIX
from . import t

from .. import log
import logging

logger = logging.getLogger(__name__)


class ServerTest(TmuxTestCase):

    def test_has_session(self):
        self.assertTrue(t.has_session(self.TEST_SESSION_NAME))
        self.assertFalse(t.has_session('asdf2314324321'))

    def test_socket_name(self):
        """ ``-L`` socket_name.

        ``-L`` socket_name  file name of socket. which will be stored in
               env TMUX_TMPDIR or /tmp if unset.)

        """
        myserver = Server(socket_name='test')

        self.assertEqual(myserver.socket_name, 'test')

    def test_socket_path(self):
        """ ``-S`` socket_path  (alternative path for server socket). """

        myserver = Server(socket_path='test')

        self.assertEqual(myserver.socket_path, 'test')

    def test_config(self):
        """ ``-f`` file for tmux(1) configuration. """

        myserver = Server(config_file='test')
        self.assertEqual(myserver.config_file, 'test')

if __name__ == '__main__':
    unittest.main()
