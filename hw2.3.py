sample_text = """And since you know you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of."""                  # str, """And since you know you cannot see yourself,

search_text = input("please enter search text: ")               # str, "since"
replace_text = input("please enter replace text: ")             # str, "because"

sample_text = sample_text.replace(search_text, replace_text)    # str, """And because you know you cannot see yourself,

print(sample_text)