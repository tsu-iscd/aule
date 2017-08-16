from copy import deepcopy

from .. import cpp
from .methods import *
from .classes import *


class Generator(cpp.Generator):
    INCLUDE_LISTENER_AND_VISITOR = """\
#include "ASTListener.cpp"
#include "ASTVisitor.cpp"
"""
    AUX2JSON = """
/** Auxiliary methods `toJSON` **/
const string _escape(const string& str){
    string result = str;
    size_t pos = 0;
    while((pos=result.find('"', pos)) != string::npos){
        result.insert(pos, 1, '\\\\');
        pos += 2;
    }
    return result;
}

string simple_toJSON(const int i){
    return to_string(i);
}

string simple_toJSON(const double d){
    return to_string(d);
}

string simple_toJSON(const string& str_){
    return '"'+_escape(str_)+'"';
}

string simple_toJSON(const bool b){
    return b ? "true" : "false";
}
\n"""


    def __init__(self, add_listener=False, add_visitor=False, **options):
        super(Generator, self).__init__(**options)
        self.add_listener = add_listener
        self.add_visitor = add_visitor

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree, mutableAST)
        # We are going to modify classes, so get a copy of them
        self.src_classes = deepcopy(self.classes)
        for cls in self.classes:
            # Inject listener and visitor methods if necessary
            if self.add_listener:
                inject_listener(cls)
            if self.add_visitor:
                inject_visitor(cls)
        inject_toJSON(self.classes)
        return self

    def generate(self):
        code = super(Generator, self).generate()
        met_def_idx = code.find("/* Methods definitions */")
        return code[:met_def_idx]+self.AUX2JSON+code[met_def_idx:]

    def generate_listener(self):
        code = "#pragma once\n" + self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_listener(self.src_classes)
            ],
        )
        return code

    def generate_visitor(self):
        code = '#pragma once\n\n' + '#include "Any.h"\n' + self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_visitor(self.src_classes)
            ],
        )
        return code
