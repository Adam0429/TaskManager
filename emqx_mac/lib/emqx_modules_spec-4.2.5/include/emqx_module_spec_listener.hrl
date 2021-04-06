%%--------------------------------------------------------------------
%% Copyright (c) 2019 EMQ Technologies Co., Ltd. All Rights Reserved.
%%
%% @doc
%%--------------------------------------------------------------------

-ifndef(EMQX_MODULE_SPEC_LISTENER_HRL).

-define(EMQX_MODULE_SPEC_LISTENER_HRL, true).

%%--------------------------------------------------------------------
%% Common listener spec confs

-define(LISTENER_SPEC_ESOCKD, #{
    acceptors => #{
        order => 1,
        type => number,
        required => true,
        default => 8,
        title => #{en => <<"Acceptors">>, zh => <<"接收器数量"/utf8>>},
        description => #{en => <<"The number of acceoptors, It just works for TCP/SSL/DTLS socket">>,
                         zh => <<"接收器数量，执行 accept 操作的进程数量，仅对 TCP/SSL/DTLS Socket 有效"/utf8>>}},
    active_n => #{
        order => 2,
        type => number,
        required => true,
        default => 100,
        title => #{en => <<"ActiveN">>, zh => <<"ActiveN"/utf8>>},
        description => #{en => <<"Specify the {active, N} option for the Socket">>,
                         zh => <<"设置 Socket 的 {active, N} 选项"/utf8>>}},
    max_conn_rate => #{
        order => 3,
        type => number,
        required => false,
        default => 1000,
        title => #{en => <<"Max Connection Rate">>, zh => <<"最大连接速率"/utf8>>},
        description => #{en => <<"Allowed connections per second">>,
                         zh => <<"该监听器每秒允许的最大连接个数"/utf8>>}},
    max_connections => #{
        order => 4,
        type => number,
        required => false,
        default => 1000000,
        title => #{en => <<"Max Connections">>, zh => <<"最大连接数"/utf8>>},
        description => #{en => <<"The maximum connections of listener">>,
                         zh => <<"该监听器允许的最大连接数"/utf8>>}},
    proxy_protocol => #{
        order => 5,
        type => boolean,
        required => false,
        default => false,
        title => #{en => <<"Proxy Protocol">>, zh => <<"开启 Proxy Protocol"/utf8>>},
        description => #{en => <<"Enable the Proxy Protocol V1/2 if the EMQ X cluster is "
                                    "deployed behind HAProxy or Nginx">>,
                         zh => <<"开启 Proxy Protocol V1/2，如果 EMQ X 集群部署在 HAProxy 或 Nginx 后"/utf8>>}},
    proxy_protocol_timeout => #{
        order => 6,
        type => string,
        required => false,
        default => <<"3s">>,
        title => #{en => <<"Proxy Protocol Timeout">>, zh => <<"Proxy Protocol 处理超时时间"/utf8>>},
        description => #{en => <<"The timeout for accepting proxy protocol, EMQ X will close "
                                    "the TCP connection if no proxy protocol packet recevied within the timeout">>,
                         zh => <<"处理 Proxy Protocol 的超时时间，如果超过该时间未收到 Proxy Protocol 的报文，"
                                    "EMQ X 将关闭该 TCP 连接"/utf8>>}},
    sndbuf => #{
        order => 7,
        type => string,
        required => false,
        default => <<"2KB">>,
        title => #{en => <<"Send Buffer">>, zh => <<"发送缓冲区"/utf8>>},
        description => #{en => <<"The send buffer of socket (os kernel)">>,
                         zh => <<"Socket 发送缓冲区大小 (操作系统内核级)"/utf8>>}},
    recbuf => #{
        order => 8,
        type => string,
        required => false,
        default => <<"2KB">>,
        title => #{en => <<"Receive Buffer">>, zh => <<"接收缓冲区"/utf8>>},
        description => #{en => <<"The receive buffer of socket (os kernel)">>,
                         zh => <<"Socket 接收缓冲区大小 (操作系统内核级)"/utf8>>}},
    reuseaddr => #{
        order => 9,
        type => boolean,
        required => false,
        default => true,
        title => #{en => <<"SO_REUSEADDR Flag">>, zh => <<"SO_REUSEADDR 标识"/utf8>>},
        description => #{en => <<"The SO_REUSEADDR flag for listener">>,
                         zh => <<"设置 Socket 的 SO_REUSEADDR 标识"/utf8>>}}
}).

