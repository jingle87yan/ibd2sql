#!/usr/bin/env python3
from pathlib import Path
from main import process__
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="解析位置参数示例")

# 添加位置参数
parser.add_argument("filepath", help="文件夹路径")
parser.add_argument("type", help="脚本类型[0:只有表结构，1只有表数据，2表与数据都有]")
parser.add_argument("savefile", help="脚本保存文件名")

# 解析参数
args = parser.parse_args()
# 访问位置参数
print("第一个参数:", args.filepath)
print("第二个参数:", args.type)
print("第三个参数:", args.savefile)

directory = Path(args.filepath)
files = [f.name for f in directory.iterdir() if f.is_file()]
type__ = (False if "0" == args.type else True)

create_file = True
for file in files:
    if not file.endswith(".ibd"):
        continue
    create_sql, insert_sql = process__(args.filepath + "\\" + file, type__)
    if args.type == "2" or args.type == "0":
        # 保存表结构脚本
        if create_sql is not None and len(create_sql) > 0:
            with open(args.savefile, "w" if create_file else 'a', encoding="utf-8") as fil:
                create_file = False
                fil.write(create_sql)
    if args.type == "1" or args.type == "2":
        if insert_sql is not None and len(insert_sql) > 0:
            with open(args.savefile, "w" if create_file else 'a', encoding="utf-8") as fil:
                create_file = False
                fil.write("\n".join(insert_sql))
