from django.test import TestCase
from querier import method
from django.test import RequestFactory
from django.http import HttpResponse


class MethodTestCase(TestCase):
    factory = RequestFactory()
    urlForTest = '/?name=黃先生&identity=屋主&identity=仲介&city=新北市&phone='

    def test_default(self):
        request = self.factory.get('/')
        self.assertEqual(method.default(
            request, 'identity'), {'$exists': True})

        request = self.factory.get(urlForTest)
        self.assertEqual(method.default(
            request, 'identity'),  {'$in': ['屋主', '仲介']})

    def test_slitPlus(self):
        request = self.factory.get('/')
        self.assertEqual(method.default(
            request, 'identity'), {'$exists': True})

        request = self.factory.get(urlForTest)
        self.assertEqual(method.default(
            request, 'identity'),  {'$in': ['黃先生', '王先生']})
