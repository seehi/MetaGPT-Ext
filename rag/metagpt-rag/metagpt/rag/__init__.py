"""MetaGPT RAG package."""

import importlib
import pkgutil


def _try_import_provider_modules():
    """
    Try to import all available provider modules without raising errors if they don't exist.
    This ensures that all provider classes decorated with @register_provider are registered.
    """
    try:
        # First check if the metagpt.provider package exists
        provider_pkg = importlib.import_module("metagpt.provider")
        
        # Get all submodules in the provider package
        for _, name, _ in pkgutil.iter_modules(provider_pkg.__path__, provider_pkg.__name__ + "."):
            try:
                importlib.import_module(name)
            except (ImportError, ModuleNotFoundError):
                pass
    except (ImportError, ModuleNotFoundError):
        raise ImportError("`metagpt.provider` package not found, please run `pip install metagpt-provider-xxx`, xxx is the provider name, such as `metagpt-provider-openai`.")


_try_import_provider_modules()
