from typing import List, Dict

import rdflib
from .constants import REQUIRED_ATTRIBUTES, OG_NAMESPACES, OG_TYPES


class OGP:
    """Class to consume HTML/XHTML and extract Open Graph metadata.

    Ingests a string containing HTML/XHTML page data, extracts the Open Graph_
    metadata from it and makes those available via attributes on the object.

    .. _Open Graph: http://opengraphprotocol.org/

    OpenGraph metadata is available as attributes on object.

    Properties
    -------------
    is_valid
        return True if all required attributes exist and are non-empty
    properties
        return a List[str] of all Open Graph metadata on webpage
    """

    def __init__(self, data: str) -> None:
        """
        :param data: str of HTML/XHTML for the website to be parsed
        :type data: str
        """
        self._properties: Dict[str, OG_TYPES] = {}
        self._graph = rdflib.Graph()
        self._data = data

    def __getattr__(self, item: str) -> OG_TYPES:
        if item in self._properties:
            return self._properties[item]
        results = []
        if len(self._graph) == 0:
            self._parse_data()
        for ns in OG_NAMESPACES:
            triples = self._graph[: ns[item] :]
            for triple in triples:
                results.append(triple[-1].toPython())
        if len(results) == 0:
            raise AttributeError(f"no attribute '{item}' exists")
        if len(results) == 1:
            self._properties[item] = results[0]
            return self._properties[item]
        self._properties[item] = results
        return self._properties[item]

    def _parse_data(self) -> None:
        assert self._data
        self._graph.parse(data=self._data, format="html")

    def _attr_is_valid(self, attr: str) -> bool:
        return len(getattr(self, attr, "")) > 0

    @property
    def is_valid(self) -> bool:
        """Make sure all required attributes have been found.

        For Open Graph data to be valid, it has to contain the following
        attributes:
            - url
            - title
            - type
            - image
        """
        return all([self._attr_is_valid(attr) for attr in REQUIRED_ATTRIBUTES])

    @property
    def properties(self) -> List[str]:
        if len(self._graph) == 0:
            self._parse_data()
        for _, prop, value in self._graph:
            for ns in OG_NAMESPACES:
                if prop.startswith(ns):
                    self._properties[prop.replace(ns, "")] = value
        return list(self._properties.keys())
