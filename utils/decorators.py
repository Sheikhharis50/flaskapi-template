def catch(func, callback=None):
    '''
    Decorator for catching exceptions
    '''

    def wrap_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
            if callback:
                callback()
    return wrap_function
