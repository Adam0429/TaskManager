-define(DEFAULT_COAP_PORT, 5683).
-define(DEFAULT_COAPS_PORT, 5684).

-define(MAX_BLOCK_SIZE, 1024).
-define(DEFAULT_MAX_AGE, 60).

-define(UDP_SOCKOPTS, []).

-record(coap_message, {type, method, id, token = <<>>, options = [], payload = <<>>}).
-record(coap_content, {
    % supported options
    etag,
    max_age = ?DEFAULT_MAX_AGE,
    content_format,
    uri_host,
    uri_port,
    uri_query,
    uri_path,
    location_path,
    location_query,
    if_match,
    if_none_match,
    accept,
    proxy_uri,
    proxy_scheme,
    size1,
    observe,
    block1,
    block2,
    % payload
    payload = <<>>
    }).

-type coap_message() :: #coap_message{}.
-type coap_content() :: #coap_content{}.
