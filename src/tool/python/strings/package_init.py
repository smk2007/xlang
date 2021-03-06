import %
%.init_apartment()

def _import_ns(ns):
    import importlib.machinery
    import importlib.util

    try:
        module_name = "%_" + ns.replace('.', '_')

        loader = importlib.machinery.ExtensionFileLoader(module_name, %.__file__)
        spec = importlib.util.spec_from_loader(module_name, loader)
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module
    except:
        return None
