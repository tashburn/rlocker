"""
Makes all the "public" methods of an instance (methods without a "_" prefix) locked with an RLock.

Example:

    import rlocker

    class MyClass():
        def __init__(self):
            rlocker.lock(self)
        def method1(self):
            print 'i am synchronized'
        def _method2(self):
            print 'i am not synchronized'

"""

import threading
import inspect

class _LockedWrapper(object):
    def __init__(self, lock, method):
        self.lock = lock
        self.method = method
    def __call__(self, *args, **kwargs):
        with self.lock:
            return self.method(*args, **kwargs)

def lock(obj):
    obj.__locker_lock = threading.RLock()
    for m in inspect.getmembers(obj, predicate=inspect.ismethod):
        method_name = m[0]
        method_to_wrap = m[1]
        if method_name[0] != '_' and not hasattr(method_to_wrap, '__ignore'):
            wrapper = _LockedWrapper(obj.__locker_lock, method_to_wrap)
            setattr(obj, method_name, wrapper)
