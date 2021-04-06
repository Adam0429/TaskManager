{application,emqx_bridge_rocket,
             [{description,"EMQ X Bridge to RocketMQ"},
              {vsn,"4.2.5"},
              {modules,[emqx_bridge_rocket,emqx_bridge_rocket_app,
                        emqx_bridge_rocket_sup]},
              {registered,[emqx_bridge_rocket_app]},
              {applications,[kernel,stdlib,rocketmq]},
              {mod,{emqx_bridge_rocket_app,[]}},
              {relup_deps,[emqx]}]}.