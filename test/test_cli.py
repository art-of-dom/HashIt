'''
Tests for the cli interface
'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_equals, assert_true
from hashit.cli import cli_main
import sys

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.args = {
            '--hash-type': None,
            '-f': False,
            '<input>': None
        }

    def tearDown(self):
        pass

    def test_cil_retruns_error_if_no_args(self):
        assert_equals(1, cli_main(None))

    def test_cil_retruns_success_no_vaild_args(self):
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_uppercase(self):
        self.args['--hash-type'] = 'CRC32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_lowercase(self):
        self.args['--hash-type'] = 'crc32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_mixedcase(self):
        self.args['--hash-type'] = 'cRc32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_error_unknown_hash(self):
        self.args['--hash-type'] = 'foobar'
        assert_equals(1, cli_main(self.args))
        self.assertEqual("Unknown hash type foobar",
            sys.stdout.getvalue().strip()
        )

    def test_cil_uses_default_hash_on_file(self):
        self.args['-f'] = True
        self.args['<input>'] = 'test/support/example.bin'
        assert_equals(0, cli_main(self.args))
        self.assertEqual("file: test/support/example.bin hash: BAD3",
            sys.stdout.getvalue().strip()
        )
