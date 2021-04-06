-define(APP, emqx_schema_registry).

-define(is_wildcard(W), (W) =:= <<"*">>).
-define(BAD_SCHEMA_ARG(REASON), {emqx_schema_badarg, (REASON)}).
-define(INCOMPATIBLE(REASON), {emqx_schema_incompatible, (REASON)}).

-type schema_name() :: binary().
-type schema_text() :: binary().

-type parser_type() :: avro | protobuf | json | '3rd-party'.
-type parser_addr() :: {tcp, inet:hostname() | inet:ip_address(), inet:port_number()}
                     | {http, httpc:url()}
                     | {resource_id, binary()}.
-type parser_opts() :: #{'3rd_party_opts' => binary(),
                         'connect_timeout' => integer(),
                         'parse_timeout' => integer(),
                         atom() => term()}.

-type decoder() :: fun((Data::binary()) -> term()).
-type encoder() :: fun((Term::binary()) -> iodata()).
-type destroy() :: fun(() -> ok).

-record(schema, {
    name :: schema_name(),
    schema :: schema_text(),
    parser_type :: parser_type(),
    parser_addr :: parser_addr(), %% only for parser_type = '3rd-party'
    parser_opts = #{} :: parser_opts(),
    descr = <<>> :: binary()
}).

-record(parser, {
    name :: schema_name(),
    decoder :: decoder(),
    encoder :: encoder(),
    destroy :: destroy()
}).

%% 3rd-party result codes
-define(CODE_REQ, 0).
-define(CODE_SUCCESS, 1).
-define(CODE_BAD_FORMAT, 2).
-define(CODE_INTERNAL, 3).
-define(CODE_UNKNOWN, 4).