-define(LISTENER_SPEC_UDP_OPTIONS, #{}).

-define(LISTENER_SPEC_TCP_OPTIONS, #{
    backlog => #{
        order => 1,
        type => number,
        required => false,
        default => 1000,
        title => #{en => <<"Backlog">>, zh => <<"TCP 连接队列长度"/utf8>>},
        description => #{en => <<"The TCP backlog defines the maximum length that the queue of pending"
                                 "connections can grow to">>,
                         zh => <<"TCP 连接队列最大长度"/utf8>>}},
     send_timeout => #{
        order => 2,
        type => string,
        required => false,
        default => <<"15s">>,
        title => #{en => <<"Send Timeout">>, zh => <<"发送超时时间"/utf8>>},
        description => #{en => <<"The TCP send timeout">>,
                         zh => <<"TCP 报文发送超时时间"/utf8>>}},
     send_timeout_close => #{
        order => 3,
        type => boolean,
        required => false,
        default => true,
        title => #{en => <<"Send Timeout Close">>, zh => <<"关闭发送超时连接"/utf8>>},
        description => #{en => <<"Close the TCP connection if send timeout">>,
                         zh => <<"关闭发送超时的 TCP 连接"/utf8>>}},
     nodelay => #{
        order => 4,
        type => boolean,
        required => false,
        default => true,
        title => #{en => <<"TCP_NODELAY Flag">>, zh => <<"TCP_NODELAY 标识"/utf8>>},
        description => #{en => <<"The TCP_NODELAY flag for MQTT connections. Small amounts of data are "
                                 "sent immediately if the option is enabled The TCP backlog defines the maximum length that the queue of pending">>,
                         zh => <<"设置 TCP_NODELAY 标识"/utf8>>}}
}).

-define(LISTENER_SPEC_TLS_OPTIONS, #{
    versions => #{
        order => 1,
        type => string,
        enum => [<<"tlsv1.2,tlsv1.1,tlsv1">>, <<"tlsv1.2">>, <<"tlsv1.2,tlsv1.1">>, <<"tlsv1">>],
        required => true,
        default => <<"tlsv1.2,tlsv1.1,tlsv1">>,
        title => #{en => <<"TLS Version">>, zh => <<"TLS 版本"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    ciphers => #{
        order => 2,
        type => string,
        enum => [<<"default">>, <<"psk">>],
        required => true,
        default => <<"default">>,
        title => #{en => <<"Ciphers">>, zh => <<"加密套件"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    handshake_timeout => #{
        order => 3,
        type => string,
        required => false,
        default => <<"15s">>,
        title => #{en => <<"Handshake Timeout">>, zh => <<"握手超时时间"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    verify => #{
        order => 4,
        type => string,
        required => true,
        enum => [<<"verify_none">>, <<"verify_peer">>],
        default => <<"verify_none">>,
        title => #{en => <<"Verify">>, zh => <<"校验类型"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    keyfile => #{
        order => 5,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"Keyfile">>, zh => <<"密钥文件"/utf8>>},
        description => #{en => <<"The Key file path">>,
                         zh => <<"秘钥文件路径"/utf8>>}},
    certfile => #{
        order => 6,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"Certfile">>, zh => <<"证书文件"/utf8>>},
        description => #{en => <<"The certificate file path">>,
                         zh => <<"证书文件路径"/utf8>>}},
    cacertfile => #{
        order => 7,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"CA Certfile">>, zh => <<"CA 证书文件"/utf8>>},
        description => #{en => <<"The CA certificate file path">>,
                         zh => <<"CA 证书文件路径"/utf8>>}},
    fail_if_no_peer_cert => #{
        order => 8,
        type => boolean,
        required => false,
        default => false,
        title => #{en => <<"fail_if_no_peer_cert">>, zh => <<"关闭无证书客户端连接"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}}
    %% secure_renegotiate, reuse_sessions, honor_cipher_order ...
    }).

-define(LISTENER_SPEC_DTLS_OPTIONS, #{
    versions => #{
        order => 1,
        type => string,
        enum => [<<"dtlsv1.2,dtlsv1">>, <<"dtlsv1.2">>, <<"dtlsv1">>],
        required => true,
        default => <<"dtlsv1.2,dtlsv1">>,
        title => #{en => <<"DTLS Version">>, zh => <<"DTLS 协议版本"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    ciphers => #{
        order => 2,
        type => string,
        enum => [<<"default">>, <<"psk">>],
        required => true,
        default => <<"default">>,
        title => #{en => <<"Ciphers">>, zh => <<"加密套件"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    verify => #{
        order => 3,
        type => string,
        required => true,
        enum => [<<"verify_none">>, <<"verify_peer">>],
        default => <<"verify_none">>,
        title => #{en => <<"Verify">>, zh => <<"校验类型"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}},
    keyfile => #{
        order => 4,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"Keyfile">>, zh => <<"密钥文件"/utf8>>},
        description => #{en => <<"The Key file path">>,
                         zh => <<"秘钥文件路径"/utf8>>}},
    certfile => #{
        order => 5,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"Certfile">>, zh => <<"证书文件"/utf8>>},
        description => #{en => <<"The certificate file path">>,
                         zh => <<"证书路径"/utf8>>}},
    cacertfile => #{
        order => 6,
        type => file,
        required => false,
        default => <<"">>,
        title => #{en => <<"CA Certfile">>, zh => <<"CA 证书文件"/utf8>>},
        description => #{en => <<"The CA certificate file path">>,
                         zh => <<"CA 证书文件路径"/utf8>>}},
    fail_if_no_peer_cert => #{
        order => 7,
        type => boolean,
        required => false,
        default => false,
        title => #{en => <<"fail_if_no_peer_cert">>, zh => <<"关闭无证书客户端连接"/utf8>>},
        description => #{en => <<"">>, zh => <<"">>}}
    }).

-endif.
