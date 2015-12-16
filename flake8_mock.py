# coding: utf-8

from sys import stdin

import ast
import tokenize


__version__ = '0.2'

NON_EXISTENT_METHODS = [
    'assert_calls',
    'assert_not_called',
    'assert_called',
    'assert_called_once',
    'not_called',
    'called_once',
    'called_once_with',
]
MOCK_ERROR_CODE = 'M001'
ERROR_MESSAGE = "%s %s is a non-existent mock method."


def get_noqa_lines(code):
    tokens = tokenize.generate_tokens(lambda L=iter(code): next(L))
    noqa = [token[2][0] for token in tokens if token[0] == tokenize.COMMENT
            and (token[1].endswith('noqa') or (isinstance(token[0], str) and
                                               token[0].endswith('noqa')))]
    return noqa


class MockChecker(object):
    name = 'flake8-mock'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = (filename == 'stdin' and stdin) or filename
        self.errors = []

    def run(self):
        with open(self.filename, 'r') as file_to_check:
            node_ast = file_to_check.read()
            self.noqa_lines = get_noqa_lines(node_ast)
        module = ast.parse(node_ast)
        walking = ast.walk(module)
        for node in walking:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                if (node.lineno not in self.noqa_lines) and \
                   hasattr(node.value.func, 'attr') and \
                   node.value.func.attr in NON_EXISTENT_METHODS:
                    self.errors.append({
                        "message": ERROR_MESSAGE % (
                            MOCK_ERROR_CODE, node.value.func.attr),
                        "line": node.lineno,
                    })
        for error in self.errors:
            yield (error.get("line"), 0, error.get("message"), type(self))
