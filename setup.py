import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ZakladacSpolku',
      version='0.0.1',
      description=('Průběžná stvaba zakladače spolků'),
      long_description='# zakladac-spolku\nHello world\n\n\n# Požadavky na novou verzi.\n- Uložení pouze vybraných informací z interview do tabulky.\n- Možnost vrátit se k rozdělanému formuláři.\n- Napojení na obchodní rejstřík.\n- Napojení na katarstr nemovitostí.\n- Pokračování interview po vygenerování dokumentů.\n- Checkboxy pro to-do list.\n- "Add another" možnost přídat další pole stejného typu (např. zakladatele spolků)\n- Custom Api volání do [Ecomailu](https://ecomailczv2.docs.apiary.io/#reference/lists/list-subscribe/add-new-subscriber-to-list).\n- Překlad rozhraní do češtiny.\n- Přepínací verze fyzická osoba/právnická osoba.\n- Získání informací z dříve vyplněného interview\n',
      long_description_content_type='text/markdown',
      author='Michal Kuk',
      author_email='michal.kuk@frankbold.org',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[''],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ZakladacSpolku/', package='docassemble.ZakladacSpolku'),
     )

