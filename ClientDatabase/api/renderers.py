import json

from rest_framework.renderers import JSONRenderer
# сократить до одной функции рендера для всех views


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        token = data.get('token', None)
        if errors is not None:
            return super(UserJSONRenderer, self).render(data)
        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({'user': data})


class DocTypeJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        if len(data) <= 1:
            errors = data.get('errors', None)
            if errors is not None:
                return super(DocTypeJSONRenderer, self).render(data)
        return json.dumps({'doc_type': data})


class DocumentJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        if len(data) <= 1:
            errors = data.get('errors', None)
            if errors is not None:
                return super(DocumentJSONRenderer, self).render(data)
        return json.dumps({'document': data})


class NoticePeriodsJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        if len(data) <= 1:
            errors = data.get('errors', None)
            if errors is not None:
                return super(NoticePeriodsJSONRenderer, self).render(data)
        return json.dumps({'notice_periods': data})


class EmailsListJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        if len(data) <= 1:
            errors = data.get('errors', None)
            if errors is not None:
                return super(EmailsListJSONRenderer, self).render(data)
        return json.dumps({'emails_list': data})

