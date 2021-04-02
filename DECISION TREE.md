# DECISION TREE

It is a graphical representation of all possible solutions to a decision based on certain conditions

### Terms used in Decision Tree

**1) Root Node** : 

The entire population of the sample is given as input and further gets divided into two or more homogeneous sets

**2) Leaf Node :**

 Node cannot be segregated further

**3) Splitting :**

It is dividing the node into different parts on the basis of some condition

**4) Branch :**

Formed by splitting the tree

**5) Pruning :**

Basically removing unwanted branch from the tree

###  Values to be found out

**1) Entropy :**

It measures impurity of something
$$
E(s) = -P(yes) * log ~2~ P(yes) - P(no) * log ~2~ P(no)
$$


**2) Information : **
$$
I(x) = [[weighted Avg] * E(each Feature)]
$$
**3) Information Gain : **
$$
Gain(x) = E(x) - I(x)
$$

**4) Gini Index**:

First find gini value of each branch using formula given , 
$$
1-\sum_1^i P~i~^2
$$
Then :
$$
Gini Index= \sum[Weighted Average]*Gini Value
$$
Gini Index Varies from 0 to 1

if the node divides the branches correctly than <u>Gini Index is 0</u>





#### Now which attribute has better information gain select that to divide the tree further ####

Consider an example : 





