"""Tests for Datetime.py"""

import pytz
import pytest
from datetime import datetime


from StockScraper.Generic.timeoperations import TimeOperate


def test_to_utc():
    t = datetime(2017, 6, 30, hour=12, minute=0, tzinfo=pytz.timezone('Europe/Warsaw'))
    assert TimeOperate.to_utc(t).hour == 10
    t = datetime(2017, 6, 30, hour=12)
    assert TimeOperate.to_utc(t).hour == 12
    with pytest.raises(TypeError) as excinfo:
        TimeOperate.to_utc('test')
    assert 'Provided object is not instance of datetime.' in str(excinfo.value)


def test_datetime_to_epoch():
    t = datetime(1970, 1, 1, hour=0, minute=0, tzinfo=pytz.utc)
    assert TimeOperate.datetime_to_epoch(t) == 0
    with pytest.raises(TypeError) as excinfo:
        TimeOperate.datetime_to_epoch('test')
    assert 'Provided object is not instance of datetime.' in str(excinfo.value)


def test_days_in_epoch():
    t = datetime(1970, 1, 2, hour=0, minute=0, tzinfo=pytz.utc)
    assert TimeOperate.days_in_epoch(t) == 86400000
    with pytest.raises(TypeError) as excinfo:
        TimeOperate.days_in_epoch('test')
    assert 'Provided object is not instance of datetime.' in str(excinfo.value)
