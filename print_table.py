#! python3

def print_table():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bab', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
    # lenの表の列分だけ0が並んだリストを作成する
    col_widths = [0] * len(table_data)
    for i in range(len(col_widths)):
        for j in range(len(table_data[i])):
            if(col_widths[i] < len(table_data[i][j])):
               col_widths[i] = len(table_data[i][j])
    i = 0
    for i in range(len(table_data[i])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j] + 1), end = '')
        print()

print_table()
