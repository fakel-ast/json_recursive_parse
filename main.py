import sys
import json
from json import JSONDecodeError


def get_dict_items(json_data):
    if isinstance(json_data, dict):
        # if dictionary, iterate on list dictionary's keys
        yield from get_dict_items(list(json_data.keys()))
        # after keys, iterate on values
        for item in json_data.values():
            if isinstance(item, (dict, list)):
                yield from get_dict_items(item)
            else:
                yield item
    else:
        # iterate on list's item and if item is dict or list run recursion
        for item in json_data:
            if isinstance(item, (dict, list)):
                yield from get_dict_items(item)
            else:
                yield item


if __name__ == '__main__':
    if not sys.argv[1:]:
        sys.exit('Not got required argument (json)')
    # if json use space (argv > 1), concat without is
    json_arg = ''.join(sys.argv[1:])
    try:
        json_arg = json.loads(json_arg)
        items = list(set(get_dict_items(json_arg)))
        print(items)
    except JSONDecodeError:
        sys.exit('Not valid json')
