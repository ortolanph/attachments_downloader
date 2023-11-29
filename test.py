if __name__ == '__main__':
    map_list = [
        {
            "key": "From",
            "value": "paulo.ortolan@gmail.com"
        },
        {
            "key": "To",
            "value": "paulo.ortolan.pt@gmail.com"
        },
    ]

    o_values = {o["key"]: o["value"] for o in [p for p in map_list]}

    print(o_values)
