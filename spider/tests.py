from unittest import TestCase
from djsite.middle import RequestBeautyMiddleWare
# Create your tests here.
import re
dictRe = re.compile("(\w+)\[(\w+)\]")
listRe = re.compile("(\w+)\[(\d+)\]\[(\w+)\]")


class UnitTest(TestCase):

    def middle_ware_test(self):
        self.assertListEqual(listRe.findall("a[0][name]")[0],('a','0','name'))