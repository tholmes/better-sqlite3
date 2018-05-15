{
  'includes': [ 'deps/common.gypi' ],
  'targets': [
    {
      'target_name': '<(module_name)',
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
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
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
    },
  ]
}
