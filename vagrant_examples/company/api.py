import logging
from tastypie.authorization import Authorization
from tastypie.resources import Resource
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpBadRequest, HttpAccepted
from django.http.response import JsonResponse

logger = logging.getLogger()


class ExemploResource(Resource):
    
    class Meta:
        allowed_methods = ['post']
        resource_name = 'exemplo'
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        
        logger.info('REQUEST: %s', bundle.data)
        
        try:
            mensagem = bundle.data['mensagem']
        except KeyError, e:
            logger.error('Faltando o parametro %s.' %str(e))
            raise ImmediateHttpResponse(HttpBadRequest(JsonResponse({'error':'Faltando o parametro %s.' %str(e)})))
        
        raise ImmediateHttpResponse(HttpAccepted(JsonResponse({'success':'Mensagem recebida foi = %s' %str(mensagem)})))
    
