#coding:utf-8

import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        responese = urllib2.urlopen(url)

        if responese.getcode() != 200:
            return None

        return responese.read()



