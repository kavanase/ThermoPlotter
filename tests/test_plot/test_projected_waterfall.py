"""Tests the tp.plot.frequency.add_projected_waterfall function

Failures in tp.plot.axes can have knock-on effects here.
"""

import unittest
from tp.plot import frequency
from tp.plot.axes import one
import matplotlib as mpl
import matplotlib.pyplot as plt

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = {'frequency':   [range(1000)],
                 'mode_kappa':  [[[[[range(1000,2000)]]]]],
                 'temperature': [11],
                 'meta':        {}}
        cls.fig, cls.ax = one()
        cls.ax, cls.cbar = frequency.add_projected_waterfall(cls.ax, cls.d,
                                                             'mode_kappa',
                                                             'frequency',
                                                             direction='x',
                                                             main=True)

    @classmethod
    def tearDownClass(cls):
        plt.close()

    def test_xlim(self):
        self.assertEqual(self.ax.get_xlim(), (0, 999))

    def test_ylim(self):
        self.assertEqual(self.ax.get_ylim(), (1010, 1999))

class InvertTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = {'frequency':   [range(1000)],
                 'mode_kappa':  [[[[[range(1000,2000)]]]]],
                 'temperature': [11],
                 'meta':        {}}
        cls.fig, cls.ax = one()
        cls.ax, cls.cbar = frequency.add_projected_waterfall(cls.ax, cls.d,
                                                             'mode_kappa',
                                                             'frequency',
                                                             direction='x',
                                                             main=True,
                                                             invert=True)

    @classmethod
    def tearDownClass(cls):
        plt.close()

    def test_xlim(self):
        self.assertEqual(self.ax.get_xlim(), (1010, 1999))

    def test_ylim(self):
        self.assertEqual(self.ax.get_ylim(), (0, 999))

class ColourTest(unittest.TestCase):
    def setUp(self):
        self.d = {'frequency':   [[range(1000)]],
                  'mode_kappa':  [[[[[range(1000,2000)]]]]],
                  'temperature': [11],
                  'meta':        {}}

    def tearDown(self):
        plt.close()

    def test_colourmap(self):
        cmap = mpl.cm.get_cmap('viridis')
        fig, ax = one()
        ax = frequency.add_projected_waterfall(ax, self.d, 'mode_kappa',
                                               'frequency', direction='x',
                                               main=True, colour=cmap)

if __name__ == '__main__':
    unittest.main()
