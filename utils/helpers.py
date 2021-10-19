import os
import wtforms as forms


def get_key_val(d: dict = {}, key: str = ''):
    return d.get(key)


def get_env_val(key: str):
    return os.getenv(key)


def get_form_data(form: forms):
    feilds = form.__dict__.get('_fields')
    return {str(f): form[f].data for f in feilds}


def serialize_all(obj_list: list = []):
    '''
    @obj_list list(Models)
    '''
    data = []
    try:
        data = [obj.serialize() for obj in obj_list]
    except Exception as e:
        pass
    return data
