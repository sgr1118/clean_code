class dbhandler_decorator(contextlib.ContextDecorator):
    def __init__(self):
        stop_database()
        
    def __init__(self, ext_type, ex_value, ex_traceback):
        start_database()
        
@dbhandler_decoreator()
def offline_backup():
    run("pg_dump database")
    
# 컨텍스트 관리자를 데코레이터로 지정해주면 offline_backup 함수를
# 호출만 하더라도 컨텍스트 관리자 안에서 자동으로 실행