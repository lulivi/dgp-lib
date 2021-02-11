This simple script splits the dataset into 3 partitions, consisting of three
sets each one:

* Training
* Validation
* Test

It has the file path as an argument, and will create the partitions in the same
directory as the file is:

.. code:: shell
   
   d2p1 path/to/file.csv

You also can use the ``seed`` option, to define a fixed seed. By default the
seed is defined in ``dgp/settings.py``. Another way of setting the seed is by
an environment variable:

.. code:: shell

   d2p1 path/to/file.csv --seed 23552
