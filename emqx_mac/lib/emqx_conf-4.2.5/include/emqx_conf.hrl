-record(emqx_conf_info, {app, version, ts}).
-record(emqx_conf, {name, confs}).
-record(emqx_listeners_state, {name, status}).

-define(ZONE_CONFIGS_SPEC,[
    {acl_deny_action, [{type, string},
                       {default, <<"ignore">>},
                       {enum, [<<"ignore">>, <<"disconnect">>]},
                       {description, [{en, <<"The action when acl check reject current operation">>},
                                      {zh, <<"ACL 被拒绝时的处理动作"/utf8>>}]}]},
    {acl_nomatch, [{type, string},
                   {enum, [<<"allow">>, <<"deny">>]},
                   {description, [{en, <<"Allow or deny if no ACL rules matched">>},
                                  {zh, <<"ACL 未命中时允许或拒绝通过验证"/utf8>>}]}]},
    {allow_anonymous, [{type, boolean},
                       {description, [{en, <<"Allow anonymous authentication by default if no auth plugins loaded. Disable the option in production deployment">>},
                                      {zh, <<"如果未加载身份验证插件，则默认情况下允许匿名身份验证。建议在生产部署中禁用该选项！"/utf8>>}]}]},
    {await_rel_timeout, [{type, string},
                         {default, <<"300s">>},
                         {description, [{en, <<"await_rel_timeout">>},
                                        {zh, <<"如果等待 pubrel 超时时间，超时将删除 QoS2 消息（client 发送到 broker）"/utf8>>}]}]},
    {bypass_auth_plugins, [{type, boolean},
                           {default, false},
                           {description, [{en,<<"Allow the zone's clients to bypass authentication step">>},
                                          {zh,<<"允许 zone 的客户端绕过身份验证步骤"/utf8>>}]}]},
    {enable_acl, [{type, string},
                  {default, <<"off">>},
                  {enum, [<<"on">>, <<"off">>]},
                  {description,[{en, <<"Enable ACL check">>},
                                {zh, <<"是否启用 ACL 检查"/utf8>>}]}]},
    {enable_ban, [{type, string},
                  {default, <<"off">>},
                  {enum, [<<"on">>, <<"off">>]},
                  {description, [{en, <<"Enable ban check">>},
                                 {zh, <<"是否启用白名单检查"/utf8>>}]}]},
    {enable_flapping_detect, [{type, string},
                              {default, <<"off">>},
                              {enum, [<<"on">>, <<"off">>]},
                              {description, [{en, <<"Whether to turn on flapping detect">>},
                                             {zh, <<"是否开启 flapping detect"/utf8>>}]}]},
    {enable_stats, [{type, string},
                    {default, <<"off">>},
                    {enum, [<<"on">>, <<"off">>]},
                    {description, [{en, <<"Enable per connection stats">>},
                                   {zh, <<"启用连接状态统计，会降低部分性能"/utf8>>}]}]},
    {force_gc_policy, [{type, string},
                       {description,[{en, <<"Force MQTT connection/session process GC after this number of messages | bytes passed through">>},
                                     {zh, <<"MQTT 连接/消息大小 GC 阈值"/utf8>>}]}]},
    {force_shutdown_policy, [{type, string},
                             {description, [{en, <<"Process message queue length | Memory byte">>},
                                            {zh, <<"进程消息队列长度 ｜ 内存字节"/utf8>>}]}]},
    {idle_timeout, [{type, string},
                    {default, <<"15s">>},
                    {description,[{en, <<"Idle timeout of the MQTT connections">>},
                                  {zh, <<"MQTT 连接空闲超时"/utf8>>}]}]},
    {ignore_loop_deliver, [{type, boolean},
                           {description, [{en, <<"Whether to ignore loop delivery of messages (for MQTT v3.1.1)">>},
                                          {zh, <<"是否忽略消息循环传递，常用于消息桥接"/utf8>>}]}]},
    {keepalive_backoff, [{type, number},
                         {default, 0.75},
                         {description, [{en, <<"The backoff for MQTT keepalive timeout. The broker will kick a connection out until keepalive * backoff * 2 timeout">>},
                                        {zh, <<"MQTT keepalive 超时回退， keepalive * backoff * 2 时将断开连接"/utf8>>}]}]},
    {max_awaiting_rel, [{type, number},
                        {default, 0},
                        {description, [{en, <<"Maximum QoS2 packets (Client -> Broker) awaiting PUBREL, 0 means no limit">>},
                                       {zh, <<"等待 PUBREL 的 QoS2 消息最大数据包数（client->broker），0 表示没有限制"/utf8>>}]}]},
    {max_clientid_len,[{type, number},
                       {description, [{en, <<"Maximum length of MQTT clientid allowed">>},
                                      {zh, <<"MQTT 客户端 ID 的长度限制"/utf8>>}]}]},
    {max_inflight,[{type, number},
                   {default, 0},
                   {description, [{en, <<"Maximum size of the Inflight Window storing QoS1/2 messages delivered but unacked">>},
                                  {zh, <<"保存的已传递但未确认的 QoS1/2 消息的飞行窗口的最大值"/utf8>>}]}]},
    {max_mqueue_len,[{type, number},
                     {default, 0},
                     {description, [{en, <<"Maximum queue length. Enqueued messages when persistent client disconnected, or inflight window is full. 0 means no limit">>},
                                    {zh, <<"排队消息的最大长度，0 表示没有限制"/utf8>>}]}]},
    {max_packet_size,[{type, string},
                      {description, [{en, <<"Maximum MQTT packet size allowed">>},
                                     {zh, <<"最大 MQTT 数据包大小"/utf8>>}]}]},
    {max_qos_allowed,[{type, number},
                      {enum, [0, 1, 2]},
                      {description, [{en, <<"Maximum QoS allowed">>},
                                     {zh, <<"最大 QoS"/utf8>>}]}]},
    {max_subscriptions,[{type, number},
                        {default, 0},
                        {description, [{en, <<"Maximum number of subscriptions allowed, 0 means no limit">>},
                                       {zh, <<"允许的最大订阅数，0 表示无限制"/utf8>>}]}]},
    {max_topic_alias,[{type, number},
                      {description, [{en, <<"Maximum Topic Alias, 0 means no topic alias supported">>},
                                     {zh, <<"最大主题别名数量，0 表示不支持主题别名"/utf8>>}]}]},
    {max_topic_levels,[{type, number},
                       {default, 0},
                       {description, [{en, <<"Maximum topic levels allowed, 0 means no limit">>},
                                      {zh, <<"主题层级限制，0 表示没有限制层级"/utf8>>}]}]},
    {mountpoint, [{type, string},
                  {description, [{en, <<"Topic mount point">>},
                                 {zh, <<"主题挂载点"/utf8>>}]}]},
    {mqueue_default_priority, [{type, string},
                               {default, <<"lowest">>},
                               {enum, [<<"highest">>, <<"lowest">>]},
                               {description,[{en, <<"Default to highest priority for topics not matching priority table">>},
                                             {zh, <<"对于不匹配优先级表的主题，默认为最高优先级"/utf8>>}]}]},
    {mqueue_priorities, [{type, string},
                         {default, <<"none">>},
                         {description, [{en, <<"Topic priorities">>},
                                        {zh, <<"主题优先级"/utf8>>}]}]},
    {mqueue_store_qos0, [{type, boolean},
                         {default, true},
                         {description, [{en, <<"Whether to enqueue QoS0 messages">>},
                                        {zh, <<"是否将 QoS0 的消息存储在队列中"/utf8>>}]}]},
    {publish_limit,[{type, string},
                    {description, [{en, <<"Publish limit">>},
                                   {zh, <<"发布限制"/utf8>>}]}]},
    {quota_conn_messages_routing, [{type, string},
                                   {description, [{en, <<"Quota for the number of times a single client message is forwarded">>},
                                                  {zh, <<"单个客户端消息转发次数的配额"/utf8>>}]}]},
    {quota_overall_messages_routing, [{type, string},
                                      {description, [{en, <<"Quota for the number of times all client messages are forwarded under Zone">>},
                                                     {zh, <<"Zone 下面所有客户端消息转发次数的配额"/utf8>>}]}]},
    {rate_limit_conn_bytes_in, [{type, string},
                                {description, [{en, <<"Client byte inflow rate limit">>},
                                               {zh, <<"客户端字节流入速率限制"/utf8>>}]}]},
    {rate_limit_conn_messages_in, [{type,string},
                                   {description, [{en, <<"Client Publish message inflow rate limit">>},
                                                  {zh, <<"客户端 Publish 消息流入速率限制"/utf8>>}]}]},
    {response_information, [{type, string},
                            {description,[{en, <<"Response information">>},
                                          {zh, <<"响应信息"/utf8>>}]}]},
    {retain_available, [{type,boolean},
                        {description, [{en, <<"Whether the Server supports MQTT retained messages">>},
                                      {zh, <<"是否启用 Retain 消息"/utf8>>}]}]},
    {retry_interval, [{type, string},
                      {default, <<"30s">>},
                      {description, [{en, <<"retry_interval">>},
                                     {zh, <<"QoS 1/2 消息传递的重试间隔"/utf8>>}]}]},
    {server_keepalive, [{type, number},
                        {description, [{en, <<"The Keepalive time specified by the server">>},
                                       {zh, <<"服务端指定的 Keepalive 时间"/utf8>>}]}]},
    {session_expiry_interval, [{type, string},
                               {default, <<"2h">>},
                               {description, [{en, <<"Default session expiry interval for MQTT V3.1.1 connections">>},
                                             {zh, <<"会话到期时长 MQTT V3.1.1"/utf8>>}]}]},
    {shared_subscription, [{type, boolean},
                           {description,[{en, <<"Whether the Server supports MQTT Shared Subscriptions">>},
                                         {zh, <<"是否启用共享订阅"/utf8>>}]}]},
    {strict_mode, [{type, boolean},
                   {default, false},
                   {description,[{en, <<"Whether to parse the MQTT frame in strict mode">>},
                                 {zh, <<"是否在严格模式下解析 MQTT 帧"/utf8>>}]}]},
    {upgrade_qos, [{type, string},
                   {default, <<"off">>},
                   {enum, [<<"on">>, <<"off">>]},
                   {description,[{en, <<"Force to upgrade QoS according to subscription">>},
                                 {zh, <<"根据订阅强制升级 QoS"/utf8>>}]}]},
    {use_username_as_clientid, [{type, boolean},
                                {default, false},
                                {description, [{en, <<"Whether use username replace clientid">>},
                                               {zh, <<"是否使用用户名替换客户端 ID"/utf8>>}]}]},
    {wildcard_subscription, [{type, boolean},
                             {description, [{en, <<"Whether the Server supports MQTT Wildcard Subscriptions">>},
                                            {zh, <<"是否启用通配符订阅"/utf8>>}]}]}
]).

