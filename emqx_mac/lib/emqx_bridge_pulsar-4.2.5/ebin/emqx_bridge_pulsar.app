{application,emqx_bridge_pulsar,
             [{description,"EMQ X Bridge to Pulsar"},
              {vsn,"4.2.5"},
              {modules,[emqx_bridge_pulsar,emqx_bridge_pulsar_app,
                        emqx_bridge_pulsar_sup]},
              {registered,[emqx_bridge_pulsar_app]},
              {applications,[kernel,stdlib,pulsar]},
              {mod,{emqx_bridge_pulsar_app,[]}},
              {relup_deps,[emqx]}]}.