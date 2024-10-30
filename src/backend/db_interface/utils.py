def class_to_dict(obj):
    """
    Converte un oggetto in un dizionario, includendo solo gli attributi dell'istanza.

    Args:
        obj: Oggetto di cui creare il dizionario

    Returns:
        dict: Dizionario con attributi e valori dell'oggetto
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("L'oggetto fornito non è una classe o non ha attributi di istanza.")
    out = {key: value for key, value in obj.__dict__.items()}
    del out['_sa_instance_state']
    return out