-define(SSL_CONFIGS_SPEC, [
    {keyfile, [{order, 1},
               {type, string},
               {description, [{en, <<"The Key file">>},{zh, <<"秘钥文件"/utf8>>}]}]},
    {certfile, [{order, 2},
                {type, string},
                {description, [{en, <<"The Certfile file">>},{zh, <<"证书文件"/utf8>>}]}]},
    {cacertfile, [{order, 3},
                  {type, string},
                  {description, [{en, <<"The CA certificate file">>},
                                 {zh, <<"CA证书文件"/utf8>>}]}]},
    {verify, [{order, 4},
              {type, boolean},
              {default, false},
              {description, [{en, <<"Enable Two-Way SSL">>}, {zh, <<"是否开启双认证"/utf8>>}]}]},
    {fail_if_no_peer_cert, [{order, 5},
                            {type, boolean},
                            {default, false},
                            {description,[{en, <<"fail_if_no_peer_cert">>},
                                          {zh, <<"关闭无证书客户端连接"/utf8>>}]}]},
    {tls_versions, [{order, 6},
                    {type, string},
                    {enum, [<<"tlsv1.2,tlsv1.1,tlsv1">>, <<"tlsv1.2">>, <<"tlsv1.2,tlsv1.1">>, <<"tlsv1">>]},
                    {description, [{en, <<"TLS Version">>},
                                   {zh, <<"TLS 版本"/utf8>>}]}]},
    {ciphers, [{order, 7},
               {type, string},
               {default, <<"ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-DES-CBC3-SHA,ECDH-ECDSA-AES256-GCM-SHA384,ECDH-RSA-AES256-GCM-SHA384,ECDH-ECDSA-AES256-SHA384,ECDH-RSA-AES256-SHA384,DHE-DSS-AES256-GCM-SHA384,DHE-DSS-AES256-SHA256,AES256-GCM-SHA384,AES256-SHA256,ECDHE-ECDSA-AES128-GCM-SHA256,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,ECDH-ECDSA-AES128-GCM-SHA256,ECDH-RSA-AES128-GCM-SHA256,ECDH-ECDSA-AES128-SHA256,ECDH-RSA-AES128-SHA256,DHE-DSS-AES128-GCM-SHA256,DHE-DSS-AES128-SHA256,AES128-GCM-SHA256,AES128-SHA256,ECDHE-ECDSA-AES256-SHA,ECDHE-RSA-AES256-SHA,DHE-DSS-AES256-SHA,ECDH-ECDSA-AES256-SHA,ECDH-RSA-AES256-SHA,AES256-SHA,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,DHE-DSS-AES128-SHA,ECDH-ECDSA-AES128-SHA,ECDH-RSA-AES128-SHA,AES128-SHA">>},
               {description, [{en, <<"Ciphers">>},{zh,<<"加密套件"/utf8>>}]}]},
    {psk_ciphers, [{order, 8},
                   {type, string},
                   {default, <<"PSK-AES128-CBC-SHA,PSK-AES256-CBC-SHA,PSK-3DES-EDE-CBC-SHA,PSK-RC4-SHA">>},
                   {description, [{en, <<"Ciphers">>},{zh,<<"加密套件"/utf8>>}]}]},
    {handshake_timeout, [{order, 9},
                         {type, string},
                         {default, <<"15s">>},
                         {description, [{en, <<"Handshake Timeout">>},
                                        {zh, <<"握手超时时间"/utf8>>}]}]},
    {dhfile, [{order, 10},
              {type, string},
              {description, [{en, <<"dhfile">>}, {zh, <<"dhfile"/utf8>>}]}]},
    {honor_cipher_order, [{order, 11},
                          {type, string},
                          {enum, [<<"on">>, <<"off">>]},
                          {description, [{en, <<"If set to on, use the server preference for cipher selection. If set to off (the default), use the client preference.">>},
                                         {zh, <<"如果设置为on，则使用服务器偏好来选择密码。如果设置为off（默认值），则使用客户端偏好"/utf8>>}]}]},
    {secure_renegotiate, [{order, 12},
                          {type, string},
                          {enum, [<<"on">>, <<"off">>]},
                          {description, [{en, <<"Specifies if to reject renegotiation attempt that does not live up to RFC 5746">>},
                                         {zh, <<"指定是否拒绝不符合RFC 5746的重新协商尝试"/utf8>>}]}]},
    {reuse_sessions, [{order, 13},
                      {type, string},
                      {default, <<"on">>},
                      {enum, [<<"on">>, <<"off">>]},
                      {description, [{en, <<"Reuse Sessions">>},
                                     {zh, <<"是否开启SSL会话重用"/utf8>>}]}]}
]).

