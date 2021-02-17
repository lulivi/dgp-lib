"""Test the :mod:`dgp.ga_optimizer.utils` module."""
import unittest

from unittest import mock

from dgp.ga_optimizer.utils import evaluate_population


class TestUtils(unittest.TestCase):
    """Test the util functions."""

    def test_evaluate_population(self):
        """Test the population evaluator."""
        mock_fitness = 1
        mock_evaulate_fn = lambda x: mock_fitness
        mock_ind_1 = mock.Mock()
        mock_ind_2 = mock.Mock()
        mock_population = [mock_ind_1, mock_ind_2]

        evaluate_population(mock_population, mock_evaulate_fn)

        self.assertEqual(mock_ind_1.fitness.values, mock_fitness)
        self.assertEqual(mock_ind_2.fitness.values, mock_fitness)

