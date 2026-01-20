a dn die is a n-sided structure that when it's rolled can give you any of the n values with equal probabilities.
a d10 has 10 values, d5 5 values, d256 256 values.
on this paper we are only using d3's so everytime we talk about die and dices, we mean d3.
a d3 consists of 3 values #Work in progress

given three die (x_0, y_0, z_0), (x_1, y_1, z_1) and (x_2, y_2, z_2)

we can have a < b < c < d < e < f < g < h < i, how many possibilities, there are?

9!

9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

however, a few rules are always true:

x_0 < y_0 < z_0
x_1 < y_1 < z_1
x_2 < y_2 < z_2

and the dices are interchangeable

we calculate this on:

- `code/counting_possibilities`: 280

ouput saved on:

- `data/dice_set_cases.txt`

let's use the values 1,2,3,4,5,6,7,8 and 9 as test values because they hold that 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9

we have these dice sets, and we test which ones are intransitive on `code/intransitive_exploration`