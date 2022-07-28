"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""


def deco_doc(new_docstring):

    def wrapped(cls):
        public_method_names = [method for method in dir(cls) if callable(getattr(cls, method)) if not method.startswith('_')]

        for method in public_method_names:
            getattr(cls, method).__doc__ = new_docstring
        return cls
    return wrapped

