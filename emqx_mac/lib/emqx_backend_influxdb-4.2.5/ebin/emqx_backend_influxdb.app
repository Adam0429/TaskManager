{application,emqx_backend_influxdb,
             [{description,"EMQ X InfluxDB Backend"},
              {vsn,"4.2.5"},
              {modules,[emqx_backend_influxdb,emqx_backend_influxdb_app,
                        emqx_backend_influxdb_cli,emqx_backend_influxdb_sup]},
              {registered,[emqx_backend_influxdb_sup]},
              {applications,[kernel,stdlib,influxdb]},
              {mod,{emqx_backend_influxdb_app,[]}},
              {relup_deps,[emqx]}]}.