{application,emqx_bridge_kafka,
             [{description,"EMQ X Bridge to Kafka"},
              {vsn,"4.2.5"},
              {modules,[emqx_bridge_kafka,emqx_bridge_kafka_app,
                        emqx_bridge_kafka_cli,emqx_bridge_kafka_sup]},
              {registered,[emqx_bridge_kafka_sup]},
              {applications,[kernel,stdlib,wolff,erlavro,jsx,brod]},
              {mod,{emqx_bridge_kafka_app,[]}},
              {relup_deps,[emqx]}]}.