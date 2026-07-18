import ssl

def get_tls_context(node_name):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(
        certfile=f"~/sentinel_probe/security/nodes/{node_name}/{node_name}.crt",
        keyfile=f"~/sentinel_probe/security/nodes/{node_name}/{node_name}.key"
    )
    context.load_verify_locations(cafile="~/sentinel_probe/security/certs/rootCA.pem")
    context.verify_mode = ssl.CERT_REQUIRED
    return context
