import starkbank

private_key = """
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIDGXLChx9oiVlngO/ysyrb79oJy32Ux6aHNN+lcpmDxmoAcGBSuBBAAK
oUQDQgAEmrlKSnU70LNi3IVBkgTyBwh6J4+gdwFlACK5EeoCt3q7Adjmp09rVd6H
RsLkkcuSYQzwkZ30e/gE9YRrGp0klA==
-----END EC PRIVATE KEY-----
"""

project = starkbank.Project(
    environment="sandbox",
    id="4740157227925504",
    private_key=private_key
)
starkbank.user = project