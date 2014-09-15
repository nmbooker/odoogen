odoogen
=======

Code generators for Odoo

# odoogen-mod

Create a new Odoo addon directory, with a skeleton `__openerp__.py` and an
`__init__.py`.

The technical name is taken as the command line argument.

Full name, summary, author and website are prompted for on the command line.

# odoogen-py

Generate an additional skeleton Python file (such as you would import inside
you `__init__.py`) on the current working directory.

Takes the target module name (i.e. without the `.py`) on command line.

Key data for the copyright section is taken from the `__openerp__.py` 
in the present working directory (no need to enter all that stuff again).
