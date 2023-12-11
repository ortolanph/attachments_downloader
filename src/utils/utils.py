from os import path, mkdir


def transform_headers(header_list):
    return {header["name"]: header["value"] for header in [pair for pair in header_list]}


def create_target_folder(target_folder):
    print(f"Creating folder {target_folder}")
    if not path.exists(target_folder):
        mkdir(target_folder)
