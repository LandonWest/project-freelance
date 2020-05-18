from uuid import uuid4

from app.errors import PublicIDCreationError


def generate_public_id(model_name):
    """Function factory for creating public id's in the form of uuid4-model_abreviation"""
    mapping = {"User": "usr", "Address": "adr"}
    suffix = mapping.get(model_name)
    if not suffix:
        raise PublicIDCreationError(
            f'"{model_name}" is not mapped. Public ID creation function failed.'
        )

    def wrapper():
        return str(uuid4()) + f"-{suffix}"

    return wrapper
