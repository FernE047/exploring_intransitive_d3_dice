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

problem I: how many ways can we arrange X, Y, Z values so the relationship "less than or equal" between them is unique, not repeated? (e.g a ≤ b ≤ c ≤ d ≤ e ≤ f ≤ g ≤ h ≤ i)

we calculate this on: `code/counting_possibilities`: 280 ouput saved at `data/dice_set_cases.txt`

however, the equality between values matter in this case because changing x₀ < y₀ to x₀ = y₀ changes the winning relationship between them from a win for dice X to a tie, so we have to consider the cases where values are equal.
we have 280 cases, each one with 8 comparisions ≤, each comparision can be either < or =, so we have 2^8 = 256 combinations of < and = for each case.
totaling 280 * 256 = 71680 combinations of value arrangements. some of these combinations equivalent to each other, for example: 

case 17 and case 18:
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ y₂ ≤ z₂
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ z₂ ≤ y₂
are equivalent when we set y₂ = z₂, because both become:
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ y₂ = z₂
so we have to filter these equivalences out. I propose we do this by generating all combinations, and storing them in a set data structure to ensure uniqueness. when equality is set, we sort equal values to ensure uniqueness.
This is done on `code/generating_equality_cases.py`, output saved at `data/dice_set_all_cases.txt` with 15712 unique combinations.
We sort the output by amount of equalities first, then lexicographically, to make it easier to analyze. first the ones less equalities, then the more equalities. and sorted lexicographically inside each group.
given a comparision arrangement, we can generate the dice comparision results because we know which values are equal and which are not. for example line 217 from `data/dice_set_all_cases.txt`:

x₀<y₀<z₀<x₁<z₁<y₁<z₂<y₂<x₂

gives us the results:

(x₀,x₁,x₂),(y₀,y₁,y₂),(z₀,z₁,z₂)

   y₀ y₁ y₂    z₀ z₁ z₂    x₀ x₁ x₂
x₀ o  o  o  y₀ o  o  o  z₀ x  o  o 
x₁ x  o  o  y₁ x  x  o  z₁ x  x  o 
x₂ x  x  x  y₂ x  x  x  z₂ x  x  o 

where o means win, x means loss, and = means tie.
we can see that Y that beats X, Y beats Z, and Z beats X, so this diceset isn't intransitive. Y is a dominant die.
