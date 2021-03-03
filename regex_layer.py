import re


def check_regex(test_query):
    bool_patterns = ["^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+\d+\s*=\s*\d+",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND|OR NOT)\s+'([\w]+\s*)+'\s*=\s*'([\w]+\s*)+'",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND|OR NOT)\s+'([\w]+\s*)+'\s*=\s*'([\w]+\s*)+'",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND){0,1}\s+MAKE_SET\(\s*\d+\s*=\s*\d+\s*,\s*\d+\s*\)",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND){0,1}\s+ELT\(\s*\d+\s*=\s*\d+\s*,\s*\d+\s*\)",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+(\s*\d+\s*=\s*\d+\s*)\s*\*\s*\d+",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?IIF\(\s*\d+\s*=\s*\d+\s*,\s*\d+\s*,\s*\d+\s*/\s*\d+\s*\)"]
    time_patterns = ["^(SELECT |UPDATE |DELETE |INSERT ).*?SLEEP\(\s*\d+\s*\)",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?WAITFOR\s+DELAY\s+'[\d:]+'",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(ALL_USERS\s+T\d+,?){3,}",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(SYSUSERS\s+AS\s+SYS\d+,?){3,}",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?BENCHMARK\(",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?GENERATE_SERIES\(\s*\d+",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?DBMS_PIPE\.RECEIVE_MESSAGE\(",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(SYSIBM\.SYSTABLES\s+AS\s+T\d+(,){0,1}){3,}",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?UPPER\(HEX\(RANDOMBLOB",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(RDB\$[\w]+\s+AS\s+T\d+,?){3,}",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?(DOMAIN\.[\w]+\s+AS\s+T\d+,?){3,}",
                     "^(SELECT |UPDATE |DELETE |INSERT ).*?REGEXP_SUBSTRING\(REPEAT"]
    error_patterns = ["^(SELECT |UPDATE |DELETE |INSERT ).*?EXP\(\s*~\(\s*SELECT\s+?\*\s+?FROM",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?JSON_KEYS\(\(\s*SELECT\s+CONVERT",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?EXTRACTVALUE\(\d+",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+UPDATEXML\(\s*[\d]+",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?ROW\(\s*\d+\s*,\s*\d+\s*\)\>",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?END\s*\)\)::text",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?CONVERT\(\s*INT",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+XMLTYPE\(\s*CHR\(\s*\d+\s*\)\s+",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+DUTL_INADDR\.GET_HOST_ADDRESS\(",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?(OR|AND)\s+CTXSYS\.DRITHSX\.SN\(\s*\d+",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?DBMS_UTILITY\.SQLID_TO_SQLHASH\(",
                      "^(SELECT |UPDATE |DELETE |INSERT ).*?FLOOR\(.+?\(\s*\d+?\s*\)\*\d+?\)"]
    union_patterns = [
        "^(SELECT |UPDATE |DELETE |INSERT ).*?UNION(\s+ALL){0,1}\s+SELECT"]
    stacked_patterns = ["^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*SELECT",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*UPDATE",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*INSERT",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*DELETE",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*DROP",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*WAITFOR\sDELAY",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*CALL",
                        "^(SELECT |UPDATE |DELETE |INSERT ).*?;\s*BEGIN"]
    test_dict = {test_query: 0}
    for pattern in bool_patterns:
        if len(re.findall(pattern, test_query)) > 0:
            test_dict[test_query] = 1
    for pattern in time_patterns:
        if len(re.findall(pattern, test_query)) > 0:
            test_dict[test_query] = 1
    for pattern in error_patterns:
        if len(re.findall(pattern, test_query)) > 0:
            test_dict[test_query] = 1
    for pattern in union_patterns:
        if len(re.findall(pattern, test_query)) > 0:
            test_dict[test_query] = 1
    for pattern in stacked_patterns:
        if len(re.findall(pattern, test_query)) > 0:
            test_dict[test_query] = 1
    for item in test_dict:
        if test_dict.get(item) == 1:
            print("MALICIOUS QUERY DETECTED")
            return True
        else:
            print("BENIGN QUERY")
            return False
