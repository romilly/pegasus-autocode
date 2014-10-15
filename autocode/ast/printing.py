from autocode.ast.ast import Element


class Print(Element):
    def __init__(self, value, format_spec):
        self.value = value
        self.format_spec = format_spec

    def evaluate_in(self, context):
        val = self.value.evaluate_in(context)
        fmt = self.format_spec.evaluate_in(context)
        context.write(self.format_value(val, fmt))

    def unpack(self, fmt):
        a = fmt / 1000
        bc = fmt % 1000
        b = bc / 20
        c = bc % 20
        return (a, b, c)

    def format_value(self, val, fmt):
        result = ''
        a,b,c =  self.unpack(fmt)
        width = b+c+1
        result += '\n '[a % 2]
        if a > 2:
            format_string = '%+'+('%d.%d' % (width , c))+'F'
            result +=  format_string % val
        return result
