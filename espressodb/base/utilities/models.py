"""Help functions to inspect models
"""
from typing import Optional
from typing import Tuple
from typing import List

from django.db import models

from espressodb.base.utilities.apps import get_project_apps
from espressodb.base.models import Base


def get_espressodb_models(exclude_apps: Optional[Tuple[str]] = None) -> models.Model:
    """Returns all installed project models which are not in the exclude list
    """
    return [
        model for app in get_project_apps(exclude_apps) for model in app.get_models()
    ]


def iter_tree(model: Base, name: Optional[str] = None) -> List[Tuple[str, str]]:
    """Extracts all foreign keys of model and inserters them in list.

    Returns strings in flat tree format, e.g., `propagator.gaugeconfig`.

    **Arguments**
        model: Base
            A child of the base model.

        name: Optional[str] = None
            The (path) name of the model.

    **Returns**
        tree: List[Tuple[str, str]]
            First element of tuple are name names of the foreign keys in format
            `{name}.{field.name}`.
            Second element are the actual classes.
    """
    tree = []

    for field in model.get_open_fields():
        if isinstance(field, models.ForeignKey):
            tree.append(
                (f"{name}.{field.name}" if name else field.name, field.related_model)
            )

    return tree
