# -*- coding: utf-8 -*- 

import unittest
from NumberToWords import NumberToWords

class testNumberToWord(unittest.TestCase):

    def test_cardinal(self):
            self.assertEqual(NumberToWords(12, to='cardinal', lang='ar'), 'اثنا عشر')
            self.assertEqual(NumberToWords(-8324, to='cardinal', lang='ar'),
                            'سالب ثمانية آلاف  و ثلاثمائة و أربعة و عشرون')
            self.assertEqual(
                NumberToWords(3431.12, to='cardinal', lang='ar'),
                'ثلاثة آلاف  و أربعمائة و واحد و ثلاثون  , اثنتا عشرة')
            self.assertEqual(NumberToWords(431, to='cardinal', lang='ar'),
                            'أربعمائة و واحد و ثلاثون')
            self.assertEqual(NumberToWords(94231, to='cardinal', lang='ar'),
                            'أربعة و تسعون ألفاً  و مئتان و واحد و ثلاثون')
            self.assertEqual(NumberToWords(1431, to='cardinal', lang='ar'),
                            'واحد ألف  و أربعمائة و واحد و ثلاثون')

if __name__ == '__main__':
    unittest.main()