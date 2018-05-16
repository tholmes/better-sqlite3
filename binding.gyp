{
  'includes': [ 'deps/common.gypi' ],
  'targets': [
    {
      'target_name': 'better_sqlite3',
      'dependencies': [
        'deps/sqlite3.gyp:sqlite3'
      ],
      'cflags': [
        '-std=c++11'
      ],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [
          '-std=c++11',
          '-stdlib=libc++'
        ],
      },
      'sources': [
        'src/better_sqlite3.cpp'
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "better_sqlite3" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/better_sqlite3.node" ],
          "destination": "<(module_path)"
        }
      ]
    },
    {
      'target_name': 'test_extension',
      'dependencies': [
        'deps/sqlite3.gyp:action_before_build'
      ],
      'cflags_cc': [
        '-Wno-unused-value',
      ],
      'sources': [
        'deps/test_extension.c'
      ]
    }
  ]
}
