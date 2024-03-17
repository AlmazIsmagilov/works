def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered_password = input('Enter password: ')
            if entered_password != password:
                print('Access denied')
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_password('password')
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print(f'Making burger with {type_of_meat} meat, onions={with_onion}, tomatoes={with_tomato}')

result = make_burger('beef', with_onion=True, with_tomato=False)
if result is not None:
    print(result)