import builtins


def print(*args):
    text = ' '.join(str(arg) for arg in args)
    builtins.print(text.upper())
print('Нельзя ли потише?')

