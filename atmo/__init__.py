#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Guadeloupe (French West Indies) ATMO pollution indicator (from 1 to 10).

This module grabs ATMO pollution indicator from Gwadair.com website and show
a digest of these data.

This module was created to work in Guadeloupe but should be usable in other
areas with obervatory using iseo module as well.
"""

__author__ = "Olivier Watte"
__copyright__ = "Copyright (c) 2016 Olivier Watte"
__license__ = "GPL-V3+"
__all__ = ['Atmo', 'run', ]


def get_version(version, alpha_num=None, beta_num=None,
                rc_num=None, post_num=None, dev_num=None):
    """Manage version number according to PEP 386.

    The less advanced version is chosed.
    eg. in case of alpha, beta and rc, the version is shown as alpha.

    Args:
        version(tuple): actual version number eg. : (0,0,1) ou (2,0,4)
        alpha_num: set version as alpha
        beta_num: set version as beta
        rc_num: set version as release candidate
        post_num: set version as post dev
        dev_num: set version as in dev

    Returns:
        formatted version number (str)
    """
    num = "%s.%s" % (int(version[0]), int(version[1]))
    if version[2]:
        num += ".%s" % int(version[2])

    letter_marker = False  # permet de sortir si on a un marqueur lettre
    if alpha_num:
        num += "a%s" % int(alpha_num)
        letter_marker = True

    if beta_num and not letter_marker:
        num += "b%s" % int(beta_num)
        letter_marker = True

    if rc_num and not letter_marker:
        num += "rc%s" % int(rc_num)

    if post_num:
        num += ".post%s" % int(post_num)

    if dev_num:
        num += ".dev%s" % int(dev_num)

    return num

__version__ = get_version((0, 0, 1), beta_num=1, dev_num=1)
