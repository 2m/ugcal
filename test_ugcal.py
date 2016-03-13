from __future__ import absolute_import

from ugcal import UGCal


def test_existing_events_by_links():
    php_meetup = {
        'link': 'http://www.meetup.com/php_meetup/events/123456/'
    }
    js_meetup = {
        'link': 'http://www.meetup.com/js_meetup/events/654321/'
    }

    php_event = {
        'description': 'lorem ipsum http://www.meetup.com/php_meetup/events/123456/ somehting else.'  # noqa
    }
    ruby_event = {
        'description': ''
    }

    meetups = [php_meetup, js_meetup]
    gcal_events = [php_event, ruby_event]

    result = UGCal.find_existing_events(meetups, gcal_events)
    assert {
        'http://www.meetup.com/php_meetup/events/123456/': php_event
    } == result


def test_filter_events_to_create():
    old_php_meetup = {
        'link': 'http://www.meetup.com/php_meetup/events/123456/'
    }
    new_php_meetup = {
        'link': 'http://www.meetup.com/php_meetup/events/987654/'
    }

    meetups = [old_php_meetup, new_php_meetup]
    existing = {
        'http://www.meetup.com/php_meetup/events/123456/': old_php_meetup
    }

    result = UGCal.filter_for_creation(meetups, existing)
    assert {
        'http://www.meetup.com/php_meetup/events/987654/': new_php_meetup
    } == result
