

def test_2(self):
    fn = r"binout.bin"
    file_handle = open(fn, 'wb')
    intended_size = 1000000
    file_handle.write(bytes(intended_size))
    file_handle.close()
    actual_size = os.stat(fn).st_size
    self.assertTrue(actual_size==intended_size)
    self.assertEqual(actual_size, intended_size + 1, "Wrong! Looking for {}".format(intended_size))



