from .signals import set_request_user

class AuditMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if hasattr(request, 'user') and request.user.is_authenticated:
			set_request_user(request.user)
		else:
			set_request_user(None)
		
		response = self.get_response(request)
		return response