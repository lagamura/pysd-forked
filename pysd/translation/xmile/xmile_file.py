from pathlib import Path
from lxml import etree

from ..structures.abstract_model import AbstractModel

from .xmile_section import FileSection


class XmileFile():
    """
    Create a XmileFile object which allows parsing a xmile file.

    Parameters
    ----------
    xmile_path: str or pathlib.Path
        Path to the Xmile model.

    encoding: str or None (optional)
        Encoding of the source model file. If None, the encoding will be
        read from the model, if the encoding is not defined in the model
        file it will be set to 'UTF-8'. Default is None.

    """
    def __init__(self, xmile_path, encoding=None):
        self.xmile_path = Path(xmile_path)
        self.root_path = self.xmile_path.parent
        self.xmile_root = self.get_root()
        self.ns = self.xmile_root.nsmap[None]  # namespace of the xmile
        self.view_elements = None

    def __str__(self):
        return "\nXmile model file, loaded from:\n\t%s\n" % self.xmile_path

    @property
    def _verbose(self):
        text = self.__str__()
        for section in self.sections:
            text += section._verbose

        return text

    @property
    def verbose(self):
        print(self._verbose)

    def get_root(self):
        """Read a Xmile file and assign its content to self.model_text"""
        # check for model extension
        if self.xmile_path.suffix.lower() != ".xmile":
            raise ValueError(
                "The file to translate, '%s' " % self.xmile_path
                + "is not a Xmile model. It must end with xmile extension."
            )

        return etree.parse(
            str(self.xmile_path),
            parser=etree.XMLParser(encoding="utf-8", recover=True)
        ).getroot()

    def parse(self):
        # We keep everything in a single section
        # TODO: in order to make macros work we need to split them here in
        # several sections
        self.sections = [FileSection(
                name="__main__",
                path=self.xmile_path.with_suffix(".py"),
                type="main",
                params=[],
                returns=[],
                content_root=self.xmile_root,
                namespace=self.ns,
                split=False,
                views_dict=None)]

        for section in self.sections:
            section._parse()

    def get_abstract_model(self):
        return AbstractModel(
            original_path=self.xmile_path,
            sections=tuple(section.get_abstract_section()
                           for section in self.sections))