from flask import Response, jsonify
import json


class APIResponse():
    '''
    @data: dict
    @status: int
    @mimetype: str
    @return: Response
    '''

    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    def __new__(cls, *args):
        return cls.__getResponse(cls, *args)

    def __getResponse(self, data: dict = {}, status: int = 0, mimetype: str = ''):
        return Response(
            response=json.dumps(data),
            status=status if status else self.default_status,
            mimetype=mimetype if mimetype else self.default_mimetype,
        )
