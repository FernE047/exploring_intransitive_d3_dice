a dn die is a n-sided structure that when it's rolled can give you any of the n values with equal probabilities 1/n.
a d10 has 10 values, d5 5 values, d256 256 values.
on this paper we are only using d3's so everytime we talk about die and dice, we mean d3.
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
totaling 280 * 256 = 71680 combinations of value arrangements. 
Two arrangements are considered equivalent if they induce the same partial order over {x₀,…,z₂}. We canonicalize each by collapsing equal elements and sorting within equality classes, for example: 
case 17 and case 18:
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ y₂ ≤ z₂
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ z₂ ≤ y₂
are equivalent when we set y₂ = z₂, because:
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ y₂ = z₂
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ z₂ = y₂
both reduce to:
x₀ ≤ x₁ ≤ y₀ ≤ x₂ ≤ z₀ ≤ y₁ ≤ z₁ ≤ y₂ = z₂
so we have to filter these equivalences out. I propose we do this by generating all combinations, and storing them in a set data structure to ensure uniqueness. when equality is set, we sort equal values to ensure uniqueness.
Sorting equal values ensures that different syntactic descriptions of the same partial order are mapped to a unique representative.
This is done on `code/generating_equality_cases.py`, output saved at `data/dice_set_all_cases.txt` with 15712 unique combinations.
We sort the output by amount of equalities first, then lexicographically, to make it easier to analyze. first the ones less equalities, then the more equalities. and sorted lexicographically inside each group.

so we solve Problem I: 15712 unique arrangements of values with < and = comparisions.

Problem II: given all the comparision arrangements from Problem I, how many of these arrangements produce intransitive dicesets?

to solve this we have to generate the diceset winning results from each arrangement.
to compare two values a and b given a comparision, we find where they are positioned in the arrangement, and if there's at least one < between them, the left one loses to the right one, otherwise they tie.

for easier visualization, we can use a table to represent the results of comparing two dice X, Y, Z., where each cell represents the result of comparing one face of a die to one face of another die. 

in this paper 1 means win, -1 means loss, and 0 means tie.
let S(A, B) be the score of die A against die B, where A is the row die and B is the column die, calculated as:
S(A, B) = sum(a in A){sum(b in B){sgn(a - b)}}
where sgn(x) is 1 if positive, -1 if negative, and 0 if 0.
If S(A, B) > 0, A wins. If < 0, B wins. if = 0, they tie.
Note that S(A,B) = -S(B,A), hence the dominance relation is antisymmetric.

For example line 217 from `data/dice_set_all_cases.txt`:

x₀<y₀<z₀<x₁<z₁<y₁<z₂<y₂<x₂

gives us the results:

(x₀,x₁,x₂),(y₀,y₁,y₂),(z₀,z₁,z₂)

   y₀ y₁ y₂    z₀ z₁ z₂    x₀ x₁ x₂
x₀ -1 -1 -1 y₀ -1 -1 -1 z₀  1 -1 -1
x₁  1 -1 -1 y₁  1  1 -1 z₁  1  1 -1
x₂  1  1  1 y₂  1  1  1 z₂  1  1 -1

We observe that Y > X, Y > Z, and Z > X.
Since Y defeats both other dice, this DiceSet is transitive with Y as a dominant die, and therefore not intransitive.

To find intransitive dicesets, we check if there is a cycle in the winning relationships: X > Y, Y > Z, Z > X.
Note that intransitive dicesets cannot have any ties, because ties would prevent the formation of a strict cycle of wins.
This is implemented on `code/intransitive_exploration.py`, output saved at `data/intransitive_dice_sets.txt` with ???? intransitive dicesets found. #TODO: the code needs to be modified to not use numerical values for the comparisions, instead use the symbolic representation from `data/dice_set_all_cases.txt`.