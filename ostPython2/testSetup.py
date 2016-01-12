#!/usr/local/bin/python3

# what happens when a setUp() method fails?

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("/testdir")
        os.chdir(self.dirname)
        assertTrue(os.getcwd()=="/testdir")

    def test_1(self):
        "Verify creation of files is possible"
        for filename in ("one.txt", "two.txt", "three.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
