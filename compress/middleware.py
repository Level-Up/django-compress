from django.utils.html import strip_spaces_between_tags


class MinifyHTMLMiddleware(object):
    def process_response(self, request, response):
        if response['content-type'][:9] == 'text/html':
            response.content = strip_spaces_between_tags(response.content.strip())

        return response
