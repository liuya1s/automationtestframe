# -*- encoding: utf-8 -*-
import yaml

def read_yaml_file(yaml_file):
    with open(yaml_file, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    
    return data