from ..base import BaseGenerator


class Generator(BaseGenerator):
    TEMPLATE_FILE = "ecmascript.jinja2"

    def __init__(self, **options):
        super(Generator, self).__init__()
