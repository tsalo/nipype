# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import ROIStats


def test_ROIStats_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        debug=dict(argstr='-debug', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        format1D=dict(
            argstr='-1Dformat',
            xor=['format1DR'],
        ),
        format1DR=dict(
            argstr='-1DRformat',
            xor=['format1D'],
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        mask=dict(
            argstr='-mask %s',
            deprecated='1.1.5',
            new_name='mask_file',
            position=3,
        ),
        mask_f2short=dict(argstr='-mask_f2short', ),
        mask_file=dict(argstr='-mask %s', ),
        nobriklab=dict(argstr='-nobriklab', ),
        nomeanout=dict(argstr='-nomeanout', ),
        num_roi=dict(argstr='-numroi %s', ),
        out_file=dict(
            argstr='> %s',
            keep_extension=False,
            name_source='in_file',
            name_template='%s_roistat.1D',
            position=-1,
        ),
        quiet=dict(argstr='-quiet', ),
        roisel=dict(argstr='-roisel %s', ),
        stat=dict(argstr='%s...', ),
        zerofill=dict(
            argstr='-zerofill %s',
            requires=['num_roi'],
        ),
    )
    inputs = ROIStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ROIStats_outputs():
    output_map = dict(out_file=dict(), )
    outputs = ROIStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
