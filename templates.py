#! /usr/bin/env python

"""Shared templates for odoogen.
"""

import jinja2

def writefile(path, string):
    """Create or empty file with path, and write string to it."""
    with open(path, 'w') as thefile:
        thefile.write(string)

def renderfile(path, template_str, ctx):
    """Create or overwrite file with template rendered with ctx."""
    rendered = jinja2.Template(template_str).render(**ctx)
    writefile(path, rendered + '\n')

TEMPLATE_LICENSE = """
##############################################################################
#
# {{fullname}}
# Copyright (C) {{today.strftime('%Y')}} {{author}} (<{{website}}>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
"""

