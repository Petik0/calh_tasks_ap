"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps
import inspect

def require_typing(fn):

    is_all_params = True

    @wraps(fn)
    def wrapper(*args, **kwargs):
        inspect_result = inspect.getfullargspec(fn)
        params = list(inspect_result[0])
        type_hints = inspect_result[6]

        params.append('return')

        print(params)
        print(type_hints.keys())

        nonlocal is_all_params
        for param in params:
            if param not in list(type_hints.keys()):
                is_all_params = False

        if not is_all_params:
            return f"Add typing to function {fn.__name__}, please!"
        else:
            return fn(*args, **kwargs)

    return wrapper
