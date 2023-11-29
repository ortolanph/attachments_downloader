def transform_headers(header_list):
    return {header["name"]: header["value"] for header in [pair for pair in header_list]}
