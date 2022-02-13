import secure

__all__ = ("set_secure_headers",)

# Angular requires default-src 'self'; style-src 'self' 'unsafe-inline';
# https://angular.io/guide/security#content-security-policy
csp_policy = (
    secure.ContentSecurityPolicy()
    .default_src("'self'")
    .font_src("'self'", "fonts.gstatic.com")
    .style_src("'self'", "'unsafe-inline'", "fonts.googleapis.com")
)
secure_headers = secure.Secure(csp=csp_policy, permissions=secure.PermissionsPolicy())


def set_secure_headers(get_response):
    def middleware(request):
        response = get_response(request)
        secure_headers.framework.django(response)
        return response

    return middleware
