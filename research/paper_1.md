a dn die is a n-sided structure that when it's rolled can give you any of the n values with equal probabilities 1/n.
a d10 has 10 values, d5 5 values, d256 256 values.
on this paper we are only using d3's so everytime we talk about die and dices, we mean d3.
a d3 consists of 3 values.
the values order can be ignored (1,1,2) = (1,2,1) = (2,1,1). To ensure uniqueness and ignore permutation order, every die is represented as a tuple (a, b, c) ordered such that: a ≤ b ≤ c
diceset is a multiset with n dice, in this paper we are dealing with 3-diceset.
let dice X = (x₀, x₁, x₂), Y = (y₀, y₁, y₂), Z = (z₀, z₁, z₂). and the diceset dD = (X, Y, Z)
We say X > Y if the number of pairs (x_i, y_j) with x_i > y_j exceeds the number with y_j > x_i.
to ensure DiceSet uniqueness we sort the dice based on their first-most values
A dice set (X, Y, Z) is ordered lexicographically by face values:
first by x₀ ≤ y₀ ≤ z₀;
ties are broken by x₁ ≤ y₁ ≤ z₁
remaining ties by x₂ ≤ y₂ ≤ z₂
⇒ x₀ is the smallest first-face among all dice in the set.

problem I: how many ways can we arrange X, Y, Z values so the relationship less than between them is unique, not repeated? (e.g a ≤ b ≤ c ≤ d ≤ e ≤ f ≤ g ≤ h ≤ i)

we calculate this on:

- `code/counting_possibilities`: 280

ouput saved on:

- `data/dice_set_cases.txt`

let's use the values 1, 2, 3, 4, 5, 6, 7, 8 and 9 as test values because they hold that 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9

we have these dice sets, and we test which ones are intransitive on `code/intransitive_exploration`
