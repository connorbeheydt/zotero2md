from typing import List, Tuple, Dict
from sqlite3 import Cursor

def get_tableinfo(cur: Cursor, tablename) -> Dict:
    res = cur.execute(f"PRAGMA table_info('{tablename}')")
    tableinfo: Dict = {}
    for item in res.fetchall():
        name = item[1]
        tableinfo[name] = {}
        tableinfo[name]["index"] = item[0]
        tableinfo[name]["name"] = item[1]
        tableinfo[name]["type"] = item[2]
    return tableinfo

def get_tabledata_from_key(zotero_cur: Cursor, tablename: str, itemKey: str) -> List[Dict]:
    column_names = get_column_names(zotero_cur, tablename)
    res = zotero_cur.execute(f"""
                                SELECT *
                                FROM {tablename}
                                WHERE itemKey == {itemKey};
                                """)
    data_res = res.fetchall()
    data:  List[Dict] = []
    for item in data_res:
        item_data: Dict = {}
        for i, elem in enumerate(item):
            item_data[column_names[i]] = elem
        data.append(item_data)
    return data

def get_tabledata_from_id(zotero_cur: Cursor, tablename, itemID) -> List[Dict]:
    column_names = get_column_names(zotero_cur, tablename)
    res = zotero_cur.execute(f"""
                                SELECT *
                                FROM {tablename}
                                WHERE itemID == {itemID};
                                """)
    data_res = res.fetchall()
    data:  List[Dict] = []
    for item in data_res:
        item_data: Dict = {}
        for i, elem in enumerate(item):
            item_data[column_names[i]] = elem
        data.append(item_data)
    return data

def get_tabledata_from_parent_id(zotero_cur: Cursor, tablename, parentID) -> List[Dict]:
    column_names = get_column_names(zotero_cur, tablename)
    res = zotero_cur.execute(f"""
                                SELECT *
                                FROM {tablename}
                                WHERE parentItemID == {parentID};
                                """)
    data_res = res.fetchall()
    data:  List[Dict] = []
    for item in data_res:
        item_data: Dict = {}
        for i, elem in enumerate(item):
            item_data[column_names[i]] = elem
        data.append(item_data)
    return data

def get_annotations(zotero_cur: Cursor, parentID) -> List[Dict]:
    column_names = get_column_names(zotero_cur, "itemAnnotations")
    res = zotero_cur.execute(f"""
                                SELECT *
                                FROM itemAnnotations
                                WHERE parentItemID == {parentID};
                                """)
    data_res = res.fetchall()
    data:  List[Dict] = []
    for item in data_res:
        item_data: Dict = {}
        for i, elem in enumerate(item):
            item_data[column_names[i]] = elem
        data.append(item_data)
    return data

def get_bibdata(betterbib_cur: Cursor) -> Dict[str, Dict]:
    bibdata: Dict[str, Dict] = {}
    res = betterbib_cur.execute("""
                                SELECT *
                                from citationkey
                                """)
    for item in res.fetchall():
        bibdata[item[3]] = {"itemID": item[0], "itemKey": item[1], "libraryID": item[2], "citationKey": item[3]}
    return bibdata

def get_citation_keys(betterbib_cur: Cursor) -> List[str]:
    """betterbib_cur: cursor corresponding to BetterBibTex sqlite database."""
    res = betterbib_cur.execute("""
                                SELECT citationkey
                                FROM citationkey;
                                """)
    names_tuple: List[Tuple] = res.fetchall()
    names: List[str] = []
    for item in names_tuple:
        names.append(item[0])
    return names

def get_column_names(cur: Cursor, tablename):
    tableinfo = get_tableinfo(cur, tablename)
    return list(tableinfo.keys())

def get_table_names(cur: Cursor):
    res = cur.execute("""
                      SELECT name
                      FROM sqlite_schema
                      WHERE 
                      type ='table' AND 
                      name NOT LIKE 'sqlite_%';
                      """)
    return res

