"""
Created August 14 2014
James Houghton <james.p.houghton@gmail.com>

Changed May 03 2017
Alexey Prey Mulyukin <alexprey@yandex.ru> from sdCloud.io developement team
    Changes:

    [May 03 2017] Alexey Prey Mulyukin: Integrate support to
        logical operators like 'AND', 'OR' and 'NOT'.
        Fix support the whitespaces in expressions between
        operators and operands.
        Add support to modulo operator - 'MOD'.
        Fix support for case insensitive in function names.

This module converts a string of SMILE syntax into Python

"""
import parsimonious
from parsimonious.nodes import NodeVisitor
import pkg_resources
import re
from .. import builder, utils

# Here we define which python function each XMILE keyword corresponds to
functions = {
    # ===
    # 3.5.1 Mathematical Functions
    # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039980
    # ===

    "abs": "abs",
    "int": "int",
    "inf": {"name": "np.inf", "module": "numpy"},
    "exp": {"name": "np.exp", "module": "numpy"},
    "sin": {"name": "np.sin", "module": "numpy"},
    "cos": {"name": "np.cos", "module": "numpy"},
    "tan": {"name": "np.tan", "module": "numpy"},
    "arcsin": {"name": "np.arcsin", "module": "numpy"},
    "arccos": {"name": "np.arccos", "module": "numpy"},
    "arctan": {"name": "np.arctan", "module": "numpy"},
    "sqrt": {"name": "np.sqrt", "module": "numpy"},
    "ln": {"name": "np.log", "module": "numpy"},
    "log10": {"name": "np.log10", "module": "numpy"},
    "max": "max",
    "min": "min",

    # ===
    # 3.5.2 Statistical Functions
    # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039981
    # ===

    "exprnd": {"name": "np.random.exponential", "module": "numpy"},
    "lognormal": {"name": "np.random.lognormal", "module": "numpy"},
    "normal": {"name": "np.random.normal", "module": "numpy"},
    "poisson": {"name": "np.random.poisson", "module": "numpy"},
    "random": {"name": "np.random.rand", "module": "numpy"},

    # ===
    # 3.5.4 Test Input Functions
    # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039983
    # ===

    "pulse": {
        "name": "pulse_magnitude",
        "parameters": [
            {"name": 'time', "type": "time"},
            {"name": 'magnitude'},
            {"name": 'start'},
            {"name": "repeat_time", "optional": True}
        ],
        "module": "functions"
    },
    "step": {
        "name": "step",
        "parameters": [
            {"name": 'time', "type": 'time'},
            {"name": 'value'},
            {"name": 'tstep'}
        ],
        "module": "functions"
    },
    # time, slope, start, finish=0
    "ramp": {
        "name": "ramp",
        "parameters": [
            {"name": 'time', "type": 'time'},
            {"name": 'slope'},
            {"name": 'start'},
            {"name": 'finish', "optional": True}
        ],
        "module": "functions"
    },

    # ===
    # 3.5.6 Miscellaneous Functions
    # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039985
    # ===
    "if then else": {
        "name": "if_then_else",
        "parameters": [
            {"name": 'condition'},
            {"name": 'val_if_true', "type": 'lambda'},
            {"name": 'val_if_false', "type": 'lambda'}
        ],
        "module": "functions"
    },

    # TODO functions/stateful objects to be added
    # https://github.com/JamesPHoughton/pysd/issues/154
    "forecast": {"name": "not_implemented_function", "module": "functions",
                 "original_name": "forecast"},
    "previous": {"name": "not_implemented_function", "module": "functions",
                 "original_name": "previous"},
    "self": {"name": "not_implemented_function", "module": "functions",
             "original_name": "self"}
}

prefix_operators = {
    "not": " not ",
    "-": "-",
    "+": " ",
}

infix_operators = {
    "and": " and ",
    "or": " or ",
    "=": "==",
    "<=": "<=",
    "<": "<",
    ">=": ">=",
    ">": ">",
    "<>": "!=",
    "^": "**",
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
    "mod": "%",
}

# ====
# 3.5.3 Delay Functions
# http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039982
# ====

