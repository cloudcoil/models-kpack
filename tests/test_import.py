from types import ModuleType

import cloudcoil.models.kpack as kpack


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), kpack.__dict__.values()))
    assert modules, "No modules found in kpack"