-define(TCP_CONFIGS_SPEC, [
    {listener, [{order, 1},
                {type, string},
                {required, true},
                {description, [{en, <<"Listener">>},
                               {zh, <<"监听地址"/utf8>>}]}]},
    {acceptors, [{order, 2},
                 {type, number},
                 {default, 8},
                 {required, true},
                 {description, [{en, <<"The number of acceoptors, It just works for TCP/SSL/DTLS socket">>},
                                {zh, <<"接收器数量，执行 accept 操作的进程数量，仅对 TCP/SSL/DTLS Socket 有效"/utf8>>}]}]},
    {max_connections, [{order, 3},
                       {type, number},
                       {default, 102400},
                       {description, [{en,<<"The maximum connections of listener">>},
                                      {zh,<<"该监听器允许的最大连接数"/utf8>>}]}]},
    {zone, [{order, 4},
            {type, string},
            {default, <<"external">>},
            {description, [{en, <<"zone">>}, {zh, <<"使用Zone的名字"/utf8>>}]}]},
    {active_n, [{order, 5},
                {type, nunber},
                {default, 100},
                {description, [{en, <<"Specify the {active, N} option for the Socket">>},
                            {zh, <<"设置 Socket 的 {active, N} 选项"/utf8>>}]}]},
    {max_conn_rate, [{order, 6},
                     {type, number},
                     {default, 1000},
                     {description,[{en, <<"Allowed connections per second">>},
                                   {zh, <<"该监听器每秒允许的最大连接个数"/utf8>>}]}]},
    {peer_cert_as_username, [{order, 7},
                             {type, string},
                             {enum, [cn, dn, crt]},
                             {description, [{en, <<"Enable the option for X.509 certificate based authentication.EMQX will use the common name of certificate as MQTT username.">>},
                                            {zh, <<"启用基于X.509证书的身份验证选项，EMQX将使用证书的通用名称作为MQTT的用户名。"/utf8>>}]}]},
    {proxy_protocol, [{order, 8},
                      {type, string},
                      {default, <<"off">>},
                      {enum, [<<"on">>, <<"off">>]},
                      {description, [{en, <<"Enable the Proxy Protocol V1/2 if the EMQ X cluster is deployed behind HAProxy or Nginx">>},
                                     {zh, <<"开启 Proxy Protocol V1/2，如果 EMQ X 集群部署在 HAProxy 或 Nginx 后"/utf8>>}]}]},
    {proxy_protocol_timeout, [{order, 9},
                              {type, string},
                              {default, <<"15s">>},
                              {description, [{en, <<"The timeout for accepting proxy protocol, EMQ X will close the TCP connection if no proxy protocol packet recevied within the timeout">>},
                                             {zh, <<"处理 Proxy Protocol 的超时时间，如果超过该时间未收到 Proxy Protocol 的报文，EMQ X 将关闭该 TCP 连接"/utf8>>}]}]},
    {send_timeout, [{order, 10},
                    {type, string},
                    {default, <<"15s">>},
                    {description, [{en, <<"The TCP send timeout">>},
                                   {zh, <<"TCP 报文发送超时时间"/utf8>>}]}]},
    {send_timeout_close, [{order, 11},
                          {type, string},
                          {default, <<"off">>},
                          {enum, [<<"on">>, <<"off">>]},
                          {description, [{en, <<"Close the TCP connection if send timeout">>},
                                         {zh, <<"关闭发送超时的 TCP 连接"/utf8>>}]}]},
    {reuseaddr, [{order, 12},
                 {type, boolean},
                 {default, true},
                 {description, [{en, <<"The SO_REUSEADDR flag for listener">>},
                                {zh, <<"设置 Socket 的 SO_REUSEADDR 标识"/utf8>>}]}]},
    {nodelay, [{order, 13},
               {type, boolean},
               {default, true},
               {description,[{en, <<"The TCP_NODELAY flag for MQTT connections. Small amounts of data are sent immediately if the option is enabled The TCP backlog defines the maximum length that the queue of pending">>},
                             {zh, <<"设置 TCP_NODELAY 标识"/utf8>>}]}]},
    {backlog, [{order, 14},
               {type, number},
               {default, 8},
               {required, true},
               {description,[{en, <<"The TCP backlog defines the maximum length that the queue of pending connections can grow to">>},
                             {zh, <<"TCP 连接队列最大长度"/utf8>>}]}]},
    {recbuf, [{order, 15},
              {type, string},
              {default, <<"2KB">>},
              {description, [{en, <<"The receive buffer of socket (os kernel)">>},
                             {zh, <<"Socket 接收缓冲区大小 (操作系统内核级)"/utf8>>}]}]},
    {sndbuf, [{order, 16},
              {type, string},
              {default, <<"2KB">>},
              {description, [{en, <<"The send buffer of socket (os kernel)">>},
                             {zh, <<"Socket 发送缓冲区大小 (操作系统内核级)"/utf8>>}]}]}
]).

