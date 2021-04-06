-define(APP, emqx_backend_dynamo).

-record(action, {function, pool}).

-define(ONLINE, 1).
-define(OFFLINE, 0).

-define(RETAIN, <<"mqtt_retain">>).
-define(MSG, <<"mqtt_msg">>).
-define(TOPIC_MSG, <<"mqtt_topic_msg_map">>).
-define(ACKED, <<"mqtt_acked">>).
-define(SUB, <<"mqtt_sub">>).
-define(CLIENT, <<"mqtt_client">>).