builders = {
    # "delay" !TODO! How to add the infinity delay?

    "delay1": lambda element, subscript_dict, args:
        builder.add_n_delay(
            identifier=element["py_name"],
            delay_input=args[0],
            delay_time=args[1],
            initial_value=args[2] if len(args) > 2 else args[0],
            order="1",
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "delay3": lambda element, subscript_dict, args:
        builder.add_n_delay(
            identifier=element["py_name"],
            delay_input=args[0],
            delay_time=args[1],
            initial_value=args[2] if len(args) > 2 else args[0],
            order="3",
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "delayn": lambda element, subscript_dict, args:
        builder.add_n_delay(
            identifier=element["py_name"],
            delay_input=args[0],
            delay_time=args[1],
            initial_value=args[2] if len(args) > 3 else args[0],
            order=args[2],
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "smth1": lambda element, subscript_dict, args:
        builder.add_n_smooth(
            identifier=element["py_name"],
            smooth_input=args[0],
            smooth_time=args[1],
            initial_value=args[2] if len(args) > 2 else args[0],
            order="1",
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "smth3": lambda element, subscript_dict, args:
        builder.add_n_smooth(
            identifier=element["py_name"],
            smooth_input=args[0],
            smooth_time=args[1],
            initial_value=args[2] if len(args) > 2 else args[0],
            order="3",
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "smthn": lambda element, subscript_dict, args:
        builder.add_n_smooth(
            identifier=element["py_name"],
            smooth_input=args[0],
            smooth_time=args[1],
            initial_value=args[2] if len(args) > 3 else args[0],
            order=args[2],
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    # "forcst" !TODO!

    "trend": lambda element, subscript_dict, args:
        builder.add_n_trend(
            identifier=element["py_name"],
            trend_input=args[0],
            average_time=args[1],
            initial_trend=args[2] if len(args) > 2 else 0,
            subs=element["subs"],
            merge_subs=None,
            deps=element["dependencies"]
        ),

    "init": lambda element, subscript_dict, args:
        builder.add_initial(
            identifier=element["py_name"],
            value=args[0],
            deps=element["dependencies"]),
}


def format_word_list(word_list):
    return '|'.join(
        [re.escape(k) for k in reversed(sorted(word_list, key=len))])


class SMILEParser(NodeVisitor):
    def __init__(self, model_namespace={}, subscript_dict={}):

        self.model_namespace = model_namespace
        self.subscript_dict = subscript_dict
        self.extended_model_namespace = {
            key.replace(' ', '_'): value
            for key, value in self.model_namespace.items()}
        self.extended_model_namespace.update(self.model_namespace)

        # ===
        # 3.5.5 Time Functions
        # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039984
        # ===
        self.extended_model_namespace.update({'dt': 'time_step'})
        self.extended_model_namespace.update({'starttime': 'initial_time'})
        self.extended_model_namespace.update({'endtime': 'final_time'})

        grammar = pkg_resources.resource_string(
            "pysd", "translation/xmile/smile.grammar")
        grammar = grammar.decode('ascii').format(
            funcs=format_word_list(functions.keys()),
            in_ops=format_word_list(infix_operators.keys()),
            pre_ops=format_word_list(prefix_operators.keys()),
            identifiers=format_word_list(self.extended_model_namespace.keys()),
            build_keywords=format_word_list(builders.keys())
        )

        self.grammar = parsimonious.Grammar(grammar)

    def parse(self, text, element, context='eqn'):
        """
           context : <string> 'eqn', 'defn'
                If context is set to equation, lone identifiers will be
                parsed as calls to elements. If context is set to definition,
                lone identifiers will be cleaned and returned.
        """

        # Remove the inline comments from `text` before parsing the grammar
        # http://docs.oasis-open.org/xmile/xmile/v1.0/csprd01/xmile-v1.0-csprd01.html#_Toc398039973
        text = re.sub(r"\{[^}]*\}", "", text)
        if "dependencies" not in element:
            element["dependencies"] = dict()

        self.ast = self.grammar.parse(text)
        self.context = context
        self.element = element
        self.new_structure = []

        py_expr = self.visit(self.ast)

        return ({
            'py_expr': py_expr
        }, self.new_structure)

    def visit_conditional_statement(self, n, vc):
        return builder.build_function_call(functions["if then else"], vc[2::4])

    def visit_user_call_identifier(self, n, vc):
        return self.extended_model_namespace[n.text]

    def visit_user_call_quoted_identifier(self, n, vc):
        return self.extended_model_namespace[vc[1]]

    def visit_identifier(self, n, vc):
        subelement = self.extended_model_namespace[n.text]
        utils.update_dependency(subelement, self.element["dependencies"])
        return subelement + '()'

    def visit_quoted_identifier(self, n, vc):
        subelement = self.extended_model_namespace[vc[1]]
        utils.update_dependency(subelement, self.element["dependencies"])
        return subelement + '()'

    def visit_call(self, n, vc):
        function_name = vc[0].lower()
        arguments = [e.strip() for e in vc[4].split(",")]
        return builder.build_function_call(
            functions[function_name], arguments, self.element["dependencies"])

    def visit_user_call(self, n, vc):
        return vc[0] + '(' + vc[4] + ')'

    def visit_build_call(self, n, vc):
        builder_name = vc[0].lower()
        arguments = [e.strip() for e in vc[4].split(",")]
        name, structure = builders[builder_name](
            self.element, self.subscript_dict, arguments)
        self.new_structure += structure
        self.element["dependencies"] = {structure[-1]["py_name"]: 1}
        return name

    def visit_pre_oper(self, n, vc):
        return prefix_operators[n.text.lower()]

    def visit_in_oper(self, n, vc):
        return infix_operators[n.text.lower()]

    def generic_visit(self, n, vc):
        """
        Replace childbearing nodes with a list of their children;
        for leaves, return the node text;
        for empty nodes, return an empty string.

        Handles:
        - call
        - parens
        -
        """
        return ''.join(filter(None, vc)) or n.text or ''
