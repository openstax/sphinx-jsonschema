import json

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from sphinx.directives.code import container_wrapper
from sphinx.util.nodes import set_source_info
from sphinxcontrib.autohttp.common import import_object


class JSONSchemaDirective(Directive):
    """Generates JSON schema code block from a python object"""

    has_content = True

    def run(self):
        pyobj = import_object(self.content[0].strip())
        json_string = json.dumps(pyobj,
                                 indent=2,
                                 sort_keys=True,
                                 separators=(',', ':'))
        literal = nodes.literal_block(json_string, json_string)
        literal['language'] = 'json'
        set_source_info(self, literal)
        caption = self.options.get('caption')
        if caption:
            literal = container_wrapper(self, literal, caption)
        return [literal]


def setup(app):
    pass

directives.register_directive('jsonschema', JSONSchemaDirective)
