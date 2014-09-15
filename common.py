
"""Common code shared among odoogen utilities.
"""

import sys

def die(errno, errmsg):
    """Display errmsg on stderr and exit script with errno."""
    sys.stderr.write(errmsg + '\n')
    sys.exit(errno)
