args=$*
python inner.py $args | swipl --quiet --nosignals | python outer.py
