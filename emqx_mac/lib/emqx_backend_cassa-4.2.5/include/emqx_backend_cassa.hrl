
-define(APP, emqx_backend_cassa).

-define(INSERT_MSG, "insert into msg(topic, msgid, sender, qos, payload, arrived, retain) values(?, ?, ?, ?, ?, ?, ?)").

-define(SELECT_MSG_BY_ID, "select topic, msgid, sender, qos, payload, retain, arrived from msg where msgid = ? ALLOW FILTERING").
        
-define(SELECT_MSG_BY_TOPIC, "select topic, msgid, sender, qos, payload, retain, arrived from msg where topic = ?").
        
-define(SELECT_MSG_BY_ACK, "select topic, msgid, sender, qos, payload, retain, arrived from msg where topic = ? and msgid > ?").

-define(INSERT_CLIENT1, "insert into client(clientid, node, state, connected, disconnected) values(?, ?, ?, ?, null)").

-define(INSERT_CLIENT2, "insert into client(clientid, node, state, disconnected) values(?, ?, ?, ?)").

-define(SELECT_SUB, "select topic, qos from sub where clientid = ?").

-define(SELECT_RETAIN, "select msgid from retain where topic = ?").

-define(INSERT_RETAIN, "insert into retain(topic, msgid) values(?, ?)").

-define(DELETE_RETAIN, "delete from retain where topic = ?").

-define(INSERT_ACKED, "insert into acked(clientid, topic, msgid) values(?, ?, ?)").
