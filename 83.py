#-----------------------------------------
#tryブロックを短く保つ！

#例外処理を行う際に予期しうる例外を適切に処理には大きなオーバーエッドがかかる

#Connection = ...
#class RpcError(Exception):
    #...
#def lookup_request(connection):
    #...
    #raise RpcError("From lookup_request")
#def close_connection(connection):
    #...
    #print("Connection Closed")

#try:
    #request = lookup_request(connection)
#excrpt RpcError:
    #print("Encountered error!")
    #close_connection(connection)
    
#🥰try内で収集したデータを処理したり、特殊なケースに対応する場合🥰

#def lookup_request(connection):
    #エラーは発生しない
    #...

#def is_cached(connection, request):
    #...
    #raise RpcError("From is_cached")

#try:
    #request = lookup_request(connection)
    #if is_cached(connection, request):
        #request = None
#excrpt RpcError:
    #print("Encountered error!")
    #close_connection(connection)
    
#👆のコードの問題点は、is_cachedないでもRpcErrorが発生する可能性があるため、同じtry/exceptで呼び出すと、lookup_requestとis_cachedのどちらでエラーが起きたのかわからない

#if is_cloed(connection):
    # 接続をcloseしたのは、lookup_requestかis_cachedのエラーによるものかわからない
    #...
    
#そのため📚tryで予期されるエラーは１つだけになるようにする

#try:
    #request = lookup_request(connection) 👈tryに複数書かず1つにする
#except RpcError:
    #close_connection(connection)
#else:
    #if is_cached(connection, request): #移動した
        #request = None


