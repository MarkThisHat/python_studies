import inspect

class Inspec:
    @staticmethod
    def dir_with_newlines(obj):
        """Prints the attributes of an object, each on a new line."""
        attributes = dir(obj)
        print("\n".join(attributes))

    @staticmethod
    def namespace(obj):
        """Prints the namespace (attributes and methods) of a class or object."""
        attributes = obj.__dict__
        for key, value in attributes.items():
            print(f"{key}: {value}")

    @staticmethod
    def members(obj):
        """Uses the inspect module to list all members of an object."""
        members = inspect.getmembers(obj)
        for member in members:
            print(member)

    @staticmethod
    def source_code(obj):
        """Prints the source code of a class or method if available."""
        try:
            source_code = inspect.getsource(obj)
            print(source_code)
        except TypeError:
            print("Source code not available for this object.")

    @staticmethod
    def info(obj):
        """Prints the help documentation of an object."""
        help(obj)

    @staticmethod
    def method_resolution_order(cls):
        """Prints the Method Resolution Order (MRO) of a class."""
        print(cls.__mro__)

    @staticmethod
    def vars_formatted(obj):
        """Prints the __dict__ attribute of an object, which contains its attributes."""
        try:
            attributes = vars(obj)
        except TypeError:
            print("vars() not available for this object.")
            return

        for key, value in attributes.items():
            print(f"{key}: {value}")

    @staticmethod
    def all(obj):
        """Calls all the information methods, handling differences between vars() and __dict__."""
        print("Directory of the object (with newlines):")
        Inspec.dir_with_newlines(obj)
        print("\nNamespace (attributes and methods):")
        try:
            attributes = vars(obj)
            print("Using vars():")
            for key, value in attributes.items():
                print(f"{key}: {value}")
        except TypeError:
            print("vars() is not available for this object. Trying __dict__ instead:")
            try:
                attributes = obj.__dict__
                for key, value in attributes.items():
                    print(f"{key}: {value}")
            except AttributeError:
                print("Neither vars() nor __dict__ are available for this object.")

        print("\nMembers of the object:")
        Inspec.members(obj)
        print("\nSource code of the object:")
        Inspec.source_code(obj)
        print("\nHelp documentation of the object:")
        Inspec.info(obj)
        if inspect.isclass(obj):
            print("\nMethod Resolution Order (MRO):")
            Inspec.method_resolution_order(obj)