from unittest import TestCase
from py2emap.py2emap import py2emap


class Test(TestCase):
    def test_dumps_simple1(self):
        o = {'a': 123, 'b': 'Hello', 'c': 'World'}
        actual = py2emap.dumps(o)
        expect = 'l$#3$#v$#k0$#a$#v0$#123$#t0$#number$#k1$#b$#v1$#Hello$#t1$#string$#k2$#c$#v2$#World$#t2$#string$#'
        self.assertEqual(expect, actual)

    def test_dumps_simple2(self):
        o = [1, 2, 3]
        actual = py2emap.dumps(o)
        expect = 'l$#4$#v$#k0$#length$#v0$#3$#t0$#number$#k1$#_0_$#v1$#1$#t1$#number$#k2$#_1_$#v2$#2$#t2$#number$#k3$#_2_$#v3$#3$#t3$#number$#'
        self.assertEqual(expect, actual)

    def test_dumps_complex1(self):
        o = {
            "id": 123,
            "name": "rhenium",
            "isPublic": True,
            "accounts": [
                {
                    "type": "github",
                    "link": "https://github.com/rheniumNV"
                },
                {
                    "type": "twitter",
                    "link": "https://twitter.com/rhenium_nv"
                }
            ]
        }
        actual = py2emap.dumps(o)
        expect = 'l$#8$#v$#k0$#id$#v0$#123$#t0$#number$#k1$#name$#v1$#rhenium$#t1$#string$#k2$#isPublic$#v2$#true$#t2$#bool$#k3$#accounts.length$#v3$#2$#t3$#number$#k4$#accounts_0_.type$#v4$#github$#t4$#string$#k5$#accounts_0_.link$#v5$#https://github.com/rheniumNV$#t5$#string$#k6$#accounts_1_.type$#v6$#twitter$#t6$#string$#k7$#accounts_1_.link$#v7$#https://twitter.com/rhenium_nv$#t7$#string$#'
        self.assertEqual(expect, actual)

    def test_dumps_complex2(self):
        o = {
            "keyA": 123,
            "keyD": "valueD",
            "keyB": ["valueB-A", "valueA-B"],
            "keyC": {"keyC-A": "valueC-A",
                     "keyC-B": "valueC-B"},
            "keyE": [{"keyE-A-A": "valueE-A-A", "keyE-A-B": "valueE-A-B"},
                     {"keyE-B-A": "value-E-B-A", "keyE-B-B": "keyE-B-B"}]}
        actual = py2emap.dumps(o)
        expect = 'l$#12$#v$#k0$#keyA$#v0$#123$#t0$#number$#k1$#keyD$#v1$#valueD$#t1$#string$#k2$#keyB.length$#v2$#2$#t2$#number$#k3$#keyB_0_$#v3$#valueB-A$#t3$#string$#k4$#keyB_1_$#v4$#valueA-B$#t4$#string$#k5$#keyC.keyC-A$#v5$#valueC-A$#t5$#string$#k6$#keyC.keyC-B$#v6$#valueC-B$#t6$#string$#k7$#keyE.length$#v7$#2$#t7$#number$#k8$#keyE_0_.keyE-A-A$#v8$#valueE-A-A$#t8$#string$#k9$#keyE_0_.keyE-A-B$#v9$#valueE-A-B$#t9$#string$#k10$#keyE_1_.keyE-B-A$#v10$#value-E-B-A$#t10$#string$#k11$#keyE_1_.keyE-B-B$#v11$#keyE-B-B$#t11$#string$#'
        self.assertEqual(expect, actual)

    def test_dump_complex3(self):
        o = {'a': ['Hello', 'World'], 'b': [{'c': 1, 'd': 2}]}
        actual = py2emap.dumps(o)
        expect = 'l$#6$#v$#k0$#a.length$#v0$#2$#t0$#number$#k1$#a_0_$#v1$#Hello$#t1$#string$#k2$#a_1_$#v2$#World$#t2$#string$#k3$#b.length$#v3$#1$#t3$#number$#k4$#b_0_.c$#v4$#1$#t4$#number$#k5$#b_0_.d$#v5$#2$#t5$#number$#'
        self.assertEqual(expect, actual)

    def test_dumps_escape1(self):
        o = {'k0': r'\test', 'v0': '$#value'}
        actual = py2emap.dumps(o)
        expect = r'l$#2$#v$#k0$#k0$#v0$#\\test$#t0$#string$#k1$#v0$#v1$#$\#value$#t1$#string$#'
        self.assertEqual(expect, actual)

    def test_dumps_escape2(self):
        o = {'k\ey1': r'test', 'k$#ey2': 'value'}
        actual = py2emap.dumps(o)
        expect = r'l$#2$#v$#k0$#k\ey1$#v0$#test$#t0$#string$#k1$#k$#ey2$#v1$#value$#t1$#string$#'
        self.assertEqual(expect, actual)

    def test_dumps_escape3(self):
        o = {'key1': [r'v\alue1', r'v$#alue2', r'v\\alue3', r'v$#$#alue4']}
        actual = py2emap.dumps(o)
        expect = r'l$#5$#v$#k0$#key1.length$#v0$#4$#t0$#number$#k1$#key1_0_$#v1$#v\\alue1$#t1$#string$#k2$#key1_1_$#v2$#v$\#alue2$#t2$#string$#k3$#key1_2_$#v3$#v\\\\alue3$#t3$#string$#k4$#key1_3_$#v4$#v$\#$\#alue4$#t4$#string$#'
        self.assertEqual(expect, actual)
