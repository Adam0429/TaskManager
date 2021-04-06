{application,influxdb,
             [{description,"InfluxDB Client"},
              {vsn,"0.5.1"},
              {modules,[influxdb,influxdb_app,influxdb_line,influxdb_sup]},
              {registered,[influxdb_sup]},
              {applications,[kernel,stdlib]},
              {mod,{influxdb_app,[]}}]}.
