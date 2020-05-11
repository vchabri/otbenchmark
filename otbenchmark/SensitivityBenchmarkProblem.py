#!/usr/bin/python
# coding:utf-8
# Copyright 2020 EDF
"""Class to define a sensitivity benchmark problem."""


class SensitivityBenchmarkProblem:
    def __init__(
        self, name, distribution, function, firstOrderIndices, totalOrderIndices,
    ):
        """
        Creates a reliability problem.

        Parameters
        ----------
        thresholdEvent : ot.ThresholdEvent
            The event.

        distribution : ot.Distribution
            The input distribution.

        function : ot.Function
            The model.

        firstOrderIndices : ot.Point
            The first order indices.

        totalOrderIndices : ot.Point
            The total order indices.

        Example
        -------
        problem  = ReliabilityBenchmarkProblem(thresholdEvent)
        """
        self.name = name
        self.distribution = distribution
        self.function = function
        self.firstOrderIndices = firstOrderIndices
        self.totalOrderIndices = totalOrderIndices
        return None

    def getInputDistribution(self):
        """
        Returns the input distribution.

        Parameters
        ----------
        None.

        Returns
        -------
        distribution: ot.Distribution
            The distribution.
        """
        return self.distribution

    def getFunction(self):
        """
        Returns the function.

        Parameters
        ----------
        None.

        Returns
        -------
        function: ot.Function
            The function.
        """
        return self.function

    def getName(self):
        """
        Returns the name of the problem.

        Parameters
        ----------
        None.

        Returns
        -------
        name: str
            The name.
        """
        return self.name

    def getFirstOrderIndices(self):
        """
        Returns the first order Sobol' sensitivity indices.

        Parameters
        ----------
        None.

        Returns
        -------
        firstOrderIndices: ot.Point
            The first order sensitivity indices.
        """
        return self.firstOrderIndices

    def getTotalOrderIndices(self):
        """
        Returns the total order Sobol' sensitivity indices.

        Parameters
        ----------
        None.

        Returns
        -------
        totalOrderIndices: ot.Point
            The total order sensitivity indices.
        """
        return self.totalOrderIndices
