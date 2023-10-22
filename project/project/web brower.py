import webbrowser
import os
import shlex
import shutil
import sys
import subprocess
import threading
__all__ = ["Error", "open", "open_new", "open_new_tab", "get", "register"]

class Error(Exception):
    pass

_lock = threading.RLock()
_browsers = {}                  # Dictionary of available browser controllers
_tryorder = None                # Preference order of available browsers
_os_preferred_browser = None    # The preferred browser

def register(name, klass, instance=None, *, preferred=False):
    """Register a browser connector."""
    with _lock:
        if _tryorder is None:
            register_standard_browsers()
        _browsers[name.lower()] = [klass, instance]

        # Preferred browsers go to the front of the list.
        # Need to match to the default browser returned by xdg-settings, which
        # may be of the form e.g. "firefox.desktop".
        if preferred or (_os_preferred_browser and name in _os_preferred_browser):
            _tryorder.insert(0, name)
        else:
            _tryorder.append(name)

def get(using=None):
    """Return a browser launcher instance appropriate for the environment."""
    if _tryorder is None:
        with _lock:
            if _tryorder is None:
                register_standard_browsers()
    if using is not None:
        alternatives = [using]
    else:
        alternatives = _tryorder
    for browser in alternatives:
        if '%s' in browser:
            # User gave us a command line, split it into name and args
            browser = shlex.split(browser)
            if browser[-1] == '&':
                return BackgroundBrowser(browser[:-1])
            else:
                return GenericBrowser(browser)
        else:
            # User gave us a browser name or path.
            try:
                command = _browsers[browser.lower()]
            except KeyError:
                command = _synthesize(browser)
            if command[1] is not None:
                return command[1]
            elif command[0] is not None:
                return command[0]()
    raise Error("could not locate runnable browser")

# Please note: the following definition hides a builtin function.
# It is recommended one does "import webbrowser" and uses webbrowser.open(url)
# instead of "from webbrowser import *".

def open(url, new=0, autoraise=True):
    """Display url using the default browser.

    If possible, open url in a location determined by new.
    - 0: the same browser window (the default).
    - 1: a new browser window.
    - 2: a new browser page ("tab").
    If possible, autoraise raises the window (the default) or not.
    """
    if _tryorder is None:
        with _lock:
            if _tryorder is None:
                register_standard_browsers()
    for name in _tryorder:
        browser = get(name)
        if browser.open(url,new,autoraise):
            return True
    return False

# browser = get(name)
#         if browser.open(url, new, autoraise):
#             return True
#     return False