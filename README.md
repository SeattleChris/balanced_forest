# balanced_forest

Greg has a tree of nodes containing integer data. He wants to insert a node with some non-zero integer value somewhere into the tree. His goal is to be able to cut two edges and have the values of each of the three new trees sum to the same amount. This is called a balanced forest. Being frugal, the data value he inserts should be minimal. Determine the minimal amount that a new node can have to allow creation of a balanced forest. If it's not possible to create a balanced forest, return -1.

## Function Description

Complete the balancedForest function in the editor below. It must return an integer representing the minimum value of  that can be added to allow creation of a balanced forest, or  if it is not possible.

The function balancedForest has the following parameter(s):

* vals: an array of integers, the data values for each node
* edges: an array of 2 element arrays, the node pairs per edge

## Input Format

* The first line contains a single integer, `q`, the number of queries.
* Each of the following  sets of lines is as follows:
  * The first line contains an integer, `n`, the number of nodes in the tree.
  * The second line contains  space-separated integers describing the respective values of , where each  denotes the value at node .
  * Each of the following  lines contains two space-separated integers,  and , describing edge  connecting nodes  and .

## Constraints

Each query forms a valid undirected tree.

## Output Format

For each query, return the minimum value of the integer . If no such value exists, return  instead.
