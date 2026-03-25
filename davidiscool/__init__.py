"""This module contains a very useful function.
"""


def return_the_best(name: str) -> str:
    """Return whether <name> is the best."""
    if name == "David":
        return "David is the best!"
    else:
        return f"{name} is pretty good too, I guess"
