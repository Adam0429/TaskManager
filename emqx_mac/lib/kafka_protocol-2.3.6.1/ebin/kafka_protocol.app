{application,kafka_protocol,
             [{description,"Kafka protocol library for Erlang/Elixir"},
              {vsn,"2.3.6.1"},
              {registered,[]},
              {applications,[kernel,stdlib,ssl,snappyer,crc32cer]},
              {env,[]},
              {modules,[kpro,kpro_api_vsn,kpro_auth_backend,kpro_batch,
                        kpro_batch_v01,kpro_brokers,kpro_compress,
                        kpro_connection,kpro_consumer_group,kpro_lib,
                        kpro_prelude_schema,kpro_req_lib,kpro_rsp_lib,
                        kpro_sasl,kpro_schema,kpro_scram,kpro_sent_reqs,
                        kpro_txn_lib,kpro_varint]},
              {licenses,["Apache License 2.0"]},
              {links,[{"Github","https://github.com/klarna/kafka_protocol"}]},
              {build_tools,["rebar","rebar3"]},
              {files,["src","include","priv/kafka.bnf","rebar.config",
                      "rebar.config.script","README.md","LICENSE","NOTICE",
                      "Makefile"]}]}.