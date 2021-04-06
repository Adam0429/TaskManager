{application,emqx_bridge_rabbit,
             [{description,"EMQ X Bridge to RabbitMQ"},
              {vsn,"4.2.5"},
              {modules,[emqx_bridge_rabbit,emqx_bridge_rabbit_app,
                        emqx_bridge_rabbit_ch,emqx_bridge_rabbit_sup]},
              {registered,[emqx_bridge_rabbit_sup]},
              {applications,[kernel,stdlib,amqp_client,ecpool,recon]},
              {mod,{emqx_bridge_rabbit_app,[]}},
              {relup_deps,[emqx]}]}.