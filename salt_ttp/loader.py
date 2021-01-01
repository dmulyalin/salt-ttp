"""
Define the required entry-points functions in order for Salt to know
what and from where it should load this plugin's loaders
"""
import os

PKG_DIR = os.path.abspath(os.path.dirname(__file__))


def module_dirs():
    """
    Return a list of paths from where salt should load execution modules
    """
    return [os.path.join(PKG_DIR, "modules")]


def runner_dirs():
    """
    Return a list of paths from where salt should load runner modules
    """
    return [os.path.join(PKG_DIR, "runners")]
