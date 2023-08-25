class Singleton(type):
    """
    A metaclass that allows a class to have only one instance.

    This metaclass defines a new type that can be used as a metaclass for
    other classes. When a class is defined with this metaclass, it will
    ensure that only one instance of the class can exist at a time. If
    an instance of the class already exists, calling the constructor again
    will return the existing instance.

    Examples
    --------
    To define a new class that uses the `Singleton` metaclass, simply include
    the metaclass in the class definition:

    >>> class MyClass(metaclass=Singleton):
    ...     pass

    Now, only one instance of the `MyClass` class can exist at a time:

    >>> x = MyClass()
    >>> y = MyClass()
    >>> x is y
    True
    """
    __instance = None

    def __call__(self, *args, **kwargs):
        """
        Create a new instance of the class, or return an existing instance.

        If an instance of the class does not yet exist, create a new instance
        and store it in the `__instance` attribute. If an instance of the class
        already exists, simply return the existing instance.

        Parameters
        ----------
        *args
            Positional arguments passed to the constructor.
        **kwargs
            Keyword arguments passed to the constructor.

        Returns
        -------
        object
            An instance of the class.

        Examples
        --------
        To create a new instance of a class using the `Singleton` metaclass,
        simply call the class constructor as usual:

        >>> class MyClass(metaclass=Singleton):
        ...     def __init__(self, x):
        ...         self.x = x
        ...
        >>> x = MyClass(1)
        >>> y = MyClass(2)
        >>> x.x
        1
        >>> y.x
        1
        """
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance
