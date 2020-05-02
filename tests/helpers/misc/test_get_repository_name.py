"""Helpers: Misc: get_repository_name."""
# pylint: disable=missing-docstring
from custom_components.hacs.helpers.misc import get_repository_name
from custom_components.hacs.repositories.manifest import HacsManifest
from custom_components.hacs.const import ELEMENT_TYPES

from tests.dummy_repository import dummy_repository_base

ELEMENT_TYPES = ELEMENT_TYPES + ["appdaemon", "python_script", "theme"]


def test_everything():
    repository = dummy_repository_base()
    repository.data.full_name = "test/TEST-REPOSITORY-NAME"
    repository.repository_manifest = HacsManifest.from_dict(
        {"name": "TEST-HACS_MANIFEST"}
    )
    repository.integration_manifest = {"name": "TEST-MANIFEST"}

    for category in ELEMENT_TYPES:
        repository.data.category = category
        name = get_repository_name(repository)
        assert name == "TEST-HACS_MANIFEST"


def test_integration_manifest():
    repository = dummy_repository_base()
    repository.data.category = "integration"
    repository.data.full_name = "test/TEST-REPOSITORY-NAME"
    repository.repository_manifest = HacsManifest.from_dict({})
    repository.integration_manifest = {"name": "TEST-MANIFEST"}

    name = get_repository_name(repository)
    assert name == "TEST-MANIFEST"


def test_repository_name():
    repository = dummy_repository_base()
    repository.data.full_name = "test/TEST-REPOSITORY-NAME"
    repository.repository_manifest = HacsManifest.from_dict({})

    name = get_repository_name(repository)
    assert name == "Test Repository Name"
