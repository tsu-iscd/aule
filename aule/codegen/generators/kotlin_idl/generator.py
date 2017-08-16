from copy import deepcopy
from typing import List

from aule.codegen import ust
from .. import kotlin
from ..kotlin.helpers import annotations
from .injected_methods import inject_visitor, inject_listener
from .generated_classes import (create_visitor, create_listener,
                                create_serializer, SERIALIZER_CLASS)
from .helpers import json_type_annotation, json_field_annotation


class Generator(kotlin.Generator):
    def __init__(self,
                 add_listener: bool = False,
                 listener_type: str = "",
                 add_visitor: bool = False,
                 visitor_type: str = "",
                 add_decoder: bool = True,
                 root_context_type: str = "",
                 **options) -> None:
        super(Generator, self).__init__(**options)
        self.add_listener = add_listener
        self.listener_type = listener_type
        self.add_visitor = add_visitor
        self.visitor_type = visitor_type
        self.add_decoder = add_decoder
        self.root_context_type = root_context_type
        # Add reflect imports if necessary.
        if (self.add_listener and self.listener_type == "") \
                or (self.add_visitor and self.visitor_type == ""):
            self.imports.extend([
                "import kotlin.reflect.KVisibility",
                "import kotlin.reflect.full.isSubtypeOf",
                "import kotlin.reflect.full.memberFunctions",
                "import kotlin.reflect.full.starProjectedType",
            ])
        # Add JackSON imports if necessary.
        if self.add_decoder:
            self.imports.extend([
                "import com.fasterxml.jackson.annotation.JsonProperty",
                "import com.fasterxml.jackson.annotation.JsonSubTypes",
                "import com.fasterxml.jackson.annotation.JsonTypeInfo",
                "import com.fasterxml.jackson.annotation.JsonTypeName",
            ])

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree, mutableAST)
        # We are going to modify classes, so get a copy of them
        self.src_classes = deepcopy(self.classes)
        for cls in self.classes:
            # Inject listener and visitor methods if necessary
            if self.add_listener:
                inject_listener(cls, self.listener_type)
            if self.add_visitor:
                inject_visitor(cls, self.visitor_type)
        # We add some methods so add overrides if necessary.
        self.mark_overrides()
        # Sadly we should do it again cos we do not want to change inheritance before
        # marking overrides.
        for cls in self.classes:
            if self.add_decoder:
                if not self.class_references.is_inherited_from(cls, SERIALIZER_CLASS):
                    cls.parents.append(SERIALIZER_CLASS)
                annotations.annotate(cls, [json_type_annotation(cls)])
                for f in cls.fields:
                    annotations.annotate(f, [json_field_annotation(f)])
        return self

    def generate(self):
        code = super(Generator, self).generate()
        if not self.add_decoder:
            return code
        first_class_idx = code.find("@JsonTypeName")
        return code[:first_class_idx] \
               + create_serializer(self.classes) + "\n\n" \
               + code[first_class_idx:]

    def generate_listener(self):
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_listener(self.src_classes, self.root_context_type)
            ],
        )

    def generate_visitor(self):
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_visitor(self.src_classes, self.root_context_type)
            ],
        )
