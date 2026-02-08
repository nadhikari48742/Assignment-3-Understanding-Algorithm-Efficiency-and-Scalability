# Assignment-3-Understanding-Algorithm-Efficiency-and-Scalability
- The first section of this assignment is to assess the performance of randomized Quicksort algorithm. The algorithm has shown good performance in all input types because as indicated by the pivot being chosen uniformly at random.

- - Deterministic Quicksort, first element as pivot, behaves very differently because the behavior is dependent on input order.
 
  - results
 
  - 
=== n=1000 (median of 7 trials) ===

[random]
randomized: 0.001261079999494541
deterministic: 0.0027708899997378467

[sorted]
randomized: 0.0011123200001748046
deterministic: 0.0031440000002476154

[reverse]
randomized: 0.0018122599994967459
deterministic: 0.05653231500036782

[repeated]
randomized: 0.0003060509998249472
deterministic: 0.00033900099970196607

=== n=5000 (median of 7 trials) ===

[random]
randomized: 0.012593799000569561
deterministic: 0.010170279000703886

[sorted]
randomized: 0.009983388999899034
deterministic: 0.04734861599990836

[reverse]
randomized: 0.011013280000042869
deterministic: 1.0566326449998087

[repeated]
randomized: 0.000961708999966504
deterministic: 0.0012100200001441408

=== n=10000 (median of 7 trials) ===

[random]
randomized: 0.01461643900074705
deterministic: 0.016060138000284496

[sorted]
randomized: 0.01320272799966915
deterministic: 0.09263853300035407

[reverse]
randomized: 0.012654459000259521
deterministic: 4.442789511999763

[repeated]
randomized: 0.0018062799999825074
deterministic: 0.0024429989998679957



- Hash table with chainging
- search a: 1
delete a: True
search a: None

- The hash table supports insert, search, and delete operations using chaining.

Hash table performance depends on the load factor and degrades as buckets grow longer.

The scripts can be run directly using ptyhon or Spyder notebook. 
