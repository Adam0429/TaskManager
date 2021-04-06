{application,tdengine,
             [{description,"TDengine Client"},
              {vsn,"0.1.0"},
              {modules,[tdengine,tdengine_app,tdengine_sup]},
              {registered,[tdengine_sup]},
              {applications,[kernel,stdlib,hackney]},
              {mod,{tdengine_app,[]}}]}.
