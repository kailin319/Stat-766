import os
import sqlite3

class HW3:
        
    def extract(self, input_files, out_db_filename) -> None:
        filenames = input_files

        for file in filenames:
            # make a connection and name the database            
            conn = sqlite3.connect(out_db_filename)
            cur = conn.cursor()
            
            # Create output table
            sql1 = '''
                CREATE TABLE IF NOT EXISTS output (
                it INTEGER, v INTEGER, epoch INTEGER, U_beta_square_sum REAL
                );'''
            cur.execute(sql1)
            
            # Insert value into output table
            sql2 = '''
                INSERT INTO output 
                (it, v, epoch, U_beta_square_sum)
                VALUES (?, ?, ?, ?);'''

            with open(file, 'r') as f:
                for line in f:
                        if (('it') in line and ('U_beta**2' in line)):
                                parts = line.split()
                                
                                # list to store it, v, epoch, Ubeta**2sum(it: 1, v: 3, epoch: 5, Ubeta**2sum: 9)
                                val = ([int(parts[1]), int(parts[3]), int(parts[5]), float(parts[9])]) 
                                cur.execute(sql2, val)
            conn.commit()
            
            # Select all rows from the database such that epoch = 0.
            cur.execute('SELECT * FROM output WHERE epoch = 0 ORDER BY it ASC, v ASC;')
            rows = cur.fetchall()
            
            # Create epoch0 table
            sql_create_epoch0_table = '''
                CREATE TABLE IF NOT EXISTS epoch0(
                it INTEGER,
                v INTEGER,
                epoch INTEGER,
                U_beta_square_sum REAL
                );'''
            cur.execute(sql_create_epoch0_table)
            
            # Insert values into epoch0 table
            sql_insert_epoch0 = '''
                    INSERT INTO epoch0 
                    (it, v, epoch, U_beta_square_sum)
                    VALUES (?, ?, ?, ?);'''
    
            # Insert value into epoch0 table
            cur.executemany(sql_insert_epoch0, rows)
            

            conn.commit()
            conn.close()