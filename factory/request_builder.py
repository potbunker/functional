import json
from collections import OrderedDict

def merge(first, second):
    (section, subsection) = parse_markup(second)

    def merge_subsection(first, second):
        value = first.get(subsection)
        if value:
            value.append(second)
        else:
            first[subsection] = [second]
        return first

    if not subsection:
        section_value = first.get(section)
        if section_value:
            section_value.append(second)
        else:
            first[section] = [second]
    else:
        value = first.get(section, OrderedDict())
        first[section] = merge_subsection(value, second)

    return first


def parse_markup(row):
    markup_string = row.get('markup')
    markup = json.loads(markup_string)
    return markup.get('section'), markup.get('subsection')


rows = [
    {'markup': '{\"section\": \"section1\"}', 'suid': 'ABCD1'},
    {'markup': '{\"section\": \"section1\"}', 'suid': 'ABCD2'},
    {'markup': '{\"section\": \"section2\", \"subsection\": \"ss1\"}', 'suid': 'ABCD3'},
    {'markup': '{\"section\": \"section2\", \"subsection\": \"ss1\"}', 'suid': 'ABCD4'},
    {'markup': '{\"section\": \"section2\", \"subsection\": \"ss2\"}', 'suid': 'ABCD5'},
    {'markup': '{\"section\": \"section2\", \"subsection\": \"ss2\"}', 'suid': 'ABCD6'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss1\"}', 'suid': 'ABCD7'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss1\"}', 'suid': 'ABCD8'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss2\"}', 'suid': 'ABCD9'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss2\"}', 'suid': 'ABCD10'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss2\"}', 'suid': 'ABCD11'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss3\"}', 'suid': 'ABCD12'},
    {'markup': '{\"section\": \"section3\", \"subsection\": \"ss3\"}', 'suid': 'ABCD13'}
]

tree = reduce(merge, rows, OrderedDict())

print json.dumps(tree, indent=2)