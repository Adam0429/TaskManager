{application,clickhouse,
             [{description,"ClickHouse Client"},
              {vsn,"0.1"},
              {modules,[clickhouse,clickhouse_app,clickhouse_sup]},
              {registered,[clickhouse_sup]},
              {applications,[kernel,stdlib,hackney]},
              {mod,{clickhouse_app,[]}}]}.
