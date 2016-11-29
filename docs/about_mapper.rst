Theoretical miminum
-------------------

The Mapper algorithm  [#mapper_first]_ is a visualization and data exploration
technique to study the shape of high-dimensional data. This analysis method is
generally classified as a topological data analysis (TDA) technique. Topology is
the branch of mathematics centered around the qualitative geometric information
by studying the characteristics of space that are preserved under continuous
deformations. The mathematical properties of this discipline, such as
functoriality, make of TDA a robust framework for studying high-dimensional data
even in the presence of an weak metric or statistical noise.

In addition to the original paper where the technique
was presented, I recommend checking *Topology and data*
[#topology_and_data]_ by Gunnar Carlsson and also some of the white papers
and videos provided at Ayasdi_, which is the company created by the inventors of
the Mapper algorithm for its enterprise exploitation.
In the following subsections, the basic theoretical concepts underlying TDA will be
reviewed together with a formal description of what Mapper is and why
it can be a useful tool for exploring the shape of data:


.. toctree::
  theory/concepts
  theory/mapper
  
References
==========

.. [#mapper_first] Singh, Gurjeet, Facundo Mémoli, and Gunnar E. Carlsson.
 "Topological Methods for the Analysis of High Dimensional Data Sets and
 3D Object Recognition." SPBG. 2007.
 `doi:10.2312/SPBG/SPBG07/091-100 
 <http://dx.doi.org/10.2312/SPBG/SPBG07/091-100>`_

.. [#topology_and_data] Gunnar E. Carlsson.
 "Topology and Data" Bull. Amer. Math. Soc. 46 (2009), 255-308.
 `doi:10.1090/S0273-0979-09-01249-X
 <http://dx.doi.org/10.1090/S0273-0979-09-01249-X>`_

.. _Ayasdi: https://www.ayasdi.com/

