===============================
Runing DGP on the MNIST dataset
===============================

For this tutorial you will need the desired dataset saved into a CSV file in
order to start working with it.

Getting the CSV and adapting it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use a whole dataset (for example MNIST_ plant dataset) with dgp, we
first need to download into, for example, the ``datasets`` directory and adapt
it. First things first, add a header row on top of the file and ensure the class
column has the "class" name. After that, d2p1_ will take care of the dataset
and will split it into the Proben1 partition schema. `dataset-to-proben1` is a
script that comes with DeepGProp_ in order to ease this compatibility task.

In our case, as we selected the MNIST_ dataset, we will start from:

.. code::

   datasets/
   └── mnist_train.csv

now we will run the following command to obtain the converted partitions:

.. code:: shell

   d2p1 datasets/mnist_train.csv

we will end up (after a while) with:

.. code::

   datasets/
   ├── mnist_train1.trn
   ├── mnist_train1.tst
   ├── mnist_train1.val
   ├── mnist_train2.trn
   ├── mnist_train2.tst
   ├── mnist_train2.val
   ├── mnist_train3.trn
   ├── mnist_train3.tst
   ├── mnist_train3.val
   └── mnist_train.csv


Remember to change `# label` to class, by hand if needed, since that's the format expected by `dgp`.


Loading it into DeepGProp
^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have our newly created Proben1 partitions, we just need to tell dgp
(DeepGProp_) to search for the desired partition, for example, in order to run
the first partition we will write:

.. code:: shell
   
   dgp --dataset-name mnist_train1 --dataset-dir-path ./datasets/

.. _MNIST: https://www.kaggle.com/oddrationale/mnist-in-csv
.. _DeepGProp: https://github.com/lulivi/dgp-lib
.. _d2p1: docs/dataset_to_proben1.rst