-define(WS_CONFIGS_SPEC, [
    {mqtt_path, [{order, 1},
                 {type, string},
                 {default, <<"/mqtt">>},
                 {description, [{en, <<"mqtt_path">>}, {zh, <<"mqtt_path"/utf8>>}]}]},
    {mqtt_piggyback, [{order, 2},
                      {type, string},
                      {default, <<"multiple">>},
                      {enum, [<<"single">>, <<"multiple">>]},
                      {description, [{en, <<"Whether a WebSocket message is allowed to contain multiple MQTT packets">>},
                                     {zh, <<"WebSocket消息是否允许包含多个MQTT包"/utf8>>}]}]},
    {verify_protocol_header, [{order, 3},
                              {type, string},
                              {default, <<"off">>},
                              {enum, [<<"on">>, <<"off">>]},
                              {description, [{en, <<"Whether to validate the protocol header">>},
                                             {zh, <<"是否验证MQTT协议头"/utf8>>}]}]},
    {max_frame_size, [{order, 4},
                      {type, number},
                      {description, [{en, <<"Websocket Frame size">>},
                                     {zh, <<"Websocket 报文大小"/utf8>>}]}]},
    {idle_timeout, [{order, 5},
                    {type, string},
                    {default, <<"30s">>},
                    {description, [{en, <<"Idle timeout of the MQTT connection.">>},
                                   {zh, <<"MQTT连接的延迟超时"/utf8>>}]}]}
]).
