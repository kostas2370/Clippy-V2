import io
import g4f
import json
from .exceptions import InvalidJsonFormatError


def check_json(json_file):
    if "scenes" not in json_file:
        return False

    if "title" not in json_file:
        return False

    if len(json_file['scenes']) == 0:
        return False

    if "dialogue" not in json_file['scenes'][0]:
        return False

    return True


def get_reply(prompt, time=0, reply_format="json", gpt_model='gpt-3.5-turbo'):
    time += 1
    g4f.logging = True  # enable logging
    g4f.check_version = False

    gpt_model = g4f.models.gpt_4 if gpt_model == "gpt-4" else 'gpt-3.5-turbo'

    response = g4f.ChatCompletion.create(model = gpt_model, messages = [{"content": prompt}], stream = True, )
    x = io.StringIO()
    for message in response:
        x.write(message)

    if reply_format == "json":
        x = x.getvalue()
        x = x[x.index('{'):len(x) - (x[::-1].index('}'))]

        try:

            js = json.loads(x)

            if not check_json(js):
                raise InvalidJsonFormatError()

            return js

        except InvalidJsonFormatError:
            if time == 5:
                raise Exception("Max gpt limit is 5 , try again with different prompt !!")

            return get_reply(prompt, time = time, gpt_model = gpt_model)

    return x


def get_update_sentence(prompt):

    response = g4f.ChatCompletion.create(model = 'gpt-3.5-turbo', messages = [{"content": prompt}], stream = True, )
    x = io.StringIO()
    for message in response:
        x.write(message)

    return x.getvalue()
