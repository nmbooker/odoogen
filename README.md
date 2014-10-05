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

An import line suitable for `__init__.py` is output on STDOUT.

Example usage in VIM is to open up the `__init__.py`, find the area you
usually put your imports, and then do this:

```
:r !odoogen-py new_module_name
```

A new import line is generated thus:

```
from . import new_module_name
```


Now open your new module, for example in a new tab:

```
:tabedit new_module_name.py
```

# odoogen-xmlfile

Create a new XML file with the right tags down to `<data>`

You can run this from your shell, or from `:!` in VIM.

It just takes the name of the file, e.g.

```
$ odoogen-xmlfile my_view.xml
```

Registering the XML file in your `__openerp__.py` is left to you
at the moment.

# odoogen-viewblock

Given the options you give it on the command line, this will generate
a skeleton block of XML that inherits and overrides a specific GUI view
in ir.ui.view.

This is designed to be run in a text editor that supports inserting
lines of text above or below the cursor from the output of a command.

In VIM, you might use:

```
:r !odoogen-viewblock res.partner -I base.res_partner_form -N res.partner.form
```

# odoogen-fieldtags

Given a list of field names, one per line, on STDIN, puts each field
name into a `<field name="field_name"/>` tag on STDOUT.

So it just saves typing the XML tag around it each time.

In VIM, you can write out a list of field names in the location in the
XML file you want them to appear:

```
field1
field2
field3
```

Then do a LINE VISUAL select with Shift-V to select the three field names.

Then, with the lines still selected, do:

```
!odoogen-fieldtags
```

and your selected text will be replaced with this:

```
                    <field name="field1"/>
                    <field name="field2"/>
                    <field name="field3"/>
```
