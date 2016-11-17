
|Travis|_ |Coveralls|_ |Landscape|_ |Gitter|_ 

What is cartographer?
=====================

.. |Travis| image:: https://travis-ci.org/pablodecm/cartographer.svg?branch=master
.. _Travis: https://travis-ci.org/pablodecm/cartographer

.. |Coveralls| image:: https://coveralls.io/repos/github/pablodecm/cartographer/badge.svg?branch=master 
.. _Coveralls: https://coveralls.io/github/pablodecm/cartographer?branch=master 

.. |Landscape| image:: https://landscape.io/github/pablodecm/cartographer/master/landscape.svg?style=flat
.. _Landscape: https://landscape.io/github/pablodecm/cartographer/master

.. |Gitter| image:: https://badges.gitter.im/cartographer_.svg
.. _Gitter: https://gitter.im/cartographer_/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

Cartographer is a Python library which implements the Mapper 
algorithm [#mapper_first]_ for data visualization and exploration.
The design goal of this particular implementation is to be flexible,
extendible and fully scikit-learn_ compatible. 

Features
========

Installation
============

The Mapper algorithm of the library only requires a modern version
of scikit-learn (and its dependencies numpy and scipy). Nevertheless,
to run the examples, also a Jupyter Notebook installation with a Python
Kernel and the seaborn visualization library are required.
Both Python 2 and Python 3 are supported and tested for the time being, while
the suggestion is using the later.



Documentation
=============

The documentation of this software library, together with more information
the Mapper algorithm and some examples of its use can be found
at http://pablodecm.com/cartographer.

References
==========

.. [#mapper_first] Singh, Gurjeet, Facundo Mémoli, and Gunnar E. Carlsson.
 "Topological Methods for the Analysis of High Dimensional Data Sets and
 3D Object Recognition." SPBG. 2007.
 `doi:10.2312/SPBG/SPBG07/091-100 
 <http://dx.doi.org/10.2312/SPBG/SPBG07/091-100>`_

.. _scikit-learn: http://scikit-learn.org/stable/

