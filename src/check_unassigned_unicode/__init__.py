#!/usr/bin/env python

"""
Check for unassigned unicode data

Checks for unassigned unicode codepoints in unicode 3.2

Wraps around the pyxmpp function since it works very
well. Eventually, we will want to rewrite this
to use our own functionality

See: http://docs.python.org/library/stringprep.html
"""

import xmppstringprep_new as xsp


def is_unassigned_unicode(data):
    """
    Check if is unassigned unicode.
    """
    if isinstance(data, str):
        data = unicode(data, 'utf-8')
    else:
        data = unicode(data)
    if not hasattr(is_unassigned_unicode, '_prof'):
        is_unassigned_unicode._prof = xsp.Profile(
            unassigned=(xsp.A_1,),
            mapping=(xsp.B_1, xsp.B_2),
            normalization=xsp.nfkc,
            prohibited=(
                xsp.C_2_1,
                xsp.C_2_2,
                xsp.C_3,
                xsp.C_4,
                xsp.C_5,
                xsp.C_6,
                xsp.C_7,
                xsp.C_8,
                xsp.C_9
            ), bidi=1
        )
    try:
        is_unassigned_unicode._prof.prepare(data)
    except xsp.StringprepError:
        return True
    else:
        return False
