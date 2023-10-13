# -*- encoding: utf-8 -*-
import pytest


@pytest.mark.search
class TestSearch(object):
    def test_search(self, home, mylog):
        home.google_search()
        mylog.info("google_search1")
        mylog.error("google_search2")
        mylog.warning("google_search3")
        home.force_wait(3)