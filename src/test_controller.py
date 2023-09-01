try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '.'
            )
        )
    )
except:
    raise

from unittest import TestCase, main, mock
from controller import kitestar


def test_testar():
    assert kitestar() == "Teste"