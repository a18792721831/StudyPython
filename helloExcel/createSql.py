import time


def getSql(value, description, name, author):
    sql = '''
--AUTHOR:''' + author + '''
--DATE:''' + time.strftime('%Y-%m-%d %H:%M:%S',
                           time.localtime(time.time())) + '''
--REMARK:''' + description +  '''
DECLARE
  V_COUNT NUMBER;
BEGIN
  SELECT COUNT(*)
    INTO V_COUNT
    FROM ENUMINFOEN EF
   WHERE EF.NAMESTR = UPPER(\'''' + name + '''\');
  IF V_COUNT < 1 THEN
    INSERT INTO ENUMINFOEN
      (NAMESTR,
       MESSAGEINFO,
       CLASSNAMESTR,
       CLASSREMARK,
       ENUMVALUES,
       MESSAGEISEMPTY,
       CREATEDT,
       MODIFYDT)
    VALUES
      (\'''' + name + '''\',
       \'''' + description + '''\',
       \'APPOPERATETYPE\',
       \'APP操作类型\',
       ''' + str(value) + ''',
       \'\',
       SYSDATE,
       NULL);
    COMMIT;
  END IF;
END;
/
'''
    return sql

# getSql(0,'登录','LOGIN','JIAYQ')