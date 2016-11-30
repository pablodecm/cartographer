TDA concepts
------------

Under a very broad view, topological data analysis (TDA) can
be define as a collection of data analysis techniques
that try to find structure in data [#tda_wasserman]_. Most of these
methods are based on quantifying the ideas of shape and connectivity
on the observed data.
It is worth to point out that while even clustering or manifold learning
can be considered as a members of the TDA family of tools, some authors
restrict this category to only the approaches that make extensive use of
persistent homology (e.g. Betti numbers, barcodes and persistent
diagrams).

The main idea behind persistent homology is that the topological
features that appears within a wide range of resolutions are those more
likely to represent genuine features of the underlying space. This
is a very powerful notion which is extensible to many other statistical
tool or when clustering or applying the Mapper algorithm itself to data
as a function of parameters, as it will be shown in the next section
and the provided practical examples.

References
==========

.. [#tda_wasserman] Larry Wasserman.
 "Topological Data Analysis". Submitted to Annual Reviews in Statistics. 2016.
 `eprint arXiv:1609.08227
 <https://arxiv.org/abs/1609.08227>`_
