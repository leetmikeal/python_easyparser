python_easyparser
=================

"lite parser for python script"
This program can parse your python script


USAGE:

  python easyparser.py <python script>


If you want to analyte multiple file, can use below shell script.

>>>
#!/bin/bash
files=(
change_as2sge.py  mmgbsa_decomp.py  renamePDB.py
)
for f in ${files[@]}; do
  echo "--start-- "${f}
  python list_function.py ${f}
  echo "--end-- "${f}
  echo ""
done
<<<


CAN:

* list the functions
* list arguments in each functions

only...


Please let me know what you want to parse.

enjoy !

