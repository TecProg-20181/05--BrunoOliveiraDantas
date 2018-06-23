# -*- coding: utf-8 -*-
import unittest

from diskspace import *

class TestDiskSpace(unittest.TestCase):
    
    def test_subprocess_check_output(self):
    	result = "24\t/home/bruno/UnB/6\xc2\xba_Semestre/TecProg/05--BrunoOliveiraDantas/diskspace\n"

    	abs_directory = os.path.abspath('.') 
    	cmd = "du -d 1" + abs_directory 

    	self.assertNotEqual(subprocess_check_output(cmd), result, 
    					'Deve ser posto o caminho do seu diretório.')


    def test_bytes_to_readable(self):
        blocks = 0
        self.assertEqual(bytes_to_readable(blocks), '0.00B')

    def test_kbytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), '50.00Kb') 

    def test_mbytes_to_readable(self):
        blocks = 1000000
        self.assertEqual(bytes_to_readable(blocks), '488.28Mb')

    def test_gbytes_to_readable(self):
        blocks = 1000000000
        self.assertEqual(bytes_to_readable(blocks), '476.84Gb')

if __name__ == '__main__':
    unittest.main()