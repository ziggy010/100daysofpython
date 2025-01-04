from prettytable import PrettyTable;

table = PrettyTable();

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l";

print(table);

another_table = PrettyTable();

# another_table.field_names = ["Pokemon Name", "Type"];
# another_table.add_row(["Pikachu", "Electric"])
# another_table.add_row(["Squirtle", "Water"])

# print(another_table);