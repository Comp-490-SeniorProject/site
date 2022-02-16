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

# Secure 0.3.0 mistakenly has a semicolon in the default value,
# which is fixed in an unreleased version.
permissions_policy = secure.PermissionsPolicy()
permissions_policy.value = (
    "accelerometer=(), ambient-light-sensor=(), autoplay=(), battery=(), "
    "camera=(), clipboard-read=(), clipboard-write=(), cross-origin-isolated=(), "
    "display-capture=(), document-domain=(), encrypted-media=(), "
    "execution-while-not-rendered=(), execution-while-out-of-viewport=(), "
    "fullscreen=(), gamepad=(), geolocation=(), gyroscope=(), magnetometer=(), "
    "microphone=(), midi=(), navigation-override=(), payment=(), "
    "picture-in-picture=(), publickey-credentials-get=(), screen-wake-lock=(), "
    "speaker-selection=(), sync-xhr=(), usb=(), web-share=(), "
    "xr-spatial-tracking=()"
)

secure_headers = secure.Secure(csp=csp_policy, permissions=permissions_policy)


def set_secure_headers(get_response):
    def middleware(request):
        response = get_response(request)
        secure_headers.framework.django(response)
        return response

    return middleware
