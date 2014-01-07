# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'luasocket',
      'type': 'shared_library',
      'product_dir': "<(PRODUCT_DIR)",
      'product_name': 'socket',
      'sources': [
        'src/luasocket.c',
        'src/timeout.c',
        'src/buffer.c',
        'src/io.c',
        'src/auxiliar.c',
        'src/options.c',
        'src/inet.c',
        'src/tcp.c',
        'src/udp.c',
        'src/except.c',
        'src/select.c',
      ],
      'include_dirs': [
        '.',
        '<(DEPTH)/third_party/lua/src',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua'
      ],
      'direct_dependent_settings': {
      },
      'copies': [
        { 'destination': '<(PRODUCT_DIR)',
          'files': [
            'src/ltn12.lua',
            'src/socket.lua'
        ]},
        { 'destination': '<(PRODUCT_DIR)/socket',
          'files': [
            'src/ftp.lua',
            'src/http.lua',
            'src/smtp.lua',
            'src/tp.lua',
            'src/url.lua'
        ]},
      ],  
      'conditions': [
        ['OS=="linux"', {
          'product_prefix': '',
          'cflags!': ['-fvisibility=hidden'],
          'sources': [
            'src/usocket.c'
          ],
        }],
        ['OS == "mac"', {
          'product_prefix': '',
          'product_extension': 'so',
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
          },
          'sources': [
            'src/usocket.c'
          ],
        }],
        ['OS=="win"', {
          'defines': [
            '_USRDLL',
            'LUASOCKET_EXPORTS',
            'LUASOCKET_API=__declspec(dllexport)'
          ],
          'sources': [
            'src/wsocket.c'
          ],
        }],
      ],
    },
    {
      'target_name': 'luamime',
      'type': 'shared_library',
      'product_dir': "<(PRODUCT_DIR)",
      'product_name': 'mime',
      'sources': [
        'src/mime.c',
      ],
      'include_dirs': [
        '.',
        '<(DEPTH)/third_party/lua/src',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua'
      ],
      'copies': [
        { 'destination': '<(PRODUCT_DIR)',
          'files': [
            'src/mime.lua',
          ]
        }
      ],
      'conditions': [
        ['OS=="linux"', {
          'product_prefix': '',
          'cflags!': ['-fvisibility=hidden'],
        }],
        ['OS == "mac"', {
          'product_prefix': '',
          'product_extension': 'so',
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
          },
        }],
        ['OS=="win"', {
          'defines': [
            '_USRDLL',
            'MIME_EXPORTS',
            'MIME_API=__declspec(dllexport)'
          ],
        }],
      ],
    }, 
  ]
}
