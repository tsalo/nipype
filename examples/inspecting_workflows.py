#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
========================
Inspecting run workflows
========================

It can be useful to investigate individual nodes' inputs and outputs in a workflow that has been run.
For example, this can help developers write unit tests for their workflows.

"""
"""A test workflow."""
import os

from nipype.interfaces import utility as niu
from nipype.pipeline import engine as pe
from nipype.interfaces.base import (
    BaseInterfaceInputSpec,
    File,
    SimpleInterface,
    TraitedSpec,
    traits,
)


class _WriteStringInputSpec(BaseInterfaceInputSpec):
    in_str = traits.Str(mandatory=True)


class _WriteStringOutputSpec(TraitedSpec):
    out_file = File(exists=True)


class WriteString(SimpleInterface):
    """Write a string to a file."""

    input_spec = _WriteStringInputSpec
    output_spec = _WriteStringOutputSpec

    def _run_interface(self, runtime):
        self._results["out_file"] = os.path.join(runtime.cwd, "out_file.txt")
        with open(self._results["out_file"], "w") as fo:
            fo.write(self.inputs.in_str)

        return runtime

wf = pe.Workflow(name="example_workflow")

inputnode = pe.Node(
    niu.IdentityInterface(fields=["in_str"]),
    name="inputnode",
)
outputnode = pe.Node(
    niu.IdentityInterface(fields=["out_file"]),
    name="outputnode",
)

write_string = pe.Node(
    WriteString(),
    name="write_string",
)

wf.connect([
    (inputnode, write_string, [("in_str", "in_str")]),
    (write_string, outputnode, [("out_file", "out_file")]),
])
