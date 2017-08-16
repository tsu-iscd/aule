from ..base import BaseGenerator
from . import helpers


class Generator(BaseGenerator):
    TEMPLATE_FILE = "golang.jinja2"

    def __init__(self, **options):
        super(Generator, self).__init__()
        self.inject_filters(
            apply_modifiers=helpers.apply_modifiers,
            self_reference=helpers.self_reference,
            typed=helpers.typed,
            translate_type=helpers.translate_type,
        )
