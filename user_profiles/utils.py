import functools
import operator

from django.db.models.constraints import CheckConstraint
from django.db.models import Q


def checkWishOwner(name):
    q_objs = []
    all_field_names = [
        "material",
        "bathroom",
        "decorations",
        "furniture",
        "fabric_textile",
        "hardware_tool",
        "home_appliances",
        "kitchen",
        "landscape_garden",
        "light",
        "rugs_mat",
        "security_protection",
    ]

    for field_name in all_field_names:
        q_obj = Q(
            **{
                f"{f_name}__isnull": (False if field_name == f_name else True)
                for f_name in all_field_names
            }
        )
        q_objs.append(q_obj)

    return CheckConstraint(check=functools.reduce(operator.or_, q_objs), name=name)
