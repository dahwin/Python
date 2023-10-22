from contextlib import contextmanager


@contextmanager
def my_context_manager(resource):
    # This is the setup code
    print("Entering the context")

    # Yield the resource, making it available in the 'with' block
    yield resource

    # This is the cleanup code
    print("Exiting the context")
    # Clean up code here (e.g., releasing resources)



resource = None
with my_context_manager(resource) as ctx:
    print('dahyun+darwin')


