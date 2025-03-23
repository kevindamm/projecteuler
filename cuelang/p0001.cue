package solutions

import "list"

#limit: 1000

_sum_3: list.Sum([for x in list.Range(0, #limit, 3) {x}])
_sum_5: list.Sum([for x in list.Range(0, #limit, 5) {x}])
_sum_15: list.Sum([for x in list.Range(0, #limit, 15) {x}])

answer: _sum_3 + _sum_5 - _sum_15
