# balanced_forest

Greg has a tree of nodes containing integer data. He wants to insert a node with some non-zero integer value somewhere into the tree. His goal is to be able to cut two edges and have the values of each of the three new trees sum to the same amount. This is called a balanced forest. Being frugal, the data value he inserts should be minimal. Determine the minimal amount that a new node can have to allow creation of a balanced forest. If it's not possible to create a balanced forest, return -1.

## Function Description

Complete the balancedForest function in the editor below. It must return an integer representing the minimum value of `c[w]` that can be added to allow creation of a balanced forest, or `-1` if it is not possible.

The function balancedForest has the following parameter(s):

* vals: an array of integers, the data values for each node
* edges: an array of 2 element arrays, the node pairs per edge

## Input Format

* The first line contains a single integer, `q`, the number of queries.
* Each of the following `q` sets of lines is as follows:
  * The first line contains an integer, `n`, the number of nodes in the tree.
  * The second line contains `n` space-separated integers describing the respective values of `vals[1], vals[2], ..., vals[n]`, where each `vals[i]` denotes the value at node `i`.
  * Each of the following `n-1` lines contains two space-separated integers, `x[j]` and `y[j]`, describing edge `j` connecting nodes `x[j]` and `y[j]`.

## Constraints

* 1 <= q <= 5
* 1 <= n <= 5 x 10^4
* 1 <= vals[i] <= 10^9
* Each query forms a valid undirected tree.

## Output Format

For each query, return the minimum value of the integer `vals[w]`. If no such value exists, return `-1` instead.
