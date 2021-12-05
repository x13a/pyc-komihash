py-komihash
===========

Cython wrapper on `komihash <https://github.com/avaneev/komihash>`_ .

Library
-------

.. code:: python

  import komihash
  
  hash64 = komihash.komihash(b'test1')
  assert hash64 == 5270236647356506095
