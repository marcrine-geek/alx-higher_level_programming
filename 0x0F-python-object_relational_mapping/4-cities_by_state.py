#!/usr/bin/python3
"""
Lists all cities of
Database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
   """
    Access to the database and get the states
    from the database.
    """
   db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
   c = db.cursor()
   c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
               FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
                  ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")
   [print(city) for city in c.fetchall()]
