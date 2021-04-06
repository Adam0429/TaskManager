
-define(APP, emqx_tcp).

%% 65535 Bytes
-define(MAX_PACKET_SIZE, 16#ffff).

-define(TCP_PROTO_V1, 1).


-record(tcp_packet_conn, {client_id, keepalive, username, password, version}).

-record(tcp_packet_connack, {code, msg}).

-record(tcp_packet_datatrans, {length, data}).

-record(tcp_packet_ping, {}).

-record(tcp_packet_pong, {}).

-record(tcp_packet_disconn, {}).

-define(FRAME_TYPE(Pkt), begin
                             case tuple_to_list(Pkt) of
                                 [tcp_packet_conn|_]      -> conn;
                                 [tcp_packet_connack|_]   -> connack;
                                 [tcp_packet_datatrans|_] -> datatrans;
                                 [tcp_packet_ping|_]      -> ping;
                                 [tcp_packet_pong|_]      -> pong;
                                 [tcp_packet_disconn|_]   -> disconn
                             end
                         end).

%%------------------------------------------------------------------------------
%% Protocols Defination

-define(FRAME_TYPE_CONN,      1).
-define(FRAME_TYPE_CONNACK,   2).
-define(FRAME_TYPE_DATATRANS, 3).
-define(FRAME_TYPE_PING,      4).
-define(FRAME_TYPE_PONG,      5).
-define(FRAME_TYPE_DISCON,    6).

-define(CONNACK_SUCCESSFUL, 0).
-define(CONNACK_AUTHFAILED, 1).
-define(CONNACK_ILLEGALVER, 2).

