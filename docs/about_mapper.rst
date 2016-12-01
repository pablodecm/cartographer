Theoretical miminum
-------------------

The Mapper algorithm  [#mapper_first]_ is a visualization and data exploration
technique to study the shape of high-dimensional data. This analysis method is
generally classified as a topological data analysis (TDA) technique. Topology is
the branch of mathematics which formally studies the qualitative geometric
information of space by considering the characteristics that are preserved
under continuous deformations.
The mathematical properties of this discipline, such as
functoriality, make of TDA a robust framework for studying high-dimensional data
even in the presence of weak metrics or significant statistical noise.

In addition to the original paper [#mapper_first]_ where the technique
was presented, I recommend checking *Topology and data*
[#topology_and_data]_ by Gunnar Carlsson and also some of the white papers
and videos provided at Ayasdi_, which is the company created by the inventors of
the Mapper algorithm for its enterprise exploitation.
In the following subsections, the basic theoretical concepts underlying TDA will be
reviewed together with a formal description of what Mapper is and why
it can be a useful tool for exploring the shape of data:

Topological data analysis
=========================

Under a very broad view, topological data analysis (TDA) can
be defined as a collection of data analysis techniques
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
tools. For example, it is a really useful concept for clustering,
kernel density estimation or applying the Mapper algorithm itself to data
as a function of parameters, as it will be shown in the next section
and provided practical examples.

Mapper algorithm 
================

The purpose of the Mapper algorithm is to obtain compact representations
which can be used to visualize and explore the shape and connectivity
properties that might be present in complex high-dimensional data.


  
References
==========

.. [#mapper_first] Singh, Gurjeet, Facundo Mémoli, and Gunnar E. Carlsson.
 "Topological Methods for the Analysis of High Dimensional Data Sets and
 3D Object Recognition." SPBG. 2007.
 `doi:10.2312/SPBG/SPBG07/091-100 
 <http://dx.doi.org/10.2312/SPBG/SPBG07/091-100>`_

.. [#tda_wasserman] Larry Wasserman.
 "Topological Data Analysis". Submitted to Annual Reviews in Statistics. 2016.
 `eprint arXiv:1609.08227
 <https://arxiv.org/abs/1609.08227>`_

.. [#topology_and_data] Gunnar E. Carlsson.
 "Topology and Data" Bull. Amer. Math. Soc. 46 (2009), 255-308.
 `doi:10.1090/S0273-0979-09-01249-X
 <http://dx.doi.org/10.1090/S0273-0979-09-01249-X>`_

.. _Ayasdi: https://www.ayasdi.com/

