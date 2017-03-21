import ast


def str_node(node):
    if isinstance(node, ast.AST):
        fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in ('left', 'right')]
        # rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
        rv = '%s' % node.__class__.__name__
        return rv
    else:
        return repr(node)


def ast_visit_tostring(node, level=0):
    pass


def ast_visit(node, str='', level=0):
    print('  ' * level + str_node(node))
    print(str)
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            count = 0
            for item in value:
                count += 1
                print('lvl%2d:%2d' % (level, count), end='')
                if isinstance(item, ast.AST):
                    ast_visit(item, str + item.__class__.__name__ + '{', level=level + 1)
        elif isinstance(value, ast.AST):
            print('ter')


def ast_visit2(node, level=0):
    ans=''
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ans += ' '*level+item.__class__.__name__ + '{\n'
                    ans += ast_visit2(item, level + 1)+'\n}'
        elif isinstance(value, ast.AST):
            ans+= ' '*level+field+' '
        else:
            print('')
    return ans


filepath = r'test.py'
with open(filepath) as f:
    code = f.read()
    print(ast_visit2(ast.parse(code)))
