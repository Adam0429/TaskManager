{application,opentsdb,
             [{description,"OpenTSDB Client"},
              {vsn,"0.5.0"},
              {modules,[opentsdb,opentsdb_app,opentsdb_sup]},
              {registered,[opentsdb_sup]},
              {applications,[kernel,stdlib,jsx,hackney]},
              {mod,{opentsdb_app,[]}}]}.
