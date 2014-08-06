from flask import Flask, request, abort


from {{package}} import config


class MyFlask(Flask):

    def process_response(self, response):
        # modify the response if needed
        # for example: request.headers['Content-Type']
        # can be used to change the output on the fly
        return response


class NotFoundError(Exception):
    pass

class InvalidBodyError(KeyError):
    pass



app = MyFlask(__name__)
app.config['debug'] = config.is_debug

# register the routes with every module
for name in config.modules:
    resource = __import__('{{package}}.%s.resource' % name, globals(), locals(), ['mod'], -1)
    app.register_blueprint(resource.mod)


"""
Implement error handlers for common HTTP errors
because by default these the response is <HTML>.
"""
json_response = '{"error": %d, "message": "%s"}'


@app.before_request
def before_request():
    mime = request.headers['Content-Type']
    if mime != 'application/json':
        abort(415)

@app.errorhandler(InvalidBodyError)
def bad_request_invalid(error=None):
    return json_response % (400, "The request body did not match the resource schema"), 400

@app.errorhandler(400)
def bad_request(error=None):
    return json_response % (400, "Bad request, please read the code"), 400

@app.errorhandler(415)
def not_supported(error=None):
    mime = request.headers['Content-Type']
    return json_response % (415, "Unsupported mime type " + mime), 415


@app.errorhandler(NotFoundError)
@app.errorhandler(404)
def not_found(error=None):
    return json_response % (404, "Resource not found"), 404


@app.errorhandler(405)
def method_not_allowed(error=None):
    return json_response % (405, "Method not allowed"), 405


@app.errorhandler(500)
def server_error(error=None):
    return json_response % (500, "Oops, the code broke, we mailed our code monkeys to fix it!"), 500


@app.errorhandler(501)
def not_implemented(error=None):
    return json_response % (501, "Method not implemented, please content the developers"), 501
