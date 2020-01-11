def test1():
    import erajs.Managers.EventManager as Event
    e = Event.EventManager()
    assert e.get_listener_list() == []