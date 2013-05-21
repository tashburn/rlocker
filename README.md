rlocker
=======

A python util that wraps all the "public" methods (without "_" prefix) of a class with an RLock.

This makes it easy to prevent concurrency errors when you want all the state within a class to be synchronized when accessed outside the class. When you add a new method, you don't have to remember to add "with self._rlock:" at the beginning of the method implementation.

Example Usage:

    import rlocker

    class MyClass():
        def __init__(self):
            rlocker.lock(self)
        def method1(self):
            print 'i am synchronized'
        def _method2(self):
            print 'i am not synchronized'
