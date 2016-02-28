__author__ = 'haywire'
import re
from questions import Questions

stringRegexp = re.compile(r'\w+')
anythingRegexp = re.compile(r'.+')

def validateString(s):
    return stringRegexp.match(s)

def validateAddress(s):
    if len(s) > 10:
        return anythingRegexp.match(s)
    return None

class User():
    # name = 'Honey'
    # email = ''
    # address = ''

    basicQuestions = Questions(
        [   'What shall I call you honey? (Your sweet name please :)',
            'What\'s your internet address? (Email Id!)',
            'And where do you live on the earth? (Your address! Please type in one line only)'
        ],
        [   validateString,
            validateString,
            validateString
        ],
        [   'Honey',
            '',
            ''
        ]
    )







