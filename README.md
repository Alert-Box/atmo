# atmo
Guadeloupe (French West Indies) ATMO pollution indicator (from 1 to 10).

This module grabs ATMO pollution indicator from gwadair.com website and show
a digest of these data.

This module was created to work in Guadeloupe but should be usable in other
areas with observatory monitoring pollution using ISEO module as well.

It can be used as command line tool or as python module.

## Indice Atmo

The indice ATMO is the pollution indicator from 1 (very good) to 10 (very bad).
It's used to show simply the global air quality in a city.

See http://www.airparif.asso.fr/reglementation/indice-qualite-air-francais#

Actually, this tools works only for Guadeloupe and parse some json files
generated by a module called "ISEO". Thus this tool should work with data using
the same format. Just put your values in the atmo.cfg file.

# install

## using pip

    pip install atmo

## from source

    git clone https://github.com/Alert-Box/atmo
    cd atmo
    python setup.py install

# Usage example

## Command Line
    $ atmo

## Python Module

    >>> from atmo.atmo import Atmo
    >>> ia = Atmo()
    >>> print ia.info()
    ['ATMO Friday 15 July 2016', "Aujourd'hui : Bon (VERT [4])", 'Demain : Moyen (ORANGE [5])']

# Licence

Atmo is a Free Software and is licensed under the GNU General Public License (GPL) Version 3 or later.

## 	GNU General Public License (GPL) Version 3 or later

[![GNU GPL v3.0](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl.html)

View official GNU site <http://www.gnu.org/licenses/gpl.html>.

[![OSI](http://opensource.org/trademarks/opensource/OSI-Approved-License-100x137.png)](http://opensource.org/licenses/mit-license.php)

[View the Open Source Initiative site.](http://opensource.org/licenses/mit-license.php)
