import pytest

from pathlib import Path
import os

from rna_strand.rna_nupack_api import RNAStrand

from rna_squirrel.make_single_api_file import GenerateSingleApifile


def test_make_api_file():
    new_generator:GenerateSingleApifile = GenerateSingleApifile()
    new_generator.run(nut_struct_name="NupackRNAStruct",
                      yaml_config_path=Path('/home/rnauser/dev_data/new_yaml_version_v3.yaml'),
                      dst_save_filename=Path('/home/rnauser/dev_data/rna_nupack_api.py'))
    assert os.path.isfile(Path('/home/rnauser/dev_data/rna_nupack_api.py'))==True

def test_call_dynamic_api():
    rna_strand_num_1:RNAStrand = RNAStrand(var_name='rna_strand_num_1',
                    working_folder='/home/rnauser/dev_data/')
    rna_strand_num_1.primary_structure.strand = "AUGGCACA"
    assert rna_strand_num_1.primary_structure.strand == "AUGGCACA_returned"