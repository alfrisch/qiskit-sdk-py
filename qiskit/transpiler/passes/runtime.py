# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" An analysis pass for estimating the circuit runtime.
"""
from qiskit.transpiler.basepasses import AnalysisPass
from qiskit.transpiler.passes.longest_path import LongestPath


class Runtime(AnalysisPass):
    """ An analysis pass for estimating the circuit runtime based on op runtimes.
    """

    def __init__(self, op_times=None):
        super().__init__()
        self.requires.append(LongestPath(op_times))

    def run(self, dag):
        """ Calculate the overall runtime for the DAG longest path by putting the
        operation times as weights on edges.
        """

        runtime = self.property_set['longest_path_length']
        self.property_set['runtime'] = runtime
