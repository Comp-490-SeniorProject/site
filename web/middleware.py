import secure

__all__ = ("set_secure_headers",)

csp_policy = (
    secure.ContentSecurityPolicy()
    .default_src("'none'")
    .base_uri("'self'")
    .connect_src("'self'", "api.spam.com")
    .frame_src("'none'")
    .img_src("'self'", "static.spam.com")
)
secure_headers = secure.Secure(csp=csp_policy)


def set_secure_headers(get_response):
    def middleware(request):
        response = get_response(request)
        secure_headers.framework.django(response)
        return response

    return middleware